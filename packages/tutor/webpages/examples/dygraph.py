# -*- coding: utf-8 -*-

# palette_manager.py
# Created by Francesco Porcari on 2010-12-27.
# Copyright (c) 2010 Softwell. All rights reserved.
 
"""Test Protovis"""

   
from gnr.core.gnrbag import Bag
from random import randint
from gnr.core.gnrdecorator import public_method
from datetime import datetime
from dateutil import rrule
from collections import OrderedDict
import json


class GnrCustomWebPage(object):
    py_requires="gnrcomponents/testhandler:TestHandlerFull"
    def test_0_optionsReference(self, pane):
        frame = pane.bagGrid(storepath='.store',
                        slots='2,vtitle,*,searchOn,5',
                        title='Options',
                        datapath='.reference',
                        struct=self.refstruct,
                        addrow=False,delrow=False,
                        height='300px')

        frame.data('.store',self.dygraphOptions())


    def refstruct(self,struct):
        r = struct.view().rows()
        r.cell('option',name='Option name',width='13em')
        r.cell('type',name='Type',width='5em')
        r.cell('labels',name='Labels',width='10em')
        r.cell('description',name='Labels',width='30em')


    def test_1_simple(self, pane):
        pane.dygraph(data=[
                [1,10,100],
                [2,20,80],
                [3,50,60],
                [4,70,80]
              ],options={'labels': [ "x", "A", "B" ]},
              height='300px',width='600px',border='1px solid silver')

    def datastruct(self,struct):
        r = struct.view().rows()
        r.cell('c_0',name='Prog',dtype='L')
        r.cell('c_1',name='Foo',dtype='L')
        r.cell('c_2',name='Bar',dtype='L')


    def datastruct_dt(self,struct):
        r = struct.view().rows()
        r.cell('c_0',name='TS',dtype='DH',width='10em')
        r.cell('c_1',name='Foo',dtype='L')
        r.cell('c_2',name='Bar',dtype='L')

    def test_2_bagData(self, pane):
        pane.data('.data',self.getTestData(n=10,series=[(1,100),(1,100)]))
        pane.data('.options.labels',['x','Foo','Bar'])
        bc = pane.borderContainer(height='600px',width='800px',_anchor=True)
        bc.contentPane(region='left',width='300px').frameGrid(storepath='#ANCHOR.data',
                                                            struct=self.datastruct,
                                                            datapath='.prevgrid')
        bc.contentPane(region='center').dygraph(data='^.data',options='^.options',
                    columns='c_0,c_1,c_2',
                    height='300px',width='450px',border='1px solid silver')


    def test_3_bagData(self, pane):
        pane.data('.data',self.getTestData(dtstart=datetime.now(),interval=15,count=50,
                                            series=[(1,100),(1,100)]))
        pane.data('.options.labels',['x','Foo','Bar'])
        pane.data('.options.hideOverlayOnMouseOut',False)
        pane.data('.columns','c_0,c_1,c_2')
        bc = pane.borderContainer(height='600px',width='800px',_anchor=True)
        bc.contentPane(region='left',width='300px',splitter=True).quickGrid(value='^.data')
        bc.contentPane(region='center').dygraph(data='^.data',options='^.options',
                    columns='^.columns',
                     height='300px',width='450px',nodeId='zzz',_fired='^new')
        pane_center = bc.contentPane(region='bottom')
        pane_center.button('Change dataset', action='FIRE .change',
                  fld_width='100%', width='150px', height='40px')
        pane.dataRpc('.data', self.change_dataset, _fired='^.change',
                    _onResult="""
                    PUT .options.labels = ['x','Foo','ZZZ','Spam']
                    SET .columns = 'c_0,c_1,c_2,c_3'
                    """)
        

    @public_method
    def change_dataset(self):
        return self.getTestData(dtstart=datetime.now(),interval=15,count=50,
                                            series=[(1,100),(1,100),(1,100)])
    
    def test_4_bagDataValue(self, pane):
        pane.data('.data',self.getTestData(n=10,series=[(1,100),(1,100)],datamode='value'))
        pane.data('.options.labels',['x','Foo','Bar'])
        pane.dataFormula('.options.labels',"z",z=['x','PIPPo','Pluto'],_fired='^.change_labels')
        bc = pane.borderContainer(height='600px',width='800px',_anchor=True)
        bc.contentPane(region='top').button('Change labels',fire='.change_labels')
        tc = bc.tabContainer(region='left',width='300px',splitter=True)
        grid = tc.contentPane(title='Data').quickGrid(value='^.data')
        grid.tools('delrow,addrow')
        grid.column('c_0',edit=True,name='N',dtype='L')
        grid.column('c_1',edit=True,name='Foo',dtype='L')
        grid.column('c_2',edit=True,name='Bar',dtype='L')
        bc.contentPane(region='center').dygraph(data='^.data',options='^.options',
                    columns='c_0,c_1,c_2',border='1px solid silver',position='absolute',
                    top='10px',left='10px',right='10px',bottom='10px',
                    detachable=True)
        #grid = tc.contentPane(title='Labels').multiValueEditor(value='^.options.labels')
        tc.contentPane(title='Options').multiValueEditor(value='^.options',nodeId='optionseditor')
        

    @public_method
    def getTestData(self,n=None,count=None,interval=None,dtstart=None,series=None,datamode=None):
        result = Bag()
        if n:
            g = range(1,n)
        else:
            g = rrule.rrule(rrule.MINUTELY,count=count,interval=interval,dtstart=dtstart)
        j = 0
        for i in g:
            attr = OrderedDict(c_0=i)
            for k,s in enumerate(series):
                attr['c_%s' %(k+1)] = randint(*s)
            if datamode=='value':
                result.setItem('r_%s' %j,Bag(attr))
            else:
                result.setItem('r_%s' %j,None,attr)
            j+=1
        return result


    def dygraphOptions(self):
        result = Bag()
        with open(self.site.getStaticPath('rsrc:js_libs/dygraph-options-api.json'),'r') as f:
            data = json.loads(f.read())
        for k,v in data.items():
            r = Bag(v)
            r['option'] = k
            result[k] = r
        return result
