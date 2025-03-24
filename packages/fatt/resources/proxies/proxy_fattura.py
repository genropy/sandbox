# -*- coding: utf-8 -*-

from gnr.core.gnrnumber import decimalRound
from gnr.core.gnrdecorator import public_method
from gnr.web.gnrbaseclasses import BaseComponent,page_proxy

@page_proxy(inherites='gnrcomponents/master_detail/master_detail:MasterDetail')
class Fattura(BaseComponent):
    detail_grid_customizer = '@tipo_id.conf_grid'
    detail_tbl = 'fatt.fattura_riga'
    detail_viewResource = 'ViewFromFattura'

    @public_method
    def rowController(self,row=None,field=None,**kwargs):
        field = field or 'prodotto_id' #nel caso di inserimento batch il prodotto viene considerato campo primario
        if not row['prodotto_id']:
            return row
        if not row['quantita']:
            row['quantita'] = 1
        if field == 'prodotto_id':
            descrizione,prezzo_unitario,aliquota_iva = self.db.table('fatt.prodotto').readColumns(columns='$descrizione,$prezzo_unitario,@tipo_iva_codice.aliquota',pkey=row['prodotto_id'])
            row['prezzo_unitario'] = prezzo_unitario
            row['aliquota_iva'] = aliquota_iva
            row['descrizione_prodotto'] = descrizione
        if row['sconto']:
            #Lo sconto inserito viene confrontato con lo sconto massimo inserito nelle preferenze
            max_sconto = self.getPreference('generali.max_sconto', pkg='fatt')
            sconto = row['sconto'] if row['sconto'] < max_sconto else max_sconto
            row['sconto'] = sconto * row['prezzo_unitario'] / 100
        else:
            row['sconto']=0
        row['prezzo_totale'] = decimalRound(row['quantita'] * (row['prezzo_unitario']-row['sconto']))
        row['iva'] = decimalRound((row['aliquota_iva'] * row['prezzo_totale'])/100)
        return row



    def testata(self,parent,**kwargs):
        bc = parent.borderContainer(datapath='#FORM.record',**kwargs)
        self.selectCliente(bc,region='left',width='320px')
        self.datiTestata(bc,region='center')

    def datiTestata(self,parent,**kwargs):
        fl = parent.contentPane(**kwargs).formlet(cols=3)
        fl.field('data',disabled=True)
        fl.field('tipo_id',disabled=True)
        fl.field('protocollo',disabled=True)

    def selectCliente(self,parent,**kwargs):
        pane = parent.contentPane(**kwargs)
        pane.linkerBox('cliente_id',
                margin='2px',openIfEmpty=True, validate_notnull=True,
                    columns='$ragione_sociale,$provincia,@cliente_tipo_codice.descrizione',
                    auxColumns='@comune_id.denominazione,$provincia',
                    newRecordOnly=True,formResource='Form',
                    dialog_height='500px',dialog_width='800px')


    def righe(self,bc,storepath=None,**kwargs):
        self.detailsGrid(bc.contentPane(**kwargs),title='Righe offerta',
                                storepath=storepath)


    def defaultPromptFields(self):
        return [dict(value='^.tipo_id',lbl='Tipo',validate_notnull=True,
                        tag='dbselect',hasDownArrow=True,
                        table='fatt.fattura_tipo')]