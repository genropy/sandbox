
# -*- coding: UTF-8 -*-

"""ClientPage tester"""
from gnr.core.gnrbag import Bag,NetBag
from gnr.core.gnrdecorator import public_method


class GnrCustomWebPage(object):
    py_requires = "gnrcomponents/testhandler:TestHandlerFull"
    
    def test_1_clientrpc(self, pane):
        fb = pane.formbuilder(cols=1,border_spacing='3px')
        fb.textbox(value='^.cliente',lbl='Cliente')
        fb.button('Run',fire='.run')
        fb.dataRpc('.result',self.testRpcNetBag,cliente='^.cliente',_fired='^.run')
        pane.tree(storepath='.result')

    @public_method
    def testRpcNetBag(self,cliente=None):
        return  NetBag('http://external:3xt3rn4l@localhost:8081/fatt/test_netbag','lista_fatture',
                                            cliente=cliente)


    def test_2_selection(self, pane):
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
        frame.dataRpc('.result',self.netBagSelection,data='=.data',_fired='^.run')


    @public_method
    def netBagSelection(self,data=None,**kwargs):
        return  NetBag('http://external:3xt3rn4l@localhost:8081/fatt/test_netbag','selection',**data.asDict(ascii=True))



    def test_3_record(self, pane):
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
        frame.dataRpc('.result',self.netBagRecord,data='=.data',_fired='^.run')


    @public_method
    def netBagRecord(self,data=None,**kwargs):
        return  NetBag('http://external:3xt3rn4l@localhost:8081/fatt/test_netbag','record',**data.asDict(ascii=True))

