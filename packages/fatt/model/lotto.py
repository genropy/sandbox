# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('lotto', pkey='key_lotto', name_long='Lotto', 
                                    name_plural='Lotti',caption_field='descrizione')
        self.sysFields(tbl, id=False)
        
        tbl.column('prodotto_id',size='22', group='_', name_long='Prodotto'
                    ).relation('prodotto.id', relation_name='lotti', mode='foreignkey', onDelete='raise')
        tbl.column('codice_lotto', size=':10', name_long='Codice Lotto', name_short='Lotto')
        tbl.column('descrizione', name_long='Descrizione')
        tbl.column('data_produzione', dtype='D', name_long='Data produzione')
        tbl.column('data_scadenza', dtype='D', name_long='Data scadenza')
        
        tbl.compositeColumn('key_lotto', columns='prodotto_id,codice_lotto', static=True)