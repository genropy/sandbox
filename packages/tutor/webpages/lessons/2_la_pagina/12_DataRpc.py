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
        box=pane.div(width='300px',margintop='3p')
        box.dataRpc('.data', self.getCpuTimes, _timing=10)
        #box.div('^.table',width='100%')
       #box.dataController("""console.log('cores',cores);
       #var table= cores.asHtmlTable({cells:'core,user,nice,system,idle',headers:true});
       #SET .table=table""",
       #                   cores='^.cores')
       #
        tbl=box.div(width='100%')
        box.dataController("""var rows=data.getItem('rows');
                              var columns=data.getItem('columns');
                              genro.dom.scrollableTable(tbl.domNode,rows, 
                              {columns:columns,
                               tblclass:'formattedBagTable',
                               max_height:'90px'});""",
                              data='^.data',
                              tbl=tbl)
        
        
    @public_method
    def getCpuTimes(self):
        result=Bag()
        columns='core,user,nice,system,idle'.split(',')
        result['columns']=columns
        rows=Bag()
        result['rows']=rows
        for k, core in enumerate(psutil.cpu_times(True)):
            row=dict([(c,getattr(core,c)) for c in columns[1:]])
            row['core']=k+1
            rows.setItem('r_%i'%k,None,row)
        return result
                
                
    
    
        
        
        


        
   
