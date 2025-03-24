#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import division
from past.utils import old_div
from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method
from gnr.core.gnrnumber import decimalRound
class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('fattura_id')
        r.fieldcell('prodotto_id')
        r.fieldcell('quantita')
        r.fieldcell('prezzo_unitario')
        r.fieldcell('aliquota_iva')
        r.fieldcell('sconto')
        r.fieldcell('prezzo_totale')
        r.fieldcell('iva')

    def th_order(self):
        return 'fattura_id'

    def th_query(self):
        return dict(column='fattura_id', op='contains', val='')
        
class ViewFromProdotto(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('fattura_id')
        r.fieldcell('@fattura_id.@cliente_id.ragione_sociale',name='Cliente')
        r.fieldcell('quantita')
        r.fieldcell('prezzo_unitario')
        r.fieldcell('aliquota_iva')
        r.fieldcell('sconto')
        r.fieldcell('prezzo_totale')
        r.fieldcell('iva')

class ViewFromFattura(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('_row_count', counter=True, hidden=True)
        r.fieldcell('prodotto_id', edit=dict(remoteRowController=True, validate_notnull=True))
        r.fieldcell('quantita', edit=dict(remoteRowController=True), width='7em')
        r.fieldcell('prezzo_unitario')
        r.fieldcell('aliquota_iva')
        r.fieldcell('sconto', edit=dict(remoteRowController=True), totalize=True) 
        #Totalize può essere impostato a True o a un path specifico a scelta
        r.fieldcell('prezzo_totale', totalize='.totale_lordo')
        r.fieldcell('iva', totalize='.totale_iva')
        r.fieldcell('descrizione_prodotto',hidden=True)

        
    def th_options(self):
        return dict(grid_footer=True)


        
class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('fattura_id')
        fb.field('prodotto_id')
        fb.field('quantita')
        fb.field('prezzo_unitario')
        fb.field('aliquota_iva')
        fb.field('sconto')
        fb.field('prezzo_totale')
        fb.field('iva')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
