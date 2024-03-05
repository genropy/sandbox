#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method


class View(BaseComponent):
    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('protocollo',width='10em')
        r.fieldcell('data',width='7em')
        r.fieldcell('cliente_id',zoom=True,width='15em')
        r.fieldcell('totale_imponibile',width='7em',name='Tot.Imp')
        r.fieldcell('totale_iva',width='7em',name='Tot.Iva')
        r.fieldcell('totale_fattura',width='7em',name='Totale')

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

    def th_options(self):
        return dict(view_preview_tpl='r_fatt_riga')

class ViewFromCliente(BaseComponent):
    css_requires='fatturazione'
    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('protocollo')
        r.fieldcell('data')
        r.fieldcell('totale_imponibile')
        r.fieldcell('totale_iva')
        r.fieldcell('totale_fattura')

    def th_order(self):
        return 'protocollo'

    def th_top_custom(self,top):
        top.bar.replaceSlots('vtitle','sections@annomese',sections_annomese_remote=self.calcolaSectionAnnoMese)


    @public_method(remote_cliente_id='^#FORM.record.id')
    def calcolaSectionAnnoMese(self,cliente_id=None,**kwargs):
        if not cliente_id:
            return []
        f = self.db.table('fatt.fattura').query(where='$cliente_id=:clid',clid=cliente_id,
                        columns="to_char($data,'YYYY-MM') AS annomese",distinct=True).fetch()
        return [dict(code=f"c_{r['annomese'].replace('-','')}",
                        caption=r['annomese'],
                        condition="to_char($data,'YYYY-MM')=:am",condition_am=r['annomese'])for r in f]


class Form(BaseComponent):

    def th_form(self, form):
        bc = form.center.borderContainer()
        self.fatturaTestata(bc.borderContainer(region='top',datapath='.record',height='150px'))
        self.fatturaRighe(bc.contentPane(region='center'))

    def fatturaTestata(self,bc):
        bc.contentPane(region='center').linkerBox('cliente_id',margin='2px',openIfEmpty=True, validate_notnull=True,
                                                    columns='$ragione_sociale,$provincia,@cliente_tipo_codice.descrizione',
                                                    auxColumns='@comune_id.denominazione,$provincia',
                                                #    clientTemplate=True,
                                                    newRecordOnly=True,formResource='Form',
                                                    dialog_height='500px',dialog_width='800px')
        left = bc.roundedGroup(title='Dati fattura',region='left',width='50%')
        fb = left.formbuilder(cols=1, border_spacing='4px')
        fb.field('protocollo',readOnly=True)
        fb.field('data')
    
    def fatturaRighe(self,pane):
        pane.inlineTableHandler(relation='@righe',viewResource='ViewFromFattura',
                            picker='prodotto_id',
                            grid_remoteRowController_default=dict(
                                data_fattura='^#FORM.record.data',
                            ),
                            picker_structure_field='prodotto_tipo_id')

    def th_options(self):
        return dict(dialog_height='500px', dialog_width='700px')
