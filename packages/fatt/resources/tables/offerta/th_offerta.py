#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('cliente_id')
        r.fieldcell('offerta_tipo')
        r.fieldcell('codice_contatore')
        r.fieldcell('protocollo')
        r.fieldcell('data_protocollo')
        r.fieldcell('_righe_documento')
        r.fieldcell('filepath')

    def th_order(self):
        return 'cliente_id'

    def th_query(self):
        return dict(column='cliente_id', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('cliente_id')
        fb.field('offerta_tipo')
        fb.field('codice_contatore')
        fb.field('protocollo')
        fb.field('data_protocollo')
        fb.field('_righe_documento')
        fb.field('filepath')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
