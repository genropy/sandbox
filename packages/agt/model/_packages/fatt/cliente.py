class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('cliente', partition_agente_id='agente_id')
        tbl.column('agente_id', size='22',name_long='!![it]Agente', 
                    name_short='!![it]Agente', 
                    batch_assign=dict(do_trigger=True),
                    plugToForm = True,
                    validate_notnull=True).relation('agt.agente.id',
                                                    relation_name='clienti',
                                                    mode='foreignkey',
                                                    onDelete='setnull')
        tbl.column('provvigione_cliente',
                    dtype='percent', name_long='!![it]Provvigione cliente',
                    batch_assign=dict(do_trigger=True),
                    plugToForm = dict(lbl='Provvigione', width='5em'))

        tbl.formulaColumn('provv_calc', 'COALESCE($provvigione_cliente, @agente_id.provvigione_base)', name_long='Provv.')

    def trigger_onUpdated(self, record, old_record):
        if self.fieldsChanged('agente_id', record, old_record):
            self.db.table('fatt.fattura').batchUpdate(dict(agente_id=record['agente_id']), where='$cliente_id=:cliente_id', cliente_id=record['id'])
 
