# -*- coding: UTF-8 -*-
"""The first example of Genropy page"""
from gnr.core.gnrbag import Bag,DirectoryResolver
from gnr.core.gnrdecorator import public_method
class GnrCustomWebPage(object):

    
    def source_viewer_open(self):
        return False
    
    def main(self,root,**kwargs):
        bc = root.borderContainer(datapath='main')
        bc.contentPane(region='top').textbox(value='^.path')
        bc.dataRpc('.tree', self.getTreeRpc,p='^.path')

        bc.contentPane(region='center').tree(storepath='.tree')

    @public_method
    def getTreeRpc(self,p=None,**kwargs):
        b = Bag()
        b.setItem('root.disk',DirectoryResolver(p))
        return b