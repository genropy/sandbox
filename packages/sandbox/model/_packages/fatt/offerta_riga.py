# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('offerta_riga')
        tbl.column('is_veneto', dtype='B', name_long='Is veneto')        