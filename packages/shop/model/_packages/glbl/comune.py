# encoding: utf-8


class Table(object):
    def config_db(self, pkg):
        tbl =  pkg.table('comune')
        tbl.attributes.update(multidb='*')
