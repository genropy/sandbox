
# # -*- coding: UTF-8 -*-
#--------------------------------------------------------------------------
# Copyright (c) : 2021 Softwell srl - Milano 
# Written by    : Davide Paci
#--------------------------------------------------------------------------

class AppPref(object):
    def permission_mag_light(self,**kwargs):
        return 'admin'

    def prefpane_mag_light(self,parent,**kwargs): 
        pane = parent.contentPane(**kwargs)
        fb = pane.formbuilder(cols=1,border_spacing='3px', margin='10px')
        fb.checkbox(value='^.campi_dinamici_magazzino',label='Campi dinamici magazzino')