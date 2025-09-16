# encoding: utf-8


class Table(object):
    def config_db(self, pkg):
        tbl =  pkg.table('nazione')
        tbl.attributes.update(multidb='*')
