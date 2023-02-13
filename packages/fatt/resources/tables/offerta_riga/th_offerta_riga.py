#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('_row_count')
        r.fieldcell('offerta_id')
        r.fieldcell('prodotto_id')
        r.fieldcell('descrizione')
        r.fieldcell('quantita')
        r.fieldcell('prezzo_unitario')
        r.fieldcell('sconto')
        r.fieldcell('importo_lordo')
        r.fieldcell('importo_netto')
        r.fieldcell('aliquota_iva')
        r.fieldcell('riga_descrizione')

    def th_order(self):
        return '_row_count'

    def th_query(self):
        return dict(column='_row_count', op='contains', val='')

class ViewFromOfferta(BaseComponent):
    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('prodotto_id', name='!![it]Prodotto', width='15em',caption_field='prodotto_descrizione',
                    edit=dict(validate_notnull=True,remoteRowController=True))
        r.fieldcell('descrizione',name='Descrizione',edit=dict(tag='simpleTextArea'),width='30em',print_mm_width=0)
        r.fieldcell('quantita',name='Q.',edit=dict(remoteRowController=True),
                #editDisabled='=#ROW.riga_reale?=!#v',
                print_mm_width=15)
        r.fieldcell('prezzo_unitario',print_mm_width=20)
        r.fieldcell('importo_lordo',print_mm_width=20)
        r.fieldcell('sconto',name='Sconto',edit=dict(remoteRowController=True),
                    width='6em',print_mm_width=20)
        r.fieldcell('importo_netto', name='Netto',print_mm_width=20,width='7em')
        r.fieldcell('aliquota_iva',name='Alq',width='5em')
        r.fieldcell('_row_count',hidden=True,counter=True)
        r.fieldcell('prodotto_codice',hidden=True)
        r.fieldcell('prodotto_descrizione',hidden=True)

class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('_row_count')
        fb.field('offerta_id')
        fb.field('prodotto_id')
        fb.field('descrizione')
        fb.field('quantita')
        fb.field('prezzo_unitario')
        fb.field('sconto')
        fb.field('importo_lordo')
        fb.field('importo_netto')
        fb.field('aliquota_iva')
        fb.field('riga_descrizione')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
