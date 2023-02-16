#!/usr/bin/env python
# encoding: utf-8

class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('cliente', pkey='id', name_long='!![it]Cliente', 
                        name_plural='!![it]Clienti',caption_field='ragione_sociale',
                        branch_field='categoria')
        self.sysFields(tbl) # aggiunge id autogenerato, __ins_ts,__mod_ts,etc.
        group_anag = tbl.colgroup('anag',name_long='Dati anagrafici')
        group_anag.column('ragione_sociale' ,size=':40',name_long='!![it]Ragione sociale',name_short='Rag. Soc.',validate_notnull=True,validate_len='2:40')
        group_anag.column('indirizzo',name_long='!![it]Indirizzo')
        group_anag.column('provincia',size='2',name_long='!![it]Provincia',
                    name_short='Pr.').relation('glbl.provincia.sigla',
                            relation_name='clienti',
                            mode='foreignkey',onDelete='raise')
        group_anag.column('comune_id',size='22' ,group='_',name_long='!![it]Comune').relation('glbl.comune.id',relation_name='clienti',mode='foreignkey',onDelete='raise')
        group_anag.column('email',name_long='!![it]Email')

        group_comm = tbl.colgroup('comm',name_long='Dati commerciali')

        group_comm.column('cliente_tipo_codice',size=':5',name_long='!![it]Tipo cliente',name_short='!![it]Tipo').relation('cliente_tipo.codice',relation_name='clienti',mode='foreignkey',onDelete='raise')
        group_comm.column('pagamento_tipo_codice',size=':5',name_long='!![it]Tipo pagamento',name_short='!![it]Tipo pagamento').relation('pagamento_tipo.codice',relation_name='clienti',mode='foreignkey',onDelete='raise')
        group_comm.column('note',name_long="!![it]Note")
        group_comm.column('data_iscrizione_newsletter', dtype='D', name_long='Data iscrizione newsletter')
        group_comm.column('data_disiscrizione_newsletter', dtype='D', name_long='Data disiscrizione newsletter')
        group_comm.formulaColumn('iscritto_newsletter', """CASE WHEN $data_iscrizione_newsletter IS NOT NULL AND
                                                    $data_disiscrizione_newsletter IS NULL THEN TRUE
                                                    WHEN $data_disiscrizione_newsletter IS NOT NULL THEN FALSE ELSE NULL END""",
                                                    dtype='B', name_long='Iscr.newsletter')
        group_eco = tbl.colgroup('economici',name_long='Dati economici')
        group_eco.formulaColumn('n_fatture',select=dict(table='fatt.fattura',
                                                  columns='COUNT(*)',
                                                  where='$cliente_id=#THIS.id'),
                                      dtype='L',name_long='N.Fatture')

        group_eco.formulaColumn('tot_fatturato',select=dict(table='fatt.fattura',
                                                  columns='SUM($totale_fattura)',
                                                  where='$cliente_id=#THIS.id'),
                                      dtype='N',name_long='Tot.Fatturato')
  