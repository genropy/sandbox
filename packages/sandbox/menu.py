# encoding: utf-8

class Menu(object):

    def config(self,root,**kwargs):
        root.thpage(u"Clienti", table="fatt.cliente")
        root.thpage(u"Fatture", table="fatt.fattura")
        root.packageBranch('Mia fatturazione',pkg='fatt')
        root.webpage('Hello',filepath='hello_world')
