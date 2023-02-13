# encoding: utf-8


class Table(object):
    def config_db(self, pkg):
        tbl =  pkg.table('offerta_riga', pkey='id',name_long=u'!![it]Riga offerta',
                    default_md_mode='STD',
                    md_mode_MAG='Standard',
                    md_fkey_MAG='prodotto_id', name_plural=u'!![it]Righe offerta')
        self.sysFields(tbl,counter='offerta_id')
        tbl.column('offerta_id',size='22').relation('offerta.id',
                            relation_name='righe',
                            mode='foreignkey',
                            onDelete='cascade')  
        tbl.column('prodotto_id',size='22' ,group='_',name_long='!!Prodotto',md_mode='STD',
                    ).relation('fatt.prodotto.id',
                                relation_name='righe_offerta',onDelete='raise')
        tbl.column('descrizione',name_long='!![it]Descrizione')
        tbl.column('quantita','qta',name_long='!![it]Quantita')
        tbl.column('prezzo_unitario','money',name_long='!![it]Prezzo unitario',defaultFrom='@prodotto_id')
        tbl.column('sconto','percent',name_long='!![it]Sconto')
        tbl.column('importo_lordo','money',name_long='!![it]Lordo')
        tbl.column('importo_netto','money',name_long='!![it]Netto')
        tbl.column('aliquota_iva',dtype='percent',name_long='!![it]Aliquota',defaultFrom='@prodotto_id')
        tbl.column('riga_descrizione',dtype='B',name_long='!![it]Riga descrizione',name_short='RD')

