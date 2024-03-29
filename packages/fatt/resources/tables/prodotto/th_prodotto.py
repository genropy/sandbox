#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method
from decimal import Decimal

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('codice')
        r.fieldcell('prodotto_tipo_id',width='30em')
        r.fieldcell('descrizione',width='30em')
        r.fieldcell('prezzo_unitario')
        r.cell('azione',calculated=True,format_buttonclass='gear iconbox',
                    format_isbutton=True,
                    format_onclick="""var row = this.widget.rowByIndex($1.rowIndex);
                                      PUBLISH esegui_azione = {prodotto_id:row._pkey};""",
                    cellClassCB="""var row = cell.grid.rowByIndex(inRowIndex);
                                    if(row.codice=='C1'){
                                        return 'hidden';
                                    }""")

    def th_order(self):
        return 'codice'

    def th_query(self):
        return dict(column='codice', op='contains', val='')

    def th_view(self,view):
        view.dataRpc('dummy',self.eseguiAzioneTest,subscribe_esegui_azione=True)

    @public_method
    def eseguiAzioneTest(self,prodotto_id=None):
        with self.db.table('fatt.prodotto').recordToUpdate(prodotto_id) as record:
            record['prezzo_unitario'] = record['prezzo_unitario']*Decimal('1.5')
        self.db.commit()



class Form(BaseComponent):
    py_requires="""gnrcomponents/dynamicform/dynamicform:DynamicForm,
                   gnrcomponents/attachmanager/attachmanager:AttachManager"""

    def th_form(self, form):
        form.css('.box_produzione_invalid label',"color:red;")

        bc = form.center.borderContainer()
        self.datiProdotto(bc.borderContainer(region='top',datapath='.record',height='180px'))
        tc = bc.tabContainer(region='center',margin='2px')
        self.caratteristicheProdotto(tc.contentPane(title='Caratteristiche',datapath='.record', 
                                                    checkpref='fatt.magazzino.abilita_df_magazzino'))
        self.venditeProdotto(tc.contentPane(title='Vendite'))
        self.allegatiProdotto(tc.contentPane(title='Allegati'))

    def allegatiProdotto(self,pane):
        pane.attachmentMultiButtonFrame()


    def caratteristicheProdotto(self,pane):
        pane.dynamicFieldsPane('caratteristiche')

    def datiProdotto(self,bc):
        left = bc.roundedGroup(region='center',title='Dati prodotto').div(margin='10px',margin_right='20px')
        fb = left.formbuilder(cols=2, border_spacing='4px',colswidth='auto',fld_width='100%',width='600px')
        fb.field('prodotto_tipo_id',tag='hdbselect',validate_notnull=True,colspan=2)
        fb.field('codice',validate_notnull=True,validate_case='U',validate_nodup=True)
        fb.br()
        fb.field('descrizione',validate_notnull=True,colspan=2)
        fb.field('prezzo_unitario',validate_notnull=True)
        fb.field('tipo_iva_codice',validate_notnull=True)
        center = bc.roundedGroup(region='right',title='Immagine',width='130px')
        center.img(src='^.foto_url',crop_height='100px',crop_width='100px',margin='5px',
                    crop_border='2px dotted silver',crop_rounded=6,edit=True,
                    placeholder=True,upload_folder='site:prodotti/immagini',
                    upload_filename='=#FORM.record.codice')

    def venditeProdotto(self,pane):
        pane.plainTableHandler(relation='@righe_fattura',viewResource='ViewFromProdotto')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px', duplicate=True)
        #Utilizzando duplicate=True mostreremo un'icona per la duplicazione del record direttamente nella Form.
        #Tenendo premuto Maiusc durante il clic verrà anche mostrata la possibilità di inserire un numero di copie o delle 
        #etichette personalizzate