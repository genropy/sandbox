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
        r.fieldcell('prezzo_totale')
        r.fieldcell('iva')



class ViewFromFattura(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('_row_count',counter=True,hidden=True)
        r.fieldcell('prodotto_id',edit=dict(validate_notnull=True))
        r.fieldcell('codice_lotto',edit=dict(table='fatt.lotto', tag='dbSelect',
                                condition='$prodotto_id=:prd_id', condition_prd_id='=#ROW.prodotto_id',
                                hasDownArrow=True, alternatePkey='codice_lotto'), width='8em')
        r.fieldcell('quantita',edit=dict(validate_notnull=True),width='7em')
        r.fieldcell('prezzo_unitario')
        r.fieldcell('aliquota_iva')
        r.fieldcell('prezzo_totale',totalize='.totale_lordo',formula='quantita*prezzo_unitario')
        r.fieldcell('iva',totalize='.totale_iva',formula='aliquota_iva*prezzo_totale/100')

    def th_view(self,view):
        view.grid.attributes.update(selfDragRows=True)
        


   # @public_method
   # def th_remoteRowController(self,row=None,field=None,**kwargs):
   #     field = field or 'prodotto_id' #nel caso di inserimento batch il prodotto viene considerato campo primario
   #     if not row['prodotto_id']:
   #         return row
   #     if not row['quantita']:
   #         row['quantita'] = 1
   #     row['prezzo_totale'] = decimalRound(row['quantita'] * row['prezzo_unitario'])
   #     row['iva'] = decimalRound(old_div(row['aliquota_iva'] * row['prezzo_totale'],100))
   #     return row

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
        fb.field('prezzo_totale')
        fb.field('iva')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
