#!/usr/bin/env python
# encoding: utf-8
from gnr.core.gnrdecorator import metadata

class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('fattura_riga', pkey='id', name_long='!![it]Fattura riga',
                            name_plural='!![it]Fattura righe',
                            totalizer_articolo_totale='fatt.fattura_riga_tot')
        self.sysFields(tbl,counter='fattura_id')
        tbl.column('fattura_id',size='22' ,group='_',
                    name_long='!![it]Fattura'
                    ).relation('fattura.id',relation_name='righe',mode='foreignkey',onDelete='cascade')
        tbl.column('prodotto_id',size='22' ,group='_',name_long='!![it]Prodotto').relation('prodotto.id',relation_name='righe_fattura',mode='foreignkey',onDelete='raise')
        tbl.column('quantita',dtype='I',name_long=u'!![it]Quantità',name_short='Q.')
        tbl.column('prezzo_unitario',dtype='money',name_long='!![it]Prezzo unitario',name_short='P.U.')
        tbl.column('aliquota_iva',dtype='money',name_long='!![it]Aliquota iva',name_short='Iva')

        tbl.column('prezzo_totale',dtype='money',name_long='!![it]Prezzo totale',name_short='P.T.')
        tbl.column('iva',dtype='money',name_long='!![it]Tot.Iva')
        
        tbl.column('data_fattura', dtype='D', name_long='!!Data fattura')

    

    def aggiornaFattura(self,record):
        fattura_id = record['fattura_id']
        self.db.deferToCommit(self.db.table('fatt.fattura').ricalcolaTotali,
                                    fattura_id=fattura_id,
                                    _deferredId=fattura_id)

        #self.db.table('fatt.fattura').ricalcolaTotali(record['fattura_id'])

    def trigger_onInserted(self,record=None):
        self.aggiornaFattura(record)

    def trigger_onUpdated(self,record=None,old_record=None):
        if self.fieldsChanged('prezzo_totale,iva',record=record,old_record=old_record):
            self.aggiornaFattura(record)

    def trigger_onDeleted(self,record=None):
        if self.currentTrigger.parent:
            return
        self.aggiornaFattura(record)

    @metadata(doUpdate=True,columns='*,@fattura_id.data AS data_fatt')
    def touch_aggiorna_data_fattura(self,record,old_record=None):
        record['data_fattura'] = record['data_fatt']