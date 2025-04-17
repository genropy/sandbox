#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('prodotto_id')
        r.fieldcell('codice_lotto')
        r.fieldcell('descrizione')
        r.fieldcell('data_produzione')
        r.fieldcell('data_scadenza')

    def th_order(self):
        return 'prodotto_id'

    def th_query(self):
        return dict(column='prodotto_id', op='contains', val='')


class ViewFromProdotto(BaseComponent):
    
    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('codice_lotto', edit=True)
        r.fieldcell('descrizione', edit=True, width='30em')
        r.fieldcell('data_produzione', edit=True, width='6em')
        r.fieldcell('data_scadenza', edit=True, width='6em')
        
        
class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('prodotto_id')
        fb.field('codice_lotto')
        fb.field('descrizione')
        fb.field('data_produzione')
        fb.field('data_scadenza')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
