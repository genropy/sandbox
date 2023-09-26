# encoding: utf-8

class Table(object):
    def config_db(self, pkg):
        tbl =  pkg.table('prodotto_tipo_alias',pkey='id',name_long='!!Prodotto alias',
                      name_plural='!!Prodotto alias')
        self.sysFields(tbl)
        tbl.column('prodotto_id',size='22',group='_',name_long='Prodotto id').relation('prodotto.id', 
                                        mode='foreignkey', onDelete='cascade',
                                        relation_name='prodotti_tipi_alias')
        tbl.column('prodotto_tipo_id',size='22',group='_',name_long='Prodotto tipo id').relation('prodotto_tipo.id', 
                                        mode='foreignkey', onDelete='cascade',
                                        relation_name='prodotti_tipi_alias')