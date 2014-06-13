# -*- coding: UTF-8 -*-

import datetime
from gnr.core.gnrdecorator import public_method
import psutil
from gnr.core.gnrbag import Bag

class GnrCustomWebPage(object):
    
    def main(self,root,**kwargs):
        self.serverDatetime(root.div(margin='15px',datapath='server_datetime'))
        self.cpuTimes(root.div(margin='15px',datapath='cpuTimes'))

    def serverDatetime(self,pane):
        pane.h1('Server Datetime')
        box=pane.div(width='700px',border='1px solid gray')
        fb = box.formbuilder(cols=3)
        fb.button('Update', fire='.get_datetime')
        fb.div('^.now',_class='fakeTextBox',color='#555',
               width='300px',lbl='Server Date')
        fb.dataRpc('.now', self.getNow, _fired='^.get_datetime')
    
    @public_method
    def getNow(self,k=None):
        return datetime.datetime.now()
    
    def cpuTimes(self,pane):
        pane.h1('Cpu Times')
        box=pane.div(margin='3px')
        box.dataRpc('.data', self.getCpuTimes, _timing=10,_onStart=True)
        box.quickGrid(value='^.data',height='500px',border='1px solid silver')
        
        
    @public_method
    def getCpuTimes(self):
        return self.site.getService('sysinfo').getCpuTimes()

                
                
    
    
        
        
        


        
   
