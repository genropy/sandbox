#!/usr/bin/env python
# encoding: utf-8

class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('prodotto_tipo', pkey='id', name_long='!![it]Prodotto tipo',
                         name_plural='!![it]Prodotto tipi',
                        caption_field='hierarchical_descrizione')
        self.sysFields(tbl,hierarchical='descrizione', counter=True, df=True)
        tbl.column('descrizione' ,size=':50',name_long='!![it]Descrizione')