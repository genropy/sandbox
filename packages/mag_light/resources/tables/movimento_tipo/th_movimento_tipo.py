#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('descrizione')
        r.fieldcell('verso')
        r.fieldcell('immediato')

    def th_order(self):
        return 'descrizione'

    def th_query(self):
        return dict(column='descrizione', op='contains', val='')



class Form(BaseComponent):
    py_requires = 'gnrcomponents/dynamicform/dynamicform:DynamicForm'
    
    def th_form(self, form):
        bc = form.center.borderContainer()
        fb = bc.contentPane(region='top', height='40px', datapath='.record').formbuilder(cols=2, border_spacing='4px')
        fb.field('descrizione', validate_notnull=True)
        fb.field('verso', validate_notnull=True, hasDownArrow=True)
        if self.getPreference('campi_dinamici_magazzino', pkg='mag_light'):
            bc.contentPane(title='Campi Aggiuntivi', region='center').fieldsGrid(
                                margin='2px',rounded=6,border='1px solid silver')
        bc.contentPane(title='Prodotti', region='bottom', height='50%').inlineTableHandler(
                                relation='@movimenti', pbl_classes=True, margin='2px', viewResource='ViewFromTipoMovimento')

    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
