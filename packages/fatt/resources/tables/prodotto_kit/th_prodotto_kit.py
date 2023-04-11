#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('codice')
        r.fieldcell('descrizione')
        r.fieldcell('prodotto_tipo_id')
        r.fieldcell('prezzo_unitario')
        r.fieldcell('tipo_iva_codice')
        r.fieldcell('foto_url')
        r.fieldcell('caratteristiche')
        r.fieldcell('numero_componenti')
        r.fieldcell('distinta')

    def th_order(self):
        return 'codice'

    def th_query(self):
        return dict(column='codice', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('codice')
        fb.field('descrizione')
        fb.field('prodotto_tipo_id')
        fb.field('prezzo_unitario')
        fb.field('tipo_iva_codice')
        fb.field('foto_url')
        fb.field('caratteristiche')
        fb.field('numero_componenti')
        fb.field('distinta')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
