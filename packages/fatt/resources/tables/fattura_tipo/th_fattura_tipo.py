#!/usr/bin/python
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('descrizione', width='25em')
        r.fieldcell('codice_contatore', width='7em')

    def th_order(self):
        return 'descrizione'

    def th_query(self):
        return dict(column='descrizione', op='contains', val='')

    def th_options(self):
        return dict(virtualStore=False)


class Form(BaseComponent):
    py_requires ='gnrcomponents/master_detail/master_detail:MasterDetail AS mdconf'

    def th_form(self, form):
        bc = form.center.borderContainer()
        fb = bc.contentPane(region='top',datapath='.record').formbuilder(cols=2, border_spacing='4px')
        fb.field('descrizione')
        fb.field('codice_contatore')
        self.mdconf.configurator(bc.contentPane(region='center'),gridField='conf_grid',
                            printField='conf_print',
                            gridTable='fatt.fattura_riga',
                            gridResource='th_fattura_riga:ViewFromFattura',
                            title='Personalizzazione righe fattura',margin='2px')

    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
