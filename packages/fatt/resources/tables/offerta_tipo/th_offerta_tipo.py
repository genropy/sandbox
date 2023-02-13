#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('codice')
        r.fieldcell('descrizione')
        r.fieldcell('codice_contatore')

    def th_order(self):
        return 'codice'

    def th_query(self):
        return dict(column='codice', op='contains', val='')



class Form(BaseComponent):

    py_requires ='gnrcomponents/master_detail/master_detail:MasterDetail AS mdconf'

    def th_form(self, form):
        bc = form.center.borderContainer()
        fb = bc.contentPane(region='top',datapath='.record').formbuilder(cols=3, border_spacing='4px')
        fb.field('codice',validate_notnull=True,width='5em')
        fb.field('descrizione',validate_notnull=True)
        fb.field('codice_contatore',width='5em')
        self.mdconf.configurator(bc.contentPane(region='center',margin='2px'),gridField='conf_grid',
                            printField='conf_print',
                            gridTable='fatt.offerta_riga',
                            gridResource='th_offerta_riga:ViewFromOfferta',
                            title='Personalizzazione righe offerta',margin='2px')



    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
