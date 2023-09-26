# encoding: utf-8

from gnr.app.gnrdbo import TotalizeTable
from gnr.core.gnrbag import Bag
from gnr.core.gnrdecorator import public_method,extract_kwargs

#Tabella di Totalizzazione: definire attributi pkey_columns, totalize_maintable, poi costruire la pkey "codekey"
#In movimento_riga, specificare totalizer_nomeapiacere='mag_light.giacenza_prodotto_deposito'
class Table(TotalizeTable):
    def config_db(self,pkg):
        tbl = pkg.table('giacenza_prodotto_deposito', pkey='codekey', pkey_columns='prodotto_id,deposito_codice',
                        name_long='!!Giacenze',
                        caption_field='prodotto_id',
                        totalize_maintable='mag_light.movimento_riga',
                        partition_deposito_codice='deposito_codice')
        self.sysFields(tbl,id=False, ins=False, upd=False, ldel=False,user_ins=False)

        tbl.column('codekey',size=':45',group='zz',name_long='key')
        tbl.column('prodotto_id', size='22', name_long='Prodotto', group='_', totalize_key=True).relation('mag_light.prodotto.id',
                                                                mode='foreignkey',
                                                                relation_name='giacenza',
                                                                onDelete='cascade')
        tbl.column('deposito_codice', size='3', name_long='Deposito', totalize_key=True).relation('mag_light.deposito.codice',
                                                                mode='foreignkey',
                                                                relation_name='giacenze_prodotti',
                                                                onDelete='cascade')         
        tbl.column('quantita_disponibile', dtype='I', name_long = 'Quantità disponibile', totalize_value='quantita')
        tbl.column('quantita_attesa', dtype='I', name_long = 'Quantità attesa', totalize_value=True)

        tbl.formulaColumn('giacenza_attesa', '$quantita_disponibile + $quantita_attesa', name_long='Giacenza attesa')

    def totalize_realign_sql(self,empty=False):
        if empty:
            self.empty()
            self.db.commit()
        if self.countRecords():
            return
        
        sql = """
            INSERT INTO mag_light.mag_light_giacenza_prodotto_deposito (codekey,prodotto_id,deposito_codice,quantita_disponibile,quantita_attesa,_refcount)
            (SELECT prodotto_id||'_'||deposito_codice,
                prodotto_id,
                deposito_codice,
                sum(quantita),
                sum(quantita_attesa),
                count(*)

            FROM mag_light.mag_light_movimento_riga
            GROUP BY prodotto_id, deposito_codice) ;
        """

        self.db.execute(sql)
        self.db.commit()
