#!/usr/bin/env python
# encoding: utf-8

class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('cliente', pkey='id', name_long='!![it]Cliente', 
                        name_plural='!![it]Clienti',caption_field='ragione_sociale',
                        branch_field='categoria')
        self.sysFields(tbl) # aggiunge id autogenerato, __ins_ts,__mod_ts,etc.
        tbl.column('ragione_sociale' ,size=':40',name_long='!![it]Ragione sociale',name_short='Rag. Soc.',validate_notnull=True,validate_len='2:40')
        tbl.column('indirizzo',name_long='!![it]Indirizzo')
        provincia = tbl.column('provincia',size='2',name_long='!![it]Provincia',
                    name_short='Pr.'
                    )
        provincia.relation('glbl.provincia.sigla',
                            relation_name='clienti',
                            mode='foreignkey',onDelete='raise')
        tbl.column('comune_id',size='22' ,group='_',name_long='!![it]Comune').relation('glbl.comune.id',relation_name='clienti',mode='foreignkey',onDelete='raise')
        tbl.column('cliente_tipo_codice',size=':5',name_long='!![it]Tipo cliente',name_short='!![it]Tipo').relation('cliente_tipo.codice',relation_name='clienti',mode='foreignkey',onDelete='raise')
        tbl.column('pagamento_tipo_codice',size=':5',name_long='!![it]Tipo pagamento',name_short='!![it]Tipo pagamento').relation('pagamento_tipo.codice',relation_name='clienti',mode='foreignkey',onDelete='raise')
        tbl.column('note',name_long="!![it]Note")
        tbl.column('email',name_long='!![it]Email')

        tbl.formulaColumn('n_fatture',select=dict(table='fatt.fattura',
                                                  columns='COUNT(*)',
                                                  where='$cliente_id=#THIS.id'),
                                      dtype='L',name_long='N.Fatture')

        tbl.formulaColumn('tot_fatturato',select=dict(table='fatt.fattura',
                                                  columns='SUM($totale_fattura)',
                                                  where='$cliente_id=#THIS.id'),
                                      dtype='N',name_long='Tot.Fatturato')
  