#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('prodotto_id')
        r.fieldcell('cliente_tipo_id')
        r.fieldcell('prezzo_personalizzato', name='Prezzo')
        r.fieldcell('data_inizio')
        r.fieldcell('data_fine')

    def th_order(self):
        return 'prodotto_id'

    def th_query(self):
        return dict(column='prodotto_id', op='contains', val='')
    
    
class ViewFromProdotto(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('cliente_tipo_codice', edit=dict(tag='dbSelect', 
                            table='fatt.cliente_tipo', hasDownArrow=True))
        r.fieldcell('prezzo_personalizzato', edit=True)
        r.fieldcell('data_inizio', edit=True)
        r.fieldcell('data_fine', edit=True)


class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('prodotto_id')
        fb.field('cliente_tipo_id')
        fb.field('prezzo_personalizzato')
        fb.field('data_inizio')
        fb.field('data_fine')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
