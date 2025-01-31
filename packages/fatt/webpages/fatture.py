# -*- coding: UTF-8 -*-

class GnrCustomWebPage(object):
    py_requires='th/th:TableHandler'
    
    def main(self,root,**kwargs):
        root.contentPane(region='center', datapath='fatture').plainTableHandler(table='fatt.fattura', view_store__onStart=True,
                                                            viewResource='ViewPrintTest')
        
        