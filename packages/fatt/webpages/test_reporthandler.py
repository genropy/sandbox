    
# -*- coding: UTF-8 -*-
"""ClientPage tester"""
from gnr.core.gnrdecorator import public_method


class GnrCustomWebPage(object):
    py_requires = """gnrcomponents/testhandler:TestHandlerFull,
                     gnrcomponents/reporthandler/reporthandler:ReportHandler
                    """

    def test_reporthandler(self,pane):
        pane.reportHandler(table='fatt.fattura',height='500px',width='700px')
