# encoding: utf-8
class Menu(object):
    def config(self,root,**kwargs):
        fatturazione = root.branch(u"Fatturazione", tags="")
        fatturazione.thpage(u"Clienti", table="fatt.cliente", tags="")
        fatturazione.thpage(u"Tipi Prodotto", table="fatt.prodotto_tipo", tags="")
        fatturazione.thpage(u"Prodotti", table="fatt.prodotto", tags="")
        fatturazione.thpage(u"Fatture", table="fatt.fattura", tags="")
        fatturazione.thpage(u"Righe vendita", table="fatt.fattura_riga", tags="")
        fatturazione.lookupBranch(u"Tabelle Ausiliarie", pkg="fatt")