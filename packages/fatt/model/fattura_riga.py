#!/usr/bin/env python
# encoding: utf-8

from gnr.core.gnrnumber import decimalRound

class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('fattura_riga', pkey='id', name_long='!![it]Fattura riga', name_plural='!![it]Fattura righe')
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

    def calcolaPrezziRiga(self, record):
        prezzo_unitario,aliquota_iva = self.db.table('fatt.prodotto').readColumns(columns='$prezzo_unitario,@tipo_iva_codice.aliquota',pkey=record['prodotto_id'])
        record['prezzo_unitario'] = prezzo_unitario
        record['aliquota_iva'] = aliquota_iva
        record['prezzo_totale'] = decimalRound(record['quantita'] * record['prezzo_unitario'])
        record['iva'] = decimalRound(record['aliquota_iva'] * record['prezzo_totale'] /100)

    def aggiornaFattura(self,record):
        fattura_id = record['fattura_id']
        self.db.deferToCommit(self.db.table('fatt.fattura').ricalcolaTotali,
                                    fattura_id=fattura_id,
                                    _deferredId=fattura_id)

        #self.db.table('fatt.fattura').ricalcolaTotali(record['fattura_id'])

    def trigger_onInserting(self, record):
        self.calcolaPrezziRiga(record)

    def trigger_onUpdating(self, record):
        self.calcolaPrezziRiga(record)

    def trigger_onInserted(self,record=None):
        self.aggiornaFattura(record)

    def trigger_onUpdated(self,record=None,old_record=None):
        self.aggiornaFattura(record)

    def trigger_onDeleted(self,record=None):
        if self.currentTrigger.parent:
            return
        self.aggiornaFattura(record)

    def randomValues(self):
        return dict(prezzo_unitario=False,
                   aliquota_iva=False,
                    prezzo_totale=False,
                    iva=False)
