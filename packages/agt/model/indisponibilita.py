# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('indisponibilita', pkey='id', name_long='Indisponibilità', 
                        name_plural='Indisponibilità',caption_field='ragione')
        self.sysFields(tbl)
        tbl.column('ragione', name_long='Ragione')
