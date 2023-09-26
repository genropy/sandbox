# encoding: utf-8

from gnr.core.gnrdecorator import public_method

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('movimento_riga', pkey='id', name_long='Riga Movimento', 
                            name_plural='Righe Movimento', caption_field='prodotto_id', 
                            partition_deposito_codice='deposito_codice', 
                            totalizer_giacenza_prodotto_deposito='mag_light.giacenza_prodotto_deposito')
                            #Tabella di totalizzazione
        self.sysFields(tbl)
        
        tbl.column('prodotto_id',size='22' , group='_', name_long='!![it]Prodotto').relation(
                        'prodotto.id', relation_name='ordini', mode='foreignkey', onDelete='setnull')                
        tbl.column('quantita', dtype='L', name_long='!![it]Quantità')
        tbl.column('quantita_attesa', dtype='L', name_long='!![it]Quantità attesa')
        tbl.column('movimento_id',size='22', group='_', name_long='Movimento'
                    ).relation('movimento.id', relation_name='movimento_righe', mode='foreignkey', onDelete='cascade')
        tbl.column('movimento_riga_id',size='22', group='_', name_long='Movimento'
                    ).relation('movimento_riga.id', relation_name='riga_movimento', one_one=True, mode='foreignkey', onDelete='cascade')
        tbl.column('deposito_codice',size='3' , group='_', name_long='!![it]Deposito').relation(
                        'deposito.codice', relation_name='movimento_righe', mode='foreignkey', onDelete='raise')

        tbl.aliasColumn('in_attesa', '@movimento_id.in_attesa', name_long='Movimento in attesa', static=True)
        tbl.formulaColumn('quantita_riga', "GREATEST(abs($quantita), abs($quantita_attesa))", dtype='N', name_long='!![it]Quantità riga')

    def setDefaultValues(self, record):
        record['deposito_codice'] = record['deposito_codice'] or self.db.currentEnv['current_deposito_codice']
        record['quantita_attesa'] = record['quantita_attesa'] or 0
        record['quantita'] = record['quantita'] or 0
    
    def trigger_onInserting(self, record):
        self.setDefaultValues(record)
        verso = self.db.table('mag_light.movimento').readColumns(record['movimento_id'], columns='$verso')
        segno = (-1) if verso == 'S' else 1 
        record['quantita_attesa'] = record['quantita_attesa'] * segno 
        record['quantita'] = record['quantita'] * segno

    def confermaRighe(self, movimento_record=None):
        def updaterCb(r):
            r['quantita'] = r['quantita_attesa']
            r['quantita_attesa'] = 0
        
        self.batchUpdate(updaterCb, where='$movimento_id=:mov_id', mov_id=movimento_record['id'])