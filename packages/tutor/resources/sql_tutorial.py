#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method
from gnr.core.gnrbag import Bag

class PrintTutorial(BaseComponent):
    py_requires = 'gnrcomponents/source_viewer/source_viewer'
    source_viewer_rebuild = False

    def main(self,root,**kwargs):
        root.attributes['overflow'] = 'hidden'
        frame = root.framePane('sqltutorial',datapath='main')
        bar = frame.top.slotToolbar('10,stackButtons,10,reloader,*')
        bar.reloader.slotButton('Run',action="FIRE .runGetData;",iconClass='iconbox run')
        sc = frame.center.stackContainer(datapath='main')
        if hasattr(self,'getRecord'):
            self.recordPane(sc)
        else:
            self.selectionPane(sc)
        self.sqlPane(sc)

    def recordPane(self,sc):
        sc.contentPane(title='!!Record').div(padding='10px').tree(storepath='.result')
        sc.dataRpc('.result',self.getRecordData,subscribe_rebuildPage=True,_fired='^.runGetData',_onStart=True)

    def selectionPane(self,sc):
        sc.contentPane(title='!!Selection',overflow='hidden').quickGrid(value='^.result')
        sc.dataRpc('.result',self.getSelectionData,subscribe_rebuildPage=True,_fired='^.runGetData',
                    _onStart=True)

    def sqlPane(self,sc):
        sc.contentPane(title='Sql').codemirror(value='^.sql',
                                config_mode='sql',config_lineNumbers=True,
                                config_indentUnit=4,config_keyMap='softTab',
                                height='100%',config_autoFocus=True,
                                readOnly=True,nodeId='sqlviewer')

    @public_method
    def getSelectionData(self,**kwargs):
        q = self.getQuery()
        result = Bag()
        if not q:
            return result
        f = q.fetch()
        self.setInClientData('main.sql', q.sqltext)
        for i,r in enumerate(f):
            r = Bag(r)
            k = r.pop('pkey',None) or 'r_%i' %i
            result[k] = r
        return result

    @public_method
    def getRecordData(self,**kwargs):
        r = self.getRecord()
        if r:
            self.setInClientData('main.sql',r.sqltext)
            return r.output('bag')
        return Bag()




