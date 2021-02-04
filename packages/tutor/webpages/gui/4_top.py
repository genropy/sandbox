# -*- coding: UTF-8 -*-

import psutil
import datetime
import re

from gnr.core.gnrdecorator import public_method
from gnr.core.gnrbag import Bag

class GnrCustomWebPage(object):
    
    def main(self,root,**kwargs):
        properties=['pid','ppid','name','username','status','create_time',
                    'cpu_percent','memory_percent','cwd','nice','uids',
                    'gids','cpu_times','memory_info','exe']
        pane =root.div(margin='15px',datapath='processList')
        fb=pane.formbuilder(cols=1)
        fb.numberTextBox(value='^.treshold',lbl='Treshold',width='5em',default=.5)
        fb.checkBoxText('^.columns',values=','.join(properties),colspan=2,
                        default='pid,name,username,cpu_percent',
                        cols=4,width='100%',lbl='Columns')
        pane.dataRpc('.data', self.getProcessesBag, columns='^.columns',
                        treshold='^.treshold',_timing=2,
                        _onStart=True)
        pane.quickGrid(value='^.data',height='200px',width='100%',
                         sortedBy='cpu_percent:d',border='1px solid silver')
        
    @public_method
    def getProcessesBag(self,columns=None,treshold=None):
        columns=(columns or 'pid,name').split(',')
        result = Bag()
        for p in psutil.process_iter():
            d=p.as_dict()
            d['cpu_percent'] = d['cpu_percent'] or 0. 
            d['memory_percent'] = d['memory_percent'] or 0.
            if d['cpu_percent']>(treshold or 0):
                d['create_time'] = datetime.datetime.fromtimestamp(d['create_time'])
                row = Bag([(k,d[k]) for k in columns if k in d])
                result.setItem('p_%s'%p.pid,row)
        return result