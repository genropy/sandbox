# -*- coding: UTF-8 -*-

# palette_manager.py
# Created by Francesco Porcari on 2010-12-27.
# Copyright (c) 2010 Softwell. All rights reserved.
 
"""Dygraph gallery"""
   
from gnr.core.gnrbag import Bag
from random import randint
from dateutil import rrule
from collections import OrderedDict
    

class GnrCustomWebPage(object):
    def source_viewer_open(self):
        return False
        
    def main(self,root,**kwargs):
        frame = root.framePane(height='600px',width='800px',datapath='main')
        bar = frame.top.slotToolbar('5,instruction,*,dynamicData,5,zoomSlider,5',height='20px')
        bar.instruction.div('To detach a graph drag its title pressing Shift key',
                            color='RGBA(99, 136, 195, 0.8)',font_size='16px')
        bar.dynamicData.checkbox(value='^.dynamicData',label='Dynamic data')
        bar.data('.zoom',.4)
        bar.dataController("""
            graph_data.forEach(function(cn){
                    var dygraphData = cn._value.getItem('data');
                    var nodes = dygraphData.getNodes();
                    var lastIndex = nodes[nodes.length-1].getValue().getItem('c_0');
                    var row = new gnr.GnrBag();
                    row.setItem('c_0',lastIndex+1)
                    row.setItem('c_1',Math.floor(Math.random() * 99 + 1))
                    row.setItem('c_2',Math.floor(Math.random() * 99 + 1))
                    dygraphData.popNode('#0',false)
                    dygraphData.setItem('r_'+lastIndex,row);
                });

            """,graph_data='=.graph_data',_timing=1,
                        _if='_dynamicData',
                        _dynamicData='=.dynamicData')
        bar.zoomSlider.horizontalSlider(value='^.zoom',minimum=0.25,maximum=.5,
                                        intermediateChanges=True,width='15em')

        t = frame.center.contentPane(margin='10px').table(zoom='^.zoom',border_spacing='5px').tbody(datapath='.graph_data')
        for r in range(4):
            row = t.tr()
            for c in range(4):
                title='Graph %s %s' %(r,c)
                cell = row.td(datapath='.graph_%s_%s' %(r,c))
                cell.data('.data',self.getTestData(n=randint(10,50),series=[(1,100),(1,100)],datamode='value'))
                cell.data('.options.labels',['x','Foo','Bar'])
                cell.div(height='400px',width='600px',position='relative').dygraph(data='^.data',options='^.options',border='1px solid silver',
                    columns='c_0,c_1,c_2',
                    title=title,
                    position='absolute',top='0px',left='0px',right='0px',bottom='0px',detachable=True)


    def getTestData(self,n=None,count=None,interval=None,dtstart=None,series=None,datamode=None):
        result = Bag()
        if n:
            g = xrange(1,n)
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
