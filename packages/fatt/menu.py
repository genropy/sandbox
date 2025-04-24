# encoding: utf-8
class Menu(object):
    def config(self,root,**kwargs):
        fatturazione = root.branch("Fatturazione", tags="")
        fatturazione.thpage("Clienti", table="fatt.cliente", tags="")
        fatturazione.thpage("Tipi Prodotto", table="fatt.prodotto_tipo", tags="")
        fatturazione.thpage("Prodotti", table="fatt.prodotto", tags="")
        fatturazione.thpage("Fatture", table="fatt.fattura", tags="")
        fatturazione.thpage("Righe vendita", table="fatt.fattura_riga", tags="")
        fatturazione.lookupBranch("Tabelle Ausiliarie", pkg="fatt")