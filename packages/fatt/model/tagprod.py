#!/usr/bin/env python
# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl = pkg.table('tagprod', pkey='codice', name_long='!!Tag prodotto', 
                    name_plural='!!Tag prodotto',caption_field='codice',lookup=True)
        tbl.column('codice',size = ':20', name_long = '!!Codice')
        tbl.column('descrizione',size = ':40', name_long = '!!Descrizione')
        tbl.column('colore',size = ':30', name_long = '!!Colore',
                    cell_edit=dict(tag='ColorTextBox',mode='rgba'))
        tbl.formulaColumn('box',""":spanbox||$colore||';">'||$codice||'</span>'""",
                            var_spanbox=""" <span style="background-color:""")
