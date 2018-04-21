# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('provincia',name_plural='Province italiane')
        tbl.column('tariffa_spedizione', dtype='N', 
                    name_long='!!Tariffa spedizione',
                    plugToForm=dict(validate_notnull=True))
        