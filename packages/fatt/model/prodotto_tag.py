#!/usr/bin/env python
# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl = pkg.table('prodotto_tag', pkey='id', name_long='!!Prodotto tag', name_plural='!!Prodotto tag')
        self.sysFields(tbl)
        tbl.column('prodotto_id',size = '22', group = '_', name_long = '!!Prodotto'
                    , name_short = '!!Prodotto').relation('prodotto.id', relation_name = 'tag_collegati', mode = 'foreignkey')
        tbl.column('tag_codice',size = ':20', group = '_', name_long = '!!Tag'
                    ).relation('tagprod.codice',relation_name='prodotti', mode = 'foreignkey')