# -*- coding: UTF-8 -*-
from gnr.core.gnrdecorator import websocket_method, public_method

class GnrCustomWebPage(object):

    def main(self,root,**kwargs):
        bc = root.borderContainer(height='100%')
        top = bc.contentPane(region='top', height='150px')
        fb = top.formBuilder(cols=4)
        #### WEBSOCKET
        fb.button(label='WebSocket', action="""FIRE websocket_test_bt """)
        fb.dataController("""SET result.time=new Date();
            ; FIRE websocket_test """,_fired='^websocket_test_bt', _timing=1)
        fb.div('^result.websocket_result')
        fb.div('^result.diff_ws')
        fb.dataWs('result.websocket_result', self.test_ws, _fired='^websocket_test')
        fb.dataController(""" var now = new Date();
                SET result.diff_ws = now-last_set;""", last_set = '=result.time',_fired='^result.websocket_result')
        

        #### RPC
        fb.button(label='RPC', action="""FIRE rpc_test_bt """)
        fb.dataController("""SET result.time=new Date();
            ; FIRE rpc_test """,_fired='^rpc_test_bt', _timing=1)
        fb.dataRpc('result.rpc_result', self.test_rpc, _fired='^rpc_test')
        fb.div('^result.rpc_result')
        fb.div('^result.diff_rpc')
        fb.dataController(""" var now = new Date();
                SET result.diff_rpc = now-last_set;""", last_set = '=result.time',_fired='^result.rpc_result')
        
    @websocket_method
    def test_ws(self):
        return 'test ok'


    @public_method
    def test_rpc(self):
        return 'test ok'
