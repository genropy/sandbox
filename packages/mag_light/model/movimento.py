#!/usr/bin/env python
# encoding: utf-8

from gnr.core.gnrdecorator import public_method

class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('movimento', pkey='id', name_long='!![it]Movimento', name_plural='!![it]Movimenti', caption_field='protocollo',
                            partition_deposito_codice='deposito_codice')
        self.sysFields(tbl)
        
        tbl.column('protocollo', size='10', name_long='!![it]Protocollo')
        tbl.column('movimento_tipo', size='3', group='_', name_long='!![it]Tipo movimento').relation(
                        'movimento_tipo.codice', relation_name='movimenti', mode='foreignkey', onDelete='raise')
        tbl.column('immediato', dtype='B', name_long='Tipo movimento immediato')
        tbl.column('verso', size='1', name_long='Verso movimento')
        tbl.column('movimento_id', size='22', group='_', name_long='!![it]Trasferimento partenza').relation(
                        'movimento.id', one_one='*', mode='foreignkey', onDelete='cascade')
        tbl.column('deposito_codice', size='3', group='_', name_long='!![it]Deposito').relation(
                        'deposito.codice', relation_name='movimenti', mode='foreignkey', onDelete='raise')         
        tbl.column('campi_aggiuntivi', dtype='X', name_long='Campi aggiuntivi', subfields='movimento_tipo')
        tbl.column('data', dtype='D', name_long='Data')
        tbl.column('data_conferma', dtype='D', name_long='Data conferma')
        tbl.column('note', name_long='!![it]Note')
        tbl.column('numero_vettura', name_long='Num. Vettura')
        tbl.column('rif_ordine', name_long='Rif. Ordine')
        tbl.column('causale_eliminazione', name_long='Causale eliminazione', values='Merce scaduta, Merce danneggiata, Altro')
        tbl.column('rif_vendita', name_long='Rif. Vendita')
        tbl.column('confermato_da', name_long='Confermato da', unmodifiable=True)

   #     tbl.formulaColumn('__protected_by_confermato', "($in_attesa IS NOT TRUE)", dtype='B')
        tbl.formulaColumn('in_attesa', "$data_conferma IS NULL", dtype='B', static=True, name_long='!![it]Movimento in attesa')
        tbl.formulaColumn('status', """CASE WHEN $in_attesa IS NOT TRUE AND $verso='S' THEN 'Scarico Effettuato' 
                                        WHEN $in_attesa IS NOT TRUE AND $verso='C' THEN 'Carico Effettuato'
                                        ELSE 'In attesa' END""", static=True, name_long='Status')
        tbl.formulaColumn('creato_arrivo', '@movimento.id IS NOT NULL', static=True, name_long='Creato arrivo', dtype='B')

    def setDefaultValues(self, record):
        record['data'] = record['data'] or self.db.workdate
        record['deposito_codice'] = record['deposito_codice'] or self.db.currentEnv['current_deposito_codice']
        record['immediato'], record['verso'] = self.db.table('mag_light.movimento_tipo').readColumns(
                                record['movimento_tipo'], columns='$immediato,$verso') 
        if record['immediato']:
            record['data_conferma'] = record['data']
    
    def trigger_onInserting(self, record):
        self.setDefaultValues(record)

    def trigger_onUpdated(self, record, old_record=None):
        if self.fieldsChanged('data_conferma', record, old_record) and not old_record['data_conferma']:
            self.db.table('mag_light.movimento_riga').confermaRighe(record)

    def counter_protocollo(self,record=None):
        #K21/DEP001 con codice uguale al verso del tipo movimento
        code = self.db.table('mag_light.movimento_tipo').readColumns(where='$codice=:cod', 
                                        cod=record['movimento_tipo'], columns='$verso')
        dep = self.db.table('mag_light.deposito').readColumns(where='$id=:dep_id', 
                                        dep_id=record['deposito_codice'], columns='$codice')
        return dict(format='$K$YY/{DEP}$NNN'.format(DEP=dep), code=code, 
                                        period='YY', date_field='data')

    @public_method
    def confermaMovimento(self, movimento_id=None, **kwargs):
        with self.recordToUpdate(movimento_id) as record:
            record['data_conferma'] = self.db.workdate
            if record['verso'] == 'C':
                record['confermato_da'] = self.db.currentEnv['user']
        self.db.commit()

    @public_method
    def creaTrasferimento(self, movimento_id=None, deposito_codice=None, **kwargs):
        movimento_rec = self.record(movimento_id).output('bag')
        movimento_tipo = 'TRU' if movimento_rec['movimento_tipo'] == 'TRE' else 'TRE'
        trasferimento = self.newrecord(movimento_id=movimento_id, 
                            movimento_tipo=movimento_tipo, deposito_codice=deposito_codice)
        self.insert(trasferimento)

        movimenti_righe = self.db.table('mag_light.movimento_riga').query(where='$movimento_id=:mov_id', 
                                            mov_id=movimento_id).fetch()
        
        for movimento_riga in movimenti_righe:
            quantita = movimento_riga['quantita'] or movimento_riga['quantita_attesa']
            trasferimento_riga = self.db.table('mag_light.movimento_riga').newrecord(prodotto_id=movimento_riga['prodotto_id'], 
                                movimento_id=trasferimento['id'], movimento_riga_id=movimento_riga['id'], 
                                deposito_codice=deposito_codice, quantita_attesa= - (quantita))

            self.db.table('mag_light.movimento_riga').insert(trasferimento_riga)

        self.db.commit()

    @public_method
    def confermaTrasferimento(self, movimento_id=None):
        with self.recordToUpdate(where='@movimento.id=:mov_id', mov_id=movimento_id) as record:
            record['data_conferma'] = self.db.workdate