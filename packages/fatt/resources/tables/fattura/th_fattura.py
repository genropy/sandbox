#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('protocollo')
        r.fieldcell('cliente_id',zoom=True)
        r.fieldcell('@cliente_id.provincia')
        r.fieldcell('data')
        r.fieldcell('totale_imponibile',
                    range_basso='value<1000',
                    range_basso_color='blue',
                    range_alto='value>10000',
                    range_alto_color='red')
        r.fieldcell('totale_iva')
        r.fieldcell('totale_fattura')
        r.cell('tpl',rowTemplate="""<div>Imponibile:$totale_imponibile</div>
                                    <div>Iva:$totale_iva</div>
                                    """,width='12em')

    def th_page_stat(self,pane):
        "Statistica"
        # pane.div('aaa')
        pane.tableHandlerStats(table='fatt.fattura')

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
        center = bc.tabContainer(region='center')
        self.fatturaRighe(center.contentPane(title='Righe'))
        center.contentPane(title='Allegati')
        center.contentPane(title='Note')

    def fatturaTestata(self,bc):
        
        bc.contentPane(region='center').linkerBox('cliente_id',margin='2px',openIfEmpty=True,
                                                    validate_notnull=True,
                                                    columns='$ragione_sociale,$provincia,@cliente_tipo_codice.descrizione',
                                                    auxColumns='@comune_id.denominazione,$provincia',
                                                    newRecordOnly=True,formResource='Form',
                                                    dialog_height='500px',dialog_width='800px')
        left = bc.roundedGroup(title='Dati fattura',region='left',width='50%')
        fb = left.formbuilder(cols=1, border_spacing='4px')
        fb.field('protocollo',readOnly=True)
        fb.field('data')
        
    def fatturaRighe(self,pane):
        pane.inlineTableHandler(relation='@righe',viewResource='ViewFromFattura',
                            picker='prodotto_id',
                            picker_structure_field='prodotto_tipo_id')

    def th_options(self):
        return dict(dialog_height='500px', dialog_width='700px')
