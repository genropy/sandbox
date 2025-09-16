# encoding: utf-8
from gnrpkg.multidb.storetable import StoreTable

class Table(StoreTable):
    def config_db(self,pkg):
        tbl=pkg.table('shop', pkey='id', name_long='!![en]Shop', 
                      name_plural='!![en]Shops',caption_field='description')
        self.sysFields(tbl)
        tbl.column('denominazione',unique=True)
        tbl.column('partita_iva',unique=True)
        tbl.column('indirizzo', name_long='Indirizzo')