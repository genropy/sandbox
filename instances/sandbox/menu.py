#!/usr/bin/env python
# encoding: utf-8
def config(root,application=None):
    tutor = root.branch("Tutor")
    tutor.branch("Lezioni", pkg="tutor", dir="lessons")
    tutor.branch("Esempi", pkg="tutor", dir="examples")
    tutor.branch("Esercizi", pkg="tutor", dir="exercises")
    root.branch("Widgetpedia", dir="widgetpedia",pkg='dev')
    fatturazione = root.branch("Fatturazione")
    fatturazione.thpage("Clienti", table="fatt.cliente")
    fatturazione.thpage("Tipi Prodotto", table="fatt.prodotto_tipo")
    fatturazione.thpage("Prodotti", table="fatt.prodotto")
    fatturazione.thpage("Fatture", table="fatt.fattura")
    fatturazione.thpage("Venditore", table="fatt.venditore")
    fatturazione.lookups("Tabelle Ausiliarie", lookup_manager="fatt")
    root.branch("Amministrazione", tags="admin", pkg="adm")
    root.branch("Geo Italia", tags="admin", pkg="glbl")
    root.branch("Sistema", tags="sysadmin,_DEV_", pkg="sys")
    test15 = root.branch("Test pages")
    test15.branch("Components", pkg="test15",dir='components')
    test15.branch("Dojo" ,pkg="test15",dir='dojo')
    test15.branch("Gnrwdg", pkg="test15",dir='gnrwdg')
    test15.branch("Dev tools", pkg="test15",dir='devtools')
    
    
