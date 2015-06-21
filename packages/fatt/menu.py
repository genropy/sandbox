#!/usr/bin/env python
# encoding: utf-8
def config(root,application=None):
    fatturazione = root.branch(u"Fatturazione")
    fatturazione.thpage(u"Clienti", table="fatt.cliente")
    fatturazione.thpage(u"Tipi Prodotto", table="fatt.prodotto_tipo")
    fatturazione.thpage(u"Prodotti", table="fatt.prodotto")
    fatturazione.thpage(u"Fatture", table="fatt.fattura")
    fatturazione.thpage(u"Agenti", table="fatt.agente")
    fatturazione.lookups(u"Tabelle Ausiliarie", lookup_manager="fatt")

