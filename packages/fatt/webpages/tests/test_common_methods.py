# -*- coding: utf-8 -*-

# includedview_bagstore.py
# Created by Francesco Porcari on 2011-03-23.
# Copyright (c) 2011 Softwell. All rights reserved.

from gnr.core.gnrdecorator import public_method
from gnr.core.gnrbag import Bag

class GnrCustomWebPage(object):
    py_requires="""gnrcomponents/testhandler:TestHandlerFull"""

    def test_0_webpage(self,pane):
        fb = pane.formbuilder(cols=3)

        fb.numberTextBox('^.par_1',lbl='A')
        fb.numberTextBox('^.par_2',lbl='B')
        fb.div('^.result',lbl='Result sum A+B')

        pane.dataRpc('.result',self.getResultWebpage,par_1='^.par_1',par_2='^.par_2')
    
    @public_method
    def getResultWebpage(self,par_1=None,par_2=None,**kwargs):
        return self.fooSum(par_1 or 0,par_2 or 0)

    def test_1_table(self,pane):
        fb = pane.formbuilder(cols=3)

        fb.numberTextBox('^.par_1',lbl='A')
        fb.numberTextBox('^.par_2',lbl='B')
        fb.div('^.result',lbl='Result sum A+B')

        pane.dataRpc('.result',self.getResultTable,par_1='^.par_1',par_2='^.par_2')
    
    @public_method
    def getResultTable(self,par_1=None,par_2=None,**kwargs):
        return self.db.table('fatt.fattura').fooSum(par_1 or 0,par_2 or 0)

    def test_2_package(self,pane):
        fb = pane.formbuilder(cols=3)

        fb.numberTextBox('^.par_1',lbl='A')
        fb.numberTextBox('^.par_2',lbl='B')
        fb.div('^.result',lbl='Result sum A+B')

        pane.dataRpc('.result',self.getResultPackage,par_1='^.par_1',par_2='^.par_2')
    
    @public_method
    def getResultPackage(self,par_1=None,par_2=None,**kwargs):
        return self.db.package('fatt').fooSum(par_1 or 0,par_2 or 0)