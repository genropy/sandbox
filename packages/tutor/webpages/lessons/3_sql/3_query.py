# -*- coding: UTF-8 -*-


class GnrCustomWebPage(object):
    py_requires = 'sql_tutorial'

    def getQuery(self):
        return self.db.table('fatt.cliente').query(columns='@provincia.nome,count(*) AS num',
                                                      group_by='@provincia.nome')
