# -*- coding: utf-8 -*-

from gnr.core.gnrdecorator import public_method
from gnr.core.gnrbag import Bag


class GnrCustomWebPage(object):
    py_requires = "gnrcomponents/testhandler:TestHandlerBase"
    
    def test_0(self, pane):
        "Insert your test here"
        fb = pane.formbuilder(cols=1)