#!/usr/bin/env python
# encoding: utf-8

class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('agente', 
                        name_long='!![it]Agente', 
                        name_plural='!![it]Agenti',
                        pkey='id', 
                        caption_field='cognome_nome')
        self.sysFields(tbl)
        tbl.column('cognome',name_long='!![it]Cognome')
        tbl.column('nome',name_long='!![it]Nome')
        tbl.column('indirizzo',name_long='!![it]Indirizzo')
        tbl.column('comune_id',name_long='!![it]Comune').relation('glbl.comune.id',relation_name='agenti')
        tbl.column('provincia',name_long='!![it]Provincia').relation('glbl.provincia.sigla',relation_name='agenti')
        tbl.column('cap',size=':5',name_long='!![it]Cap')
        tbl.column('data_nascita',dtype='D',name_long='!![it]Data di nascita')


        tbl.formulaColumn('cognome_nome',sql_formula="$cognome || ' ' || $nome")

