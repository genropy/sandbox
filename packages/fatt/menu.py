#!/usr/bin/env python
# encoding: utf-8
class Menu(object):
    def config(self,root,**kwargs):
        fatturazione = root.branch(u"Fatturazione")
        fatturazione.thpage(u"Clienti", table="fatt.cliente")
        fatturazione.thpage(u"Tipi Prodotto", table="fatt.prodotto_tipo")
        fatturazione.thpage(u"Prodotti", table="fatt.prodotto")
        fatturazione.thpage(u"Fatture", table="fatt.fattura")
        fatturazione.thpage(u"Righe vendita", table="fatt.fattura_riga")
        fatturazione.lookupBranch(u"Tabelle Ausiliarie", pkg="fatt")