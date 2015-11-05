#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('protocollo')
        r.fieldcell('cliente_id',zoom=True)
        r.fieldcell('data')
        r.fieldcell('totale_imponibile')
        r.fieldcell('totale_iva')
        r.fieldcell('totale_fattura')

    def th_struct_bis(self,struct):
        "Vista alternativa"
        r = struct.view().rows()
        r.fieldcell('protocollo')
        r.fieldcell('cliente_id',zoom=True)
        r.fieldcell('data')

    def th_order(self):
        return 'protocollo'

    def th_query(self):
        return dict(column='protocollo', op='contains', val='')

class ViewFromCliente(BaseComponent):
    css_requires='fatturazione'
    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('protocollo')
        r.fieldcell('data')
        r.fieldcell('totale_imponibile')
        r.fieldcell('totale_iva')
        r.fieldcell('totale_fattura')

    def th_struct_misuraimponibile(self,struct):
        "Misura imponibile"
        r = struct.view().rows()
        r.fieldcell('totale_imponibile',cellClassCB="""
                if(v>100000){
                    return 'importo_elevato';
                }else if(v<10000){
                    return 'importo_basso'
                }
            """)
        r.fieldcell('totale_iva')
        r.fieldcell('totale_fattura')

    def th_order(self):
        return 'protocollo'

    def th_bottom_custom(self,bottom):
        bottom.slotBar('*,sum@totale_imponibile,5,sum@totale_iva,5,sum@totale_fattura,5',
            border_top='1px solid silver',height='23px')

class Form(BaseComponent):

    def th_form(self, form):
        bc = form.center.borderContainer()
        self.fatturaTestata(bc.borderContainer(region='top',datapath='.record',height='150px'))
        self.fatturaRighe(bc.contentPane(region='center'))

    def fatturaTestata(self,bc):
        left = bc.roundedGroup(title='Dati fattura',region='left',width='50%')
        fb = left.formbuilder(cols=1, border_spacing='4px',lbl_color='^gnr.user_preference.fatt.colore_testo')
        fb.field('protocollo')
        fb.field('data')
        fb.field('totale_imponibile',readOnly=True)
        fb.field('totale_iva',readOnly=True)
        fb.field('totale_fattura',readOnly=True)
        bc.contentPane(region='center').linkerBox('cliente_id',margin='2px',openIfEmpty=True,
                                                    columns='$ragione_sociale,$provincia,@cliente_tipo_codice.descrizione',
                                                    auxColumns='@comune_id.denominazione,$provincia',
                                                    newRecordOnly=True,formResource='Form',
                                                    dialog_height='500px',dialog_width='800px')

    def fatturaRighe(self,pane):
        pane.inlineTableHandler(relation='@righe',viewResource='ViewFromFattura',picker='prodotto_id')



    def th_options(self):
        return dict(dialog_height='500px', dialog_width='700px')
