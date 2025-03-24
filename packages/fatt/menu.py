# encoding: utf-8
class Menu(object):
    def config(self,root,**kwargs):
        fatturazione = root.branch(u"Fatturazione")
        fatturazione.thpage("Clienti", table="fatt.cliente")
        fatturazione.thpage("Tipi Prodotto", table="fatt.prodotto_tipo")
        fatturazione.thpage("Prodotti", table="fatt.prodotto")
        fatturazione.thpage("Tipi fattura", table="fatt.fattura_tipo")
        fatturazione.thpage("Fatture", table="fatt.fattura")
        fatturazione.thpage("Righe vendita", table="fatt.fattura_riga")
        fatturazione.lookupBranch("Tabelle Ausiliarie", pkg="fatt")