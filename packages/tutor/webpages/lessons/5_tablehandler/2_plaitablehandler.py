# -*- coding: UTF-8 -*-
"""The first example of Genropy page"""

class GnrCustomWebPage(object):
    py_requires='th/th:TableHandler'
    
    def main(self,root,**kwargs):
        bc = root.borderContainer(datapath='main' ,height='100%')
        bc.contentPane(region='top',height='30px')
        bc.contentPane(region='center').plainTableHandler(table='glbl.regione',view_store_onStart=True)