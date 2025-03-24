#!/usr/bin/env python
# encoding: utf-8

from gnr.core.gnrnumber import floatToDecimal,decimalRound
from gnr.core.gnrdecorator import metadata
from gnr.core.gnrdecorator import public_method


class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('fattura', pkey='id', name_long='!![it]Fattura', name_plural='!![it]Fattura',caption_field='protocollo')
        self.sysFields(tbl)
        tbl.column('protocollo' ,size='10',name_long='!![it]Protocollo')
        tbl.column('cliente_id',size='22' ,group='_',name_long='!![it]Cliente'
                                        ).relation('cliente.id',
                                                    relation_name='fatture',
                                                    mode='foreignkey',onDelete='raise')
        tbl.column('tipo_id',size='22', group='_', name_long='Tipo'
                    ).relation('fattura_tipo.id', relation_name='fatture', mode='foreignkey', onDelete='raise')
        tbl.column('data',dtype='D',name_long='!![it]Data')
        tbl.column('totale_imponibile',dtype='money',name_long='!![it]Totale imponibile')
        tbl.column('totale_lordo',dtype='money',name_long='!![it]Totale lordo')
        tbl.column('totale_iva',dtype='money',name_long='!![it]Totale Iva')
        tbl.column('totale_fattura',dtype='money',name_long='!![it]Totale')
        tbl.column('codice_contatore',size=':2',defaultFrom='@tipo_id')

        tbl.column('sconto',dtype='percent',name_long='Sconto')
        tbl.aliasColumn('clientenome','@cliente_id.ragione_sociale',name_long='Cliente')

    def ricalcolaTotali(self,fattura_id=None,mylist=None):
        with self.recordToUpdate(fattura_id) as record:
            totale_lordo,totale_iva = self.db.table('fatt.fattura_riga'
                                                    ).readColumns(columns="""SUM($prezzo_totale) AS totale_lordo,
                                                                             SUM($iva) AS totale_iva""",
                                                                             where='$fattura_id=:f_id',f_id=fattura_id)
            
            record['totale_lordo'] = floatToDecimal(totale_lordo)
            record['totale_imponibile'] = record['totale_lordo']
            record['totale_iva'] = floatToDecimal(totale_iva)
            record['totale_fattura'] = record['totale_imponibile'] + record['totale_iva']

    def defaultValues(self):
        return dict(data = self.db.workdate)

    def counter_protocollo(self,record=None):
        #F21/000001
        codice_contatore = record['codice_contatore'] or 'F' if record else '*'
        return dict(format='$K$YY/$NNNNNN',code=codice_contatore,period='YY',
                    date_field='data',showOnLoad=True,recycle=True)


    @metadata(doUpdate=True)
    def touch_fix_totali(self,record,old_record=None,**kwargs):
        print("record['totale_imponibile']",record['totale_imponibile'])
        record['totale_lordo'] = record['totale_imponibile']


    def randomValues(self):
        return dict(protocollo=False,
                    totale_imponibile=False,
                    totale_lordo=False,
                    totale_iva=False,
                    totale_fattura=False,
                    data=dict(sorted=True))