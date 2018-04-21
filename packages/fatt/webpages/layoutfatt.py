# -*- coding: UTF-8 -*-
from gnr.core.gnrdecorator import public_method
            
class GnrCustomWebPage(object):
    py_requires='mieilayout:LayoutBelli'
    def main(self,root,**kwargs):
        tabbone = root.superTabbone(datapath='tabbone')
