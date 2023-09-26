#!/usr/bin/env python
# encoding: utf-8

class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('prodotto_marca', pkey='id', name_long='!![it]Marca Prodotto',
                                name_plural='!![it]Marca Prodotto', caption_field='nome', lookup=True)
        self.sysFields(tbl)

        tbl.column('nome' ,size=':50',name_long='!![it]Nome')