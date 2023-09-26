#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method
from decimal import Decimal

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('prodotto_id', width='30em')
        r.fieldcell('deposito_codice', width='20em')
        r.fieldcell('quantita_disponibile', width='10em')
        r.fieldcell('giacenza_attesa', width='10em')

    def th_order(self):
        return 'prodotto_id'

    def th_query(self):
        return dict(column='prodotto_id', op='contains', val='')

    def th_options(self):
        return dict(partitioned=True, virtualStore=False, addrow=False, delrow=False)

    def th_top_custom(self,top):
        bar = top.bar
        bar.replaceSlots('viewlocker','ricalcolo,5')
        bar.ricalcolo.button("Ricalcola",fire='calcola')
        bar.dataRpc(None,self.calcolaTotali, _fired='^calcola', _lockScreen=True) 

    @public_method
    def calcolaTotali(self,**kwargs):
        self.db.table('mag_light.giacenza_prodotto_deposito').totalize_realign_sql(empty=True)

class Form(BaseComponent):

    def th_form(self, form):
        bc = form.center.contentPane(region='center', datapath='.record')
        fb = bc.formbuilder(cols=3, border_spacing='4px',colswidth='auto')
        fb.field('prodotto_id')
        fb.field('deposito_codice')
        fb.field('quantita_disponibile')
        fb.field('quantita_attesa')

    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')