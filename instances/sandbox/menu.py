#!/usr/bin/env python
# encoding: utf-8
def config(root,application=None):
    tutor = root.branch("Tutor")
    tutor.branch("Lezioni", pkg="tutor", dir="lessons")
    tutor.branch("Esempi", pkg="tutor", dir="examples")
    tutor.branch("Esercizi", pkg="tutor", dir="exercises")

    fatturazione = root.branch("Fatturazione")
    fatturazione.thpage("Clienti", table="fatt.cliente")
    fatturazione.thpage("Tipi Prodotto", table="fatt.prodotto_tipo")
    fatturazione.thpage("Prodotti", table="fatt.prodotto")
    fatturazione.thpage("Fatture", table="fatt.fattura")
    fatturazione.lookups("Tabelle Ausiliarie", lookup_manager="fatt")

    root.branch("Amministrazione", tags="admin", pkg="adm")
    root.branch("Geo Italia", tags="admin", pkg="glbl")
    root.branch("Sistema", tags="sysadmin", pkg="sys")
    root.branch("Developer", tags="_DEV_", pkg="dev")
    root.branch("Widgetpedia", dir="widgetpedia",pkg='dev')
