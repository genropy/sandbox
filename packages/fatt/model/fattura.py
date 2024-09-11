#!/usr/bin/env python
# encoding: utf-8

from past.utils import old_div
from gnr.core.gnrnumber import floatToDecimal,decimalRound
from gnr.core.gnrdecorator import metadata, public_method
from gnrpkg.fatt.fatture.descrittori import FattureManager


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
        tbl.column('totale_lordo',dtype='money',name_long='!![it]Totale lordo')
        tbl.column('totale_iva',dtype='money',name_long='!![it]Totale Iva')
        tbl.column('totale_fattura',dtype='money',name_long='!![it]Totale')
        tbl.column('peso_spedizione', dtype='N', format='##,00', name_long='!![it]Peso Spedizione (kg)',
                        checkpref='fatt.magazzino.abilita_spese_spedizione')
        tbl.column('costo_spedizione', dtype='money', name_long='!![it]Costo Spedizione', name_short='!![it]Costo Spedizione',
                        checkpref='fatt.magazzino.abilita_spese_spedizione')
        tbl.column('sconto',dtype='percent',name_long='Sconto')

        tbl.aliasColumn('clientenome','@cliente_id.ragione_sociale',name_long='Cliente')
        tbl.formulaColumn('mese_fattura', """EXTRACT(MONTH FROM $data) || '-' || EXTRACT(YEAR FROM $data)""")
        tbl.formulaColumn('anno_fattura', """EXTRACT(YEAR FROM $data)""")
        tbl.joinColumn('scaglione_id', name_long='Scaglione ID').relation('scaglione.id',between= "$totale_fattura;@scaglione_id.da;@scaglione_id.a")
        tbl.joinColumn('prodotto_tipo_id', name_long='Tipo prodotto ID',
                        dtype='N',size='22').relation('prodotto_tipo.id',
                                    cnd="""@tariffa_id.scaglione_id = $scaglione_id AND
                                    @tariffa_id.warehouse_codice=$lvbecd AND
                                    @tariffa_id.provincia=$lvaepr""", relation_name='righe')
        #Queste due formulaColumn vengono utilizzate nella stampa stats_fatturato per estrarre mese e anno dalla data


    def defaultValues(self):
        return dict(data = self.db.workdate,sconto=floatToDecimal('0'))

    def counter_protocollo(self,record=None):
        #F14/000001
        return dict(format='$K$YY/$NNNNNN',code='F',period='YY',
                    date_field='data',showOnLoad=True,recycle=True)

    def randomValues(self):
        return dict(protocollo=False,
                    totale_imponibile=False,
                    totale_lordo=False,
                    totale_iva=False,
                    totale_fattura=False,
                    data=dict(sorted=True),
                    peso_spedizione=False,
                    costo_spedizione=False,
                    sconto=False)

    @metadata(doUpdate=True)
    def touch_fix_totali(self,record,old_record=None,**kwargs):
        print("record['totale_imponibile']",record['totale_imponibile'])
        record['totale_lordo'] = record['totale_imponibile']
        record['sconto'] = floatToDecimal('0')
    

    def ricalcolaTotali(self,fattura_id=None,mylist=None):
        with self.recordToUpdate(fattura_id) as record:
            totale_lordo,totale_iva = self.db.table('fatt.fattura_riga'
                                                        ).readColumns(columns="""SUM($prezzo_totale) AS totale_lordo,
                                                                                 SUM($iva) AS totale_iva""",
                                                                                 where='$fattura_id=:f_id',f_id=fattura_id)
            
            record['sconto'] = floatToDecimal(record['sconto'] or 0)
            record['totale_lordo'] = floatToDecimal(totale_lordo)
            record['totale_imponibile'] = decimalRound(old_div(record['totale_lordo']*(100-record['sconto']),100))
            record['totale_iva'] = floatToDecimal(totale_iva)
            if record['costo_spedizione']:
                record['totale_fattura'] = record['totale_imponibile'] + record['totale_iva'] + record['costo_spedizione']
            else:
                record['totale_fattura'] = record['totale_imponibile'] + record['totale_iva']
            self.checkImportoMin(record)

    def checkImportoMin(self, record):
        #Controlla che il totale della fattura non sia inferiore all'importo minimo definito nelle preferenze
        if self.db.application.getPreference('generali.abilita_importi_fattura', pkg='fatt') and record['totale_fattura'] < self.db.application.getPreference(
                        'generali.min_importo', pkg='fatt', mandatoryMsg='!![it]Non hai impostato un importo minimo per le fatture'):
            raise self.exception('standard', msg="Devi raggiungere l'importo minimo per salvare la fattura")

    @public_method
    def duplica(self, fattura_id=None):
        
        manager = FattureManager(self.db)

        manager.duplicaFattura(fattura_id)
        manager.scriviFattura()
