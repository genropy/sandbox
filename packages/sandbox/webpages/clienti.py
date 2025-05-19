# -*- coding: UTF-8 -*-

class GnrCustomWebPage(object):
    py_requires = "th/th:TableHandler"
    
    def main(self,root,**kwargs):
        clienti = self.db.table('fatt.cliente').query().fetch()
        frame = root.rootContentPane(datapath='main',design='sidebar',title='!![it] Clienti') 
        frame.thFormHandler(table='fatt.cliente',
                            formResource='ParametricQueryBugForm',
                            startKey=clienti[0]['id'], **kwargs)