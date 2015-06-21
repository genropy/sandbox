#!/usr/bin/env python
# encoding: utf-8

class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('apparato')
        tbl.column('cliente', group='_', 
                    name_long='!!Cliente', 
                    name_short='Cliente').relation('fatt.cliente.id',relation_name='apparato_clientefk',mode='foreignkey',onDelete='raise')
