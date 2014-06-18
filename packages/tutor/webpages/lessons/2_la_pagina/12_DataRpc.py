# -*- coding: UTF-8 -*-

import datetime
import re
from gnr.core.gnrdecorator import public_method
import psutil
from gnr.core.gnrbag import Bag

class GnrCustomWebPage(object):
    
    def main(self,root,**kwargs):
        self.serverDatetime(root.div(margin='15px',datapath='serverDatetime'))
        self.cpuTimes(root.div(margin='15px',datapath='cpuTimes'))
        self.processList(root.div(margin='15px',datapath='processList'))

    def serverDatetime(self,pane):
        pane.button('Get Server Datetime',font_size='18px',
                    fire='.get_datetime')
        pane.dataRpc('.now', self.getNow, _fired='^.get_datetime')
        pane.dataController('alert(now)',now='^.now')
        
    @public_method
    def getNow(self):
        return datetime.datetime.now()
    
    
    
    def cpuTimes(self,pane):
        pane.h1('Cpu Times')
        pane.quickGrid(value='^.data', border='1px solid silver',
                              height='auto',width='auto')
        pane.dataRpc('.data', self.getCpuTimes, _timing=5,_onStart=True)
 
    @public_method
    def getCpuTimes(self):
        result=Bag()
        columns='user,nice,system,idle'.split(',')
        for j, core in enumerate(psutil.cpu_times(True)):
            row = Bag()
            row['core']=j+1
            for k in columns:
                row.setItem(k, getattr(core,k))
            result.setItem('r_%i'%j, row)
        return result
    
        
    def processList(self,pane):
        properties='pid,ppid,name,username,status,create_time,'
        properties+='cpu_percent,memory_percent,cwd,nice,uids,'
        properties+='gids,cpu_times,memory_info,exe'
        pane.h1('Processlist')
        fb=pane.formbuilder(cols=2)
        fb.textBox('^.userName',lbl='User Name')
        fb.textBox('^.processName', lbl='Process Name')
        fb.numberTextBox('^.cpuPerc', lbl='% Cpu')
        fb.numberTextBox('^.memPerc', lbl='% Memory')
        fb.checkBoxText('^.columns',values=properties,colspan=2,
                        cols=1,
                        width='100%',
                        default_value='pid,name,username',
                        lbl='Columns',popup=True)
   
        pane.dataRpc('.data', self.getProcessesBag,columns='^.columns',
                             userName='^.userName',processName='^.processName',
                             cpuPerc='^.cpuPerc',memPerc='^.memPerc',
                             _timing=5,_onStart=True)
    
        pane.quickGrid(value='^.data',height='200px',width='auto',
                                      border='1px solid silver')
        
    @public_method
    def getProcessesBag(self,columns=None, userName=None, 
                        processName=None,memPerc=None,cpuPerc=None):
        columns=(columns or 'pid,name').split(',')
        result = Bag()
        for p in psutil.process_iter():
            if userName and userName != p.username:
                continue
            if processName and not re.match(processName,p.name):
                continue
            d=p.as_dict()
            d['create_time'] = datetime.datetime.fromtimestamp(d['create_time'])
            d['cpu_percent'] = d['cpu_percent'] or 0. 
            d['memory_percent'] = d['memory_percent'] or 0.
            if memPerc and d['memory_percent'] < memPerc:
                continue
            if cpuPerc and d['cpu_percent']<cpuPerc:
                continue
            row = Bag([(k,d[k]) for k in columns if k in d])
            result.setItem('p_%s'%p.pid,row)
        return result
    
    
        
        
        


        
   
