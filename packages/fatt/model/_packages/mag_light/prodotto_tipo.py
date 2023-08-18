#!/usr/bin/env python
# encoding: utf-8

class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('prodotto_tipo')
        
        tbl.column('tipo_iva',size=':5' ,
                    group='_',name_long='!![it]Tipo iva',defaultFrom='@parent_id'
                    ).relation('fatt.tipo_iva.codice',relation_name='tipi_prodotto',
                                    mode='foreignkey',onDelete='raise')