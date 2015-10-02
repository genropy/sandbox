# -*- coding: UTF-8 -*-
from gnr.core.gnrdecorator import public_method

class GnrCustomWebPage(object):
    py_requires='bottoniera:Bottoniera'

    def main(self,root,**kwargs):
        bc = root.borderContainer()
        self.bottonieraProdotti(bc.contentPane(region='top',height='50%',splitter=True),datapath='top')

        self.bottonieraProdotti(bc.contentPane(region='center'),datapath='center')

