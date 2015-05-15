#!/usr/bin/env python
# encoding: utf-8

class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('cliente_tipo', pkey='codice', name_long='!![it]Cliente tipo', 
                        name_plural='!![it]Cliente tipi',caption_field='descrizione',lookup=True)
        self.sysFields(tbl,id=False)
        tbl.column('codice' ,size=':5',name_long='!![it]Codice')
        tbl.column('descrizione',name_long='!![it]Descrizione')