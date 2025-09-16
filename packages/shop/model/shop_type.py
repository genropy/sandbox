# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('shop_type', pkey='code', 
                      name_long='Shop type',
                        name_plural='Shop types')
        self.sysFields(tbl,id=False)
        tbl.column('code', size=':10', name_long='Codice')
        tbl.column('descrizione', name_long='Descrizione')
        