#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('hierarchical_descrizione')

    def th_order(self):
        return 'hierarchical_descrizione'

    def th_query(self):
        return dict(column='hierarchical_descrizione', op='contains', val='')



class Form(BaseComponent):
    py_requires = 'gnrcomponents/dynamicform/dynamicform:DynamicForm'
    def th_form(self, form):
        bc = form.center.borderContainer()
        fb = bc.contentPane(region='top',datapath='.record').formbuilder(cols=2, border_spacing='4px')
        fb.field('descrizione',validate_notnull=True)
        tc = bc.tabContainer(region='center')
        th = tc.contentPane(title='Prodotti').plainTableHandler(relation='@prodotti',pbl_classes=True,
                                                                margin='2px')
        form.htree.relatedTableHandler(th,dropOnRoot=False,inherited=True)

        if self.getPreference('campi_dinamici_magazzino',pkg='fatt'):
            tc.contentPane(title='Campi').fieldsGrid(margin='2px',rounded=6,border='1px solid silver')
        tpl_frame = tc.framePane(title='Template prodotto')
        bar = tpl_frame.top.slotBar('2,prod_picker,*', height='20px')
        bar.prod_picker.formbuilder().dbSelect('^#FORM.prodotto_esempio_id', 
                                                table='fatt.prodotto', lbl='Prodotto',
                                                condition='$prodotto_tipo_id=:tipo_id', 
                                                condition_tipo_id='=#FORM.record.id')
        bar.dataRecord('#FORM.prodotto_esempio',table='fatt.prodotto',pkey='^#FORM.prodotto_esempio_id',
                        _if='pkey',_else='return new gnr.GnrBag({prodotto_tipo_id:prodotto_tipo_id,id:"*sample*"})',
                        prodotto_tipo_id='^#FORM.record.id')
        tpl_frame.center.contentPane(datapath='.record').templateChunk(template='^.template_bag',
                                       editable=True,
                                       table='fatt.prodotto',
                                       datasource='=#FORM.prodotto_esempio',
                                       record_id='^#FORM.prodotto_esempio.id',
                                       selfsubscribe_onChunkEdit='this.form.save();'
                                       )

    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px',hierarchical=True)
