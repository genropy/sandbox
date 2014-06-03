# -*- coding: UTF-8 -*-
"""The first example of Genropy page"""

class GnrCustomWebPage(object):
    
    def main(self,root,**kwargs):
        root.div('Hello world')
        root.div('Hello savi')
        root.dbselect(value='^hh',dbtable='glbl.provincia')