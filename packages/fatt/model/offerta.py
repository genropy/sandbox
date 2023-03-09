from gnr.core.gnrdecorator import public_method
from gnr.core.gnrnumber import decimalRound

class Table(object):
    def config_db(self, pkg):
        tbl =  pkg.table('offerta', pkey='id',name_long=u'!![it]Offerta',
                    name_plural=u'!![it]Offerta',
                    rowcaption='protocollo',
                    caption_field='protocollo')
        self.sysFields(tbl,draftField=True)  
        tbl.column('cliente_id',size='22',group='_',name_long='!![it]Cliente').relation('fatt.cliente.id',
                    mode='foreignkey',onDelete='raise')
        tbl.column('offerta_tipo' ,size=':5',name_long='!![it]Tipo offerta',validate_notnull=True).relation('fatt.offerta_tipo.codice',
                                                                                    mode='foreignkey')
        tbl.column('codice_contatore', size=':2', name_long='C.Cont',defaultFrom='@offerta_tipo') #copiato da tipo_offerta
        tbl.column('protocollo',size=':16',name_long='!![it]Protocollo',indexed=True,unique=True)   
        tbl.column('data_protocollo','D',name_long='!![it]Data protocollo')

        tbl.column('totale_imponibile',dtype='money',name_long='!![it]Totale imponibile')
        tbl.column('totale_lordo',dtype='money',name_long='!![it]Totale lordo')
        tbl.column('totale_iva',dtype='money',name_long='!![it]Totale Iva')
        tbl.column('_righe_documento',dtype='X',name_long='!![it]Righe Bozza',group='_',_sendback=True)
        tbl.column('filepath',name_long='!!Filepath',name_short='Filepath')
        tbl.formulaColumn('fileurl',"""CASE WHEN $filepath IS NOT NULL THEN '/' || $filepath ||'?_lazydoc=fatt.offerta,' || $id ELSE NULL END || '&_mod_ts=' || $__mod_ts""",name_long='Fileurl') 
        

    def defaultValues(self):
        return dict(data_protocollo=self.db.workdate,__is_draft=True)

    def counter_protocollo(self,record=None):
        pars = dict(format='$K/$YYYY.$NNNNN',period='YY',code='**',
                    date_field='data_protocollo',
                    showOnLoad=False,recycle=True)
        if record:
            pars['code'] = record['codice_contatore']
        return pars

    def trigger_onInserting(self,record):
        record['filepath'] = self.getDocumentPath(record)

    def trigger_onUpdating(self,record,old_record=None):
        if self.fieldsChanged('__is_draft',record,old_record):
            if record['__is_draft']:
                record['_righe_documento'] = self.ricostruisciRigheDraft(self.righeDocumento(record['id']))
                self.db.table('fatt.offerta_riga').deleteSelection('$offerta_id',record['id'])
            elif record['_righe_documento']:
                righe_offerta = record['_righe_documento']
                self.aggiornaRigheOfferta(record,righe_offerta=righe_offerta)
                record['_righe_documento'] = None
        self.delete_cached_document_pdf(record)
        record['filepath'] = self.getDocumentPath(record)

    def trigger_onDeleting(self,record):
        self.delete_cached_document_pdf(record)


    def aggiornaRigheOfferta(self,offerta,righe_offerta=None):
        """Eplosione delle righe da bag a tabella"""
        offerta = self.recordAs(offerta,'dict')
        offerta_id= offerta['id']
        tblrighe = self.db.table('fatt.offerta_riga')
        righe_correnti = tblrighe.query(where='$offerta_id=:oid',oid=offerta_id).fetchAsDict('id')
        if righe_offerta:
            for v, pkey in righe_offerta.digest('#v,#a._pkey'):
                if pkey in righe_correnti:
                    righe_correnti.pop(pkey)
                    with tblrighe.recordToUpdate(pkey=pkey) as record:
                        record.update(v)
                else:
                    v['offerta_id'] = offerta_id
                    tblrighe.insert(v)
        for v in righe_correnti.values():
            tblrighe.delete(v)


    def ricalcolaTotali(self,offerta_id=None):
        with self.recordToUpdate(offerta_id) as record:
            totale_lordo,totale_netto = self.db.table('fatt.offerta_riga'
                                                    ).readColumns(columns="""SUM($importo_lordo) AS totale_lordo,
                                                                             SUM($importo_netto) AS totale_netto""",
                                                                             where='$offerta_id=:f_id',f_id=offerta_id)
            
            record['totale_imponibile'] = totale_netto
            record['totale_lordo'] = totale_lordo
            record['totale_iva'] = record['totale_lordo'] - record['totale_imponibile'] 

################### GESTIONE DRAFT #####################################################

    def ricostruisciRigheDraft(self,righe_ddt):
        """Ritorno a draft"""

        colitems = self.db.table('fatt.offerta_riga').columns.items()
        excludefields = [field for field,col in colitems \
                        if col.attributes.get('_sysfield') or col.attributes.get('righe_draft') is False]
        excludefields.append('_pkey')
        for r in righe_ddt.values():
            for k in r.keys():
                if k in excludefields:
                    r.pop(k)
        return righe_ddt

    @public_method
    def riportaABozza(self,ddt_id=None,doCommit=True,**kwargs):
        with self.recordToUpdate(ddt_id) as record:
            record['__is_draft'] = True
            record['protocollo'] = None
        if doCommit:
            self.db.commit()

################### TRASFORMAZIONE IN BAG #####################################################
    def righeDocumento(self,offerta_id=None):
        tblrighe = self.db.table('fatt.offerta_riga')
        result = tblrighe.query(where='$offerta_id=:oid',oid=offerta_id,bagFields=True).selection().output('baglist')
        return result
        
################### GESTIONE STAMPA CACHED ##########################################
    def getDocumentPath(self,record,**kwargs):
        data_protocollo = record['data_protocollo']
        filename = record['protocollo'] or record['id']
        prefix = 'offerta:'
        return '%s%04i/%02i/%s.pdf' %(prefix,data_protocollo.year,data_protocollo.month,filename.replace('/','_').replace('.','_'))
        
    def check_cached_document_pdf(self,record):
        path = self.getDocumentPath(record)
        create = False
        site = self.db.application.site
        if not site.storageNode(path).exists:
            create = True
        if create:
            self.create_cached_document_pdf(record)
        return path

    def create_cached_document_pdf(self,record):
        record= self.recordAs(record)
        self.doCreatePdfDoc(record)

    def doCreatePdfDoc(self,record):
        page = self.db.currentPage
        if page:
            htmlbuilder = page.loadTableScript(self, 'html_res/stampa_offerta')
            htmlbuilder(record = record,pdf=True)

    def delete_cached_document_pdf(self,record):
        if record['filepath']:
            site = self.db.application.site
            sn = site.storageNode(record['filepath'])
            if sn.exists:
                sn.delete()
