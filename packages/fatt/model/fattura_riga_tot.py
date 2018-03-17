#!/usr/bin/env python
# encoding: utf-8

from gnr.app.gnrdbo import TotalizeTable

class Table(TotalizeTable):
    def config_db(self,pkg):
        tbl=pkg.table('fattura_riga_tot', pkey='id', 
                    name_long='!!Fattura riga tot', 
                    name_plural='!!Fatture righe tot',
                    totalize_maintable='fatt.fattura_riga',
                    totalize_maincolumn='prodotto_id')
        self.sysFields(tbl)
        tbl.column('prodotto_id',size='22', group='_', name_long='!!Prodotto',totalize_key=True,
                    ).relation('prodotto.id', relation_name='totali_fatt', mode='foreignkey', onDelete='raise')
        tbl.column('anno_mese',size=':7', name_long='!!Anno mese',indexed=True,totalize_key='*')
        tbl.column('valore', dtype='money', name_long='!!Valore',totalize_value='prezzo_totale')
        tbl.column('quantita', dtype='money', name_long=u'!!Quantità',totalize_value='quantita')
        

    def totalize_key_anno_mese(self,record_riga,**kwargs):
        return '%s-%02i' %(record_riga['data_fattura'].year,record_riga['data_fattura'].month)
    
