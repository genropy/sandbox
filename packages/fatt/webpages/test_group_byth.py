    
# -*- coding: UTF-8 -*-
"""ClientPage tester"""
from gnr.core.gnrdecorator import public_method


class GnrCustomWebPage(object):
    py_requires = "gnrcomponents/testhandler:TestHandlerFull,th/th:TableHandler"


    def test_querytool(self,pane):
        bc = pane.borderContainer(height='500px',width='700px')
        table = 'fatt.fattura'
       #fmenupath = 'gnr.qb.%s.fieldsmenu' %table.replace('.','_')
       #bc.dataRemote(fmenupath,self.relationExplorer,item_type='QTREE',
       #                table=table,omit='_*')
        pane = bc.contentPane(region='center',nodeId='pippo',
            onCreated="""
                this.querymanager = new gnr.FakeTableHandler(this);
            """,query_storepath='.querybag',query_table=table)
            