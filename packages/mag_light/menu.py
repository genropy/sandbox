#!/usr/bin/env python
# encoding: utf-8
def config(root,application=None):
    mag = root.branch(u"Magazzino") #tags='magazzino'
    mag.thpage(u"!!Giacenze prodotti", table="mag_light.giacenza_prodotto_deposito")
    mag.thpage(u"!!Prodotti", table="mag_light.prodotto")
    mag.thpage(u"!!Tipi prodotto", table="mag_light.prodotto_tipo")
    mag.thpage(u"!!Movimenti", table="mag_light.movimento")
    mag.thpage(u"!!Tipi movimento", table="mag_light.movimento_tipo")
    mag.lookups('Configurazione', lookup_manager="mag_light")