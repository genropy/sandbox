# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('prodotto_data_totale', pkey='id')
        self.sysFields(tbl)

        tbl.column('data', dtype='D', name_long='Data')
        tbl.column('prodotto_id',size='22', group='_', name_long='Prodotto'
                    ).relation('prodotto.id', relation_name='totali_giornalieri', mode='foreignkey', onDelete='cascade')   
        tbl.column('totale', dtype='N', name_long='Totale')

    
    def aggiornaTotaleGiornaliero(self,prodotto_id=None,data=None):
        tot = self.db.table('fatt.fattura_riga').readColumns(where='$prodotto_id=:pid AND $data_fattura=:d',
                                            columns='SUM($prezzo_totale)',pid=prodotto_id,d=data)
        with self.recordToUpdate(prodotto_id=prodotto_id,data=data,insertMissing=True) as r:
            r['prodotto_id'] = prodotto_id
            r['data'] = data
            r['totale'] = tot