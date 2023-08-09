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
        left = bc.borderContainer(region='left',width='50%')
        left.roundedGroup(title='Dati testata', region='center').templateChunk(table='fatt.offerta',
                                        record_id='^#FORM.record.id', template='dati_offerta', height='100%', padding='10px')
        fb = left.roundedGroup(title='Dati spedizione', hidden="^.offerta_tipo?=#v!='B'",
                               region='bottom', height='90px').formbuilder(cols=1, border_spacing='4px')
        fb.field('peso_spedizione')
        fb.field('costo_spedizione')

        bc.contentPane(region='center').linkerBox('cliente_id',margin='2px',openIfEmpty=True, validate_notnull=True,
                                                    columns='$ragione_sociale,$provincia,@cliente_tipo_codice.descrizione',
                                                    auxColumns='@comune_id.denominazione,$provincia',
                                                #    clientTemplate=True,
                                                    newRecordOnly=True,formResource='Form',
                                                    dialog_height='500px',dialog_width='800px')
        
    