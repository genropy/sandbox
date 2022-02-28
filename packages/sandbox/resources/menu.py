from gnr.web.gnrbaseclasses import BaseComponent,page_proxy

class Menu(BaseComponent):
    def config(self,root,**kwargs):
        root.thpage(u"Clienti", table="fatt.cliente")
        root.thpage(u"Fatture", table="fatt.fattura")
        #root.packageBranch('Mia fatturazione',pkg='fatt')
        root.webpage('Hello',filepath='hello_world')

