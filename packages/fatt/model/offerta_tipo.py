#!/usr/bin/env python
# encoding: utf-8

from gnr.core.gnrdecorator import metadata

class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('offerta_tipo', pkey='codice', name_long='!!Tipo offerta',
                         name_plural='!!Tipi offerta',
                         caption_field='descrizione')
        self.sysFields(tbl,id=False)
        tbl.column('codice' ,size=':5',name_long='!![it]Codice', unique=True, indexed=True, validate_notnull=True)
        tbl.column('descrizione' ,size=':30',name_long='!![it]Descrizione')
        tbl.column('codice_contatore', size=':2', name_long='C.Cont')
        tbl.column('conf_print', dtype='X', name_long='!![it]Conf.Stampa',protected_by=False)
        tbl.column('conf_grid', dtype='X', name_long='!![it]Conf.Griglia',protected_by=False)

    def getMenuTipi(self):
        f = self.query(order_by='$codice').fetch()
        return [(r['descrizione'],dict(tipo_ddt=r['codice'])) for r in f]
