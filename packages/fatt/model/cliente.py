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
                    name_short='Pr.')
        provincia.relation('glbl.provincia.sigla',
                            relation_name='clienti',
                            mode='foreignkey',onDelete='raise')
        tbl.column('comune_id',size='22' ,group='_',name_long='!![it]Comune').relation('glbl.comune.id',relation_name='clienti',mode='foreignkey',onDelete='raise')
        tbl.column('cliente_tipo_codice',size=':5',name_long='!![it]Tipo cliente',name_short='!![it]Tipo').relation('cliente_tipo.codice',relation_name='clienti',mode='foreignkey',onDelete='raise')
        tbl.column('pagamento_tipo_codice',size=':5',name_long='!![it]Tipo pagamento',name_short='!![it]Tipo pagamento').relation('pagamento_tipo.codice',relation_name='clienti',mode='foreignkey',onDelete='raise')
        tbl.column('note',name_long="!![it]Note")
        tbl.column('email',name_long='!![it]Email')
        tbl.column('dati_estesi', dtype='X', name_long='Dati estesi')
        tbl.column('data_iscrizione_newsletter', dtype='D', name_long='Data iscrizione newsletter')
        tbl.column('data_disiscrizione_newsletter', dtype='D', name_long='Data disiscrizione newsletter')
        tbl.formulaColumn('iscritto_newsletter', """CASE WHEN $data_iscrizione_newsletter IS NOT NULL AND
                                                    $data_disiscrizione_newsletter IS NULL THEN TRUE
                                                    WHEN $data_disiscrizione_newsletter IS NOT NULL THEN FALSE ELSE NULL END""",
                                                    dtype='B', name_long='Iscr.newsletter')
        

        tbl.formulaColumn('rsociale_upper', 'UPPER($ragione_sociale)', name_long='Ragione Sociale Maiuscolo')
        tbl.formulaColumn('etichetta', "$rsociale_upper ||' - '|| $zona", name_long='Etichetta')

        tbl.formulaColumn('n_fatture',select=dict(table='fatt.fattura',
                                                  columns='COUNT(*)',
                                                  where='$cliente_id=#THIS.id'),
                                      dtype='L',name_long='N.Fatture')

        tbl.formulaColumn('tot_fatturato',select=dict(table='fatt.fattura',
                                                  columns='SUM($totale_fattura)',
                                                  where='$cliente_id=#THIS.id'),
                                      dtype='N',name_long='Tot.Fatturato')
        tbl.formulaColumn('fatt_avg', """(CASE WHEN $n_fatture >0 
                                                    THEN $tot_fatturato / $n_fatture 
                                               ELSE  0 END)""", dtype='N', name_long='Fatt.medio')
        tbl.aliasColumn('provincia_nome', relation_path='@provincia.nome', name_long='Nome provincia')
        tbl.aliasColumn('regione_sigla', relation_path='@provincia.regione', name_long='Sigla regione')
        tbl.aliasColumn('regione_nome', relation_path='@provincia.@regione.nome', name_long='Regione')
        tbl.aliasColumn('zona', relation_path='@provincia.@regione.zona', name_long='Zona')

        tbl.pyColumn('tpl_dati_cliente', name_long='Dati cliente', py_method='templateColumn', template_name='cliente_row')