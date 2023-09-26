#!/usr/bin/env python
# encoding: utf-8

from gnr.core.gnrdecorator import metadata

class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('movimento_status', pkey='codice', name_long='!![it]Status Movimento',
                         name_plural='!![it]Status movimento', caption_field='descrizione', lookup=True)
        self.sysFields(tbl, id=False)
        
        tbl.column('codice', size='3', name_long='Codice')
        tbl.column('descrizione' ,size=':50',name_long='!![it]Descrizione')

    @metadata(mandatory=True)
    def sysRecord_InAttesa(self):
        return self.newrecord(codice='ATT', descrizione='In Attesa') 

    #@metadata(mandatory=True)
    #def sysRecord_Confermato(self):
    #    return self.newrecord(codice='CNF', descrizione='Confermato') 

    @metadata(mandatory=True)
    def sysRecord_Consegnato(self):
        return self.newrecord(codice='CNS', descrizione='Consegnato')     