# -*- coding: UTF-8 -*-
from gnr.core.gnrdecorator import public_method

class GnrCustomWebPage(object):
    py_requires='th/th:TableHandler'
    def main(self,root,**kwargs):
        root.plainTableHandler(table='fatt.cliente',dbstore='@sandbox_sqlite',datapath='mainclienti')