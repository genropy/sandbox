#!/usr/bin/env python
# encoding: utf-8

class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('tipo_iva', pkey='codice', name_long='!![it]Tipo iva', 
                        name_plural='!![it]Tipi iva',caption_field='descrizione',lookup=True)
        self.sysFields(tbl,id=False)
        tbl.column('codice' ,size=':5',name_long='!![it]Codice')
        tbl.column('descrizione',name_long='!![it]Descrizione')
        tbl.column('aliquota',dtype='percent',name_long='!![it]Aliquota')
        tbl.column('valido_dal', dtype='D', name_long='Valido dal')
        tbl.column('valido_al', dtype='D', name_long='Valido al')