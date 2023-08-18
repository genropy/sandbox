#!/usr/bin/env python
# encoding: utf-8

class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('prodotto')
        
        tbl.column('tipo_iva_codice',size=':5' ,
                    group='_',name_long='!![it]Tipo iva',
                    defaultFrom='@prodotto_tipo_id.tipo_iva'
                    ).relation('fatt.tipo_iva.codice',relation_name='prodotti',mode='foreignkey',onDelete='raise')