#!/usr/bin/env python
# encoding: utf-8

class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('fattura', pkey='id', name_long='!![it]Fattura', name_plural='!![it]Fattura',caption_field='protocollo')
        self.sysFields(tbl)
        tbl.column('protocollo' ,size='10',name_long='!![it]Protocollo')
        tbl.column('cliente_id',size='22' ,group='_',name_long='!![it]Cliente'
                                        ).relation('cliente.id',
                                                    relation_name='fatture',
                                                    mode='foreignkey',onDelete='raise')
        tbl.column('data',dtype='D',name_long='!![it]Data')
        tbl.column('totale_imponibile',dtype='money',name_long='!![it]Totale imponibile')
        tbl.column('totale_iva',dtype='money',name_long='!![it]Totale Iva')
        tbl.column('totale_fattura',dtype='money',name_long='!![it]Totale')

    def ricalcolaTotali(self,fattura_id=None):
        with self.recordToUpdate(fattura_id) as record:
            totale_imponibile,totale_iva = self.db.table('fatt.fattura_riga'
                                                        ).readColumns(columns="""SUM($prezzo_totale) AS totale_imponibile,
                                                                                 SUM($iva) AS totale_iva""",
                                                                                 where='$fattura_id=:f_id',f_id=fattura_id)
            record['totale_imponibile'] = totale_imponibile
            record['totale_iva'] = totale_iva
            record['totale_fattura'] = totale_imponibile + totale_iva

    def defaultValues(self):
        return dict(data = self.db.workdate)


    def counter_protocollo(self,record=None):
        #F14/000001
        return dict(format='$K$YY/$NNNNNN',code='F',period='YY',
                    date_field='data',showOnLoad=True,recycle=True)