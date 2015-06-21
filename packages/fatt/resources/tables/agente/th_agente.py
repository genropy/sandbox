#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('cognome')
        r.fieldcell('nome')
        r.fieldcell('indirizzo')
        r.fieldcell('comune_id')
        r.fieldcell('provincia')
        r.fieldcell('cap')

    def th_order(self):
        return 'cognome'

    def th_query(self):
        return dict(column='cognome', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('cognome')
        fb.field('nome')
        fb.field('indirizzo')
        fb.field('comune_id')
        fb.field('provincia')
        fb.field('cap')
        fb.field('data_nascita')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
