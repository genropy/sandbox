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
        fb = left.formbuilder(cols=1, border_spacing='4px') #,lbl_color='^gnr.user_preference.fatt.colore_testo')
        fb.field('protocollo')
        fb.field('data')
       #fb.field('totale_imponibile',readOnly=True)
       #fb.field('totale_iva',readOnly=True)
       #fb.field('totale_fattura',readOnly=True)
        bc.contentPane(region='center').linkerBox('cliente_id',margin='2px',openIfEmpty=True,
                                                    columns='$ragione_sociale,$provincia,@cliente_tipo_codice.descrizione',
                                                    auxColumns='@comune_id.denominazione,$provincia',
                                                    newRecordOnly=True,formResource='Form',
                                                    dialog_height='500px',dialog_width='800px')

    def fatturaRighe(self,pane):
        th = pane.inlineTableHandler(relation='@righe',viewResource='ViewFromFattura',
                            picker='prodotto_id',
                            picker_structure_field='prodotto_tipo_id',
                            semaphore=True)
        bar = th.view.bottom.slotBar('*,fbtot,15',height='20px',background='#EEF2F4',border_top='1px solid silver',padding='3px')
        fb = bar.fbtot.formbuilder(cols=5,border_spacing='3px',fld_format='###,###,###.00',
                fld_class='fakeTextBox fakeNumberTextBox',fld_width='7em')
        fb.div('^.grid.totale_lordo',lbl='Lordo')
        fb.numberTextBox('^#FORM.record.sconto',lbl='Sconto',format='###.000000')
        fb.numberTextBox('^#FORM.record.totale_imponibile',
                 validate_onAccept="""
                    if(userChange){
                        var totale_lordo = GET .grid.totale_lordo;
                        var sconto_calcolato = Math.round( ( (totale_lordo-value) /totale_lordo ) *100 *100 ) /100;
                        this.setRelativeData('#FORM.record.sconto',sconto_calcolato,null,null,'calcolo_sconto');
                    }
                 """,lbl='Imponibile',readOnly='^.grid.editor.status')
        
        fb.div('^.grid.totale_iva',lbl='Iva')
        fb.div('==(_iva || 0) + (_imp || 0)',_iva='^.grid.totale_iva',_imp='^.grid.totale_imponibile',
                    lbl='Totale')

        #Math.round(d.currentTime*10)/10,
        fb.dataFormula("#FORM.record.totale_imponibile","Math.round((lordo*(100-s)/100)*100)/100",
                        lordo='^.grid.totale_lordo',
                        s='^#FORM.record.sconto',_delay=1,
                        _if='_triggerpars.kw.reason!="calcolo_sconto"',_userChanges=True)
        

    def th_options(self):
        return dict(dialog_height='500px', dialog_width='700px')
