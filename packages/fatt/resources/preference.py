
# # -*- coding: UTF-8 -*-
#--------------------------------------------------------------------------
# Copyright (c) : 2004 - 2007 Softwell sas - Milano 
# Written by    : Giovanni Porcari, Michele Bertoldi
#                 Saverio Porcari, Francesco Porcari , Francesco Cavazzana
#--------------------------------------------------------------------------
#This library is free software; you can redistribute it and/or
#modify it under the terms of the GNU Lesser General Public
#License as published by the Free Software Foundation; either
#version 2.1 of the License, or (at your option) any later version.

#This library is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#Lesser General Public License for more details.

#You should have received a copy of the GNU Lesser General Public
#License along with this library; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

class AppPref(object):
    
    def permission_fatt(self,**kwargs):
        return 'admin'

    def prefpane_fatt(self,parent,**kwargs): 
        tc = parent.tabContainer(margin='2px',**kwargs)
        self.fatt_generali(tc.contentPane(title='!![it]Generali', datapath='.generali'))
        self.fatt_magazzino(tc.contentPane(title='!![it]Magazzino', datapath='.magazzino'))
        self.fatt_dati(tc.contentPane(title='!![it]Dati',datapath='.dati'))

    def fatt_generali(self, pane):
        bc = pane.borderContainer(region='center', margin='10px')
        fb = bc.contentPane(region='top', height='80px').formbuilder(cols=1,border_spacing='3px')
        fb.span(lbl='Impostazioni importi fattura', lbl_font_weight='bold', lbl_color='#333')
        fb.numbertextbox('^.min_importo', lbl='Min. importo fatt.', width='5em')
        fb.numbertextbox('^.max_sconto', lbl='Max. sconto', width='5em')
        spese_sped = bc.contentPane(region='center').quickGrid(value='^.spese_spedizione',border='1px solid silver',margin='2px')
        spese_sped.tools('addrow,delrow',title='Impostazioni costi spedizione')
        spese_sped.column('peso_min',width='10em',name='Peso min.',edit=True)
        spese_sped.column('peso_max',width='10em',name='Peso max.',edit=True)
        spese_sped.column('costo', width='10em', dtype='money', name='Costo', edit=True)
        
    def fatt_magazzino(self, pane):
        fb = pane.formbuilder(cols=1,border_spacing='3px', margin='10px')
        fb.checkbox(value='^.campi_dinamici_magazzino',label='Campi dinamici magazzino')

    def fatt_dati(self, pane):
        fb = pane.formbuilder(cols=1,border_spacing='3px', margin='10px')
        fb.div('Press button to load default data')
        fb.button('Load data',action="""genro.mainGenroWindow.genro.publish('open_batch');
                                        genro.serverCall('_package.fatt.loadStartupData',null,function(){});
                                        """,_tags='_DEV_')