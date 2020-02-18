class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('cliente', 
                        partition_agente_id='agente_id')
                        #$agente_id=:env_current_agente_id
        tbl.column('agente_id', size='22',name_long='!![it]Agente', 
                    name_short='!![it]Agente', 
                    batch_assign=dict(do_trigger=True),
                    plugToForm = True).relation('agt.agente.id',
                                                    relation_name='clienti',
                                                    mode='foreignkey',
                                                    onDelete='setnull')
        tbl.column('provvigione_cliente',
                    dtype='percent', name_long='!![it]Provvigione cliente',
                    batch_assign=dict(do_trigger=True),
                    plugToForm = dict(lbl='Provvigione', width='5em'))

        tbl.formulaColumn('provv_calc', 'COALESCE($provvigione_cliente, @agente_id.provvigione_base)', name_long='Provv.')


    def defaultValues(self):
        return dict(agente_id=self.db.currentEnv.get('current_agente_id'))
