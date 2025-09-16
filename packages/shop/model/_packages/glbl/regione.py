# encoding: utf-8


class Table(object):
    def config_db(self, pkg):
        tbl =  pkg.table('regione')
        tbl.attributes.update(multidb='*')
