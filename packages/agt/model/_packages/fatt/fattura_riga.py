class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('fattura_riga',  partition_agente_id='agente_id')
        tbl.aliasColumn('agente_id', '@fattura_id.agente_id')