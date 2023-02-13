# -*- coding: utf-8 -*-
from gnr.core.gnrdecorator import public_method,customizable
from gnr.web.gnrbaseclasses import BaseComponent,page_proxy
from gnr.core.gnrnumber import decimalRound

@page_proxy(inherites='gnrcomponents/master_detail/master_detail:MasterDetail')
class Offerta(BaseComponent):
    detail_grid_customizer = '@offerta_tipo.conf_grid'
    detail_tbl = 'fatt.offerta_riga'
    detail_viewResource = 'ViewFromOfferta'

    @public_method
    def rowController(self,row=None,field=None,row_attr=None,**kwargs):
        field = field or 'prodotto_id' #nel caso di inserimento batch il prodotto viene considerato campo primario
        if not row['prodotto_id']:
            return row
        if not row['quantita']:
            row['quantita'] = 0
       #if field == 'prodotto_id':
       #    prezzo_unitario,aliquota_iva = self.db.table('fatt.prodotto').readColumns(columns='$prezzo_unitario,@tipo_iva_codice.aliquota',pkey=row['prodotto_id'])
       #    row['prezzo_unitario'] = prezzo_unitario
       #    row['aliquota_iva'] = aliquota_iva
        if row['sconto']:
            #Lo sconto inserito viene confrontato con lo sconto massimo inserito nelle preferenze
            max_sconto = self.getPreference('generali.max_sconto', pkg='fatt')
            sconto = row['sconto'] if row['sconto'] < max_sconto else max_sconto
            row['sconto'] = sconto * row['prezzo_unitario'] / 100
        else:
            row['sconto']=0
        row['importo_lordo'] = decimalRound(row['quantita'] * (row['prezzo_unitario']))
        row['importo_netto'] = decimalRound(row['quantita'] * (row['prezzo_unitario']-row['sconto']))
        return row
    
    @customizable
    def righe(self,bc):
        return self.detailsGrid(bc.contentPane(region='center'),nodeId='dettaglio_offerta',
                            title='Righe offerta',margin='2px',
                                storepath='#FORM.record._righe_documento')

    @customizable
    def tabCentrale(self,tc):
        self.righe(tc.borderContainer(title='!![it]Dettaglio'))
        self.stampa(tc.borderContainer(title='!![it]Stampa'))
        self.allegati(tc.borderContainer(title='!![it]Allegati'))

    def stampa(self,bc):
        bc.contentPane(region='center').iframe(height='100%',width='100%',border=0,src='^#FORM.record.fileurl',_virtual_column='fileurl',
                                                                documentClasses=True,avoidCache=True)

    def allegati(self,bc):
        bc.contentPane(region='center').attachmentMultiButtonFrame()


    @customizable
    def testata(self,bc):
        bc.contentPane(region='center').linkerBox('cliente_id',margin='2px',openIfEmpty=True, validate_notnull=True,
                                                    columns='$ragione_sociale,$provincia,@cliente_tipo_codice.descrizione',
                                                    auxColumns='@comune_id.denominazione,$provincia',
                                                #    clientTemplate=True,
                                                    newRecordOnly=True,formResource='Form',
                                                    dialog_height='500px',dialog_width='800px')
        left = bc.roundedGroup(title='Dati testata',region='left',width='50%')
        fb = left.formbuilder(cols=1, border_spacing='4px')
        fb.field('offerta_tipo')
        fb.field('protocollo',readOnly=True)
        fb.field('data_protocollo')