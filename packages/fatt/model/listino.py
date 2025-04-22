# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('listino', pkey='id', name_long='Listino', name_plural='Listini',caption_field='caption')
        self.sysFields(tbl)

        tbl.column('prodotto_id', size='22', name_long='Prodotto'
                   ).relation('prodotto.id', relation_name='listini')
        tbl.column('cliente_tipo_codice', size=':5', name_long='Tipo cliente'
                   ).relation('cliente_tipo.codice', relation_name='listini')
        tbl.column('prezzo_personalizzato', dtype='money', name_long='Prezzo personalizzato', 
                   defaultFrom='@prodotto_id.prezzo_unitario')
        
        tbl.column('data_inizio', dtype='D', name_long='Data inizio')
        tbl.column('data_fine', dtype='D', name_long='Data fine')
        
        tbl.formulaColumn('caption', "$cliente_tipo_codice || ' - ' ||@prodotto_id.codice")
        
    def defaultValues(self):
        return dict(data_inizio=self.db.workdate)