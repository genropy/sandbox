    
# -*- coding: UTF-8 -*-
"""ClientPage tester"""
from gnr.core.gnrbag import Bag,NetBag
from gnr.core.gnrdecorator import public_method


class GnrCustomWebPage(object):
    py_requires = "gnrcomponents/testhandler:TestHandlerFull"

    def test_3_selection(self, pane):
        frame = pane.framePane(height='400px')
        frame.top.slotToolbar('*,run,10').run.slotButton('Run',action='FIRE .run;')
        bc = frame.center.borderContainer()
        top = bc.contentPane(region='top',height='150px',splitter=True)
        data = Bag()
        data['table'] = 'fatt.cliente'
        data['where'] = ''
        data['limit'] = 10
        top.data('.data',data)
        top.multiValueEditor(value='^.data')
        center = bc.contentPane(region='center')
        center.quickGrid('^.result')
        frame.dataRpc('.result',self.netBagTestCaller,data='=.data',methodname='selection',_fired='^.run')

    def test_4_record(self, pane):
        frame = pane.framePane(height='400px')
        frame.top.slotToolbar('*,run,10').run.slotButton('Run',action='FIRE .run;')
        bc = frame.center.borderContainer()
        top = bc.contentPane(region='top',height='150px',splitter=True)
        data = Bag()
        data['table'] = 'fatt.cliente'
        data.setItem('pkey', '')
        top.data('.data',data)
        top.multiValueEditor(value='^.data')
        center = bc.contentPane(region='center')
        center.tree(storepath='.result')
        frame.dataRpc('.result',self.netBagTestCaller,data='=.data',methodname='record',_fired='^.run')


    @public_method
    def netBagTestCaller(self,data=None,methodname=None,**kwargs):
        return  NetBag('http://external:3xt3rn4l@localhost:8081/fatt/test_netbag',methodname,**data.asDict(ascii=True))
