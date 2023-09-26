#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('deposito_codice', width='10em')
        r.fieldcell('prodotto_id')
        r.fieldcell('quantita_riga')

    def th_order(self):
        return 'prodotto_id'

    def th_query(self):
        return dict(column='prodotto_id', op='contains', val='')

    def th_options(self):
        return dict(partitioned=True)
class ViewFromProdotto(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('@movimento_id.data')
        r.fieldcell('@movimento_id.protocollo')
        r.fieldcell('@movimento_id.@movimento_tipo.descrizione')
        r.fieldcell('deposito_codice')
        r.fieldcell('quantita_riga')
        r.fieldcell('@movimento_id.note')

    def th_order(self):
        return 'data:d'

class ViewFromMovimento(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('prodotto_id')
        r.fieldcell('quantita_riga')
        r.fieldcell('@prodotto_id.giacenza_curr_dep', lbl='Giacenza attuale')

    def th_query(self):
        return dict(column='prodotto_id', op='contains', val='')

    def th_options(self):
        return dict(partitioned=True)

class Form(BaseComponent):

    def th_form(self, form):
        bc = form.center.borderContainer(datapath='.record')
        pdt = bc.contentPane(region='top', height='100px').linkerBox('prodotto_id', margin='2px', 
                                    columns='$codice,$descrizione',
                                    auxColumns='$codice,$descrizione,$giacenza_curr_dep',
                                    formResource='FormFromMovimentoRiga',
                                    dialog_height='300px', dialog_width='500px')
        fb = bc.contentPane(region='center').formbuilder(cols=1, border_spacing='4px')
        fb.field('quantita', hidden='^#FORM.record.@movimento_id.in_attesa')
        fb.field('quantita_attesa', hidden='^#FORM.record.@movimento_id.in_attesa?=!#v')

    def th_options(self):
        return dict(dialog_height='200px', dialog_width='300px', modal=True)
