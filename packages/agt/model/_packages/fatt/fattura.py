class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('fattura', partition_agente_id='agente_id')
        tbl.column('agente_id', size='22',name_long='!![it]Agente', 
                    name_short='!![it]Agente', 
                    batch_assign=True,
                    plugToForm = dict(readOnly=True),
                    validate_notnull=True).relation('agt.agente.id',
                                                    relation_name='fatture',
                                                    mode='foreignkey',
                                                    onDelete='setnull')
        tbl.column('provvigione_fatt', dtype='percent', name_long='!![it]Provvigione fattura')
        tbl.formulaColumn('provv_calc', 'COALESCE($provvigione_fatt, @cliente_id.provvigione_cliente, @agente_id.provvigione_base)', name_long='Provv.')
        tbl.formulaColumn('importo_agente', '($provv_calc/100*$totale_fattura)', dtype='money',name_long='Imp.Agente')


    def onLoading_agente(self, record, newrecord, loadingParameters, recInfo):
        if newrecord:
            record['agente_id'] = record['@cliente_id.agente_id'] or self.db.currentEnv.get('current_agente_id')