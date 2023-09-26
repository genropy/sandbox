#!/usr/bin/env python
# encoding: utf-8

from gnr.core.gnrdecorator import metadata

class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('movimento_tipo', pkey='codice', name_long='!![it]Tipo Movimento',
                         name_plural='!![it]Tipi movimento', caption_field='descrizione')
        self.sysFields(tbl, id=False, df=True)
        
        tbl.column('codice', size='3', name_long='Codice')
        tbl.column('descrizione', size=':50', name_long='!![it]Descrizione')
        tbl.column('verso', size='1', values='C:Carico,S:Scarico', name_long='Verso')
        tbl.column('immediato', dtype='B', name_long='Movimento immediato')

    @metadata(mandatory=True)
    def sysRecord_Inventario(self):
        return self.newrecord(codice='INV', descrizione='Inventario iniziale', verso='C', immediato=True)

    @metadata(mandatory=True)
    def sysRecord_Eliminazione(self):
        return self.newrecord(codice='ELI', descrizione='Eliminazione', verso='S', immediato=True)  

    @metadata(mandatory=True)
    def sysRecord_Acquisto(self):
        return self.newrecord(codice='ACQ', descrizione='Acquisto', verso='C') 

    @metadata(mandatory=True)
    def sysRecord_Vendita(self):
        return self.newrecord(codice='VEN', descrizione='Vendita', verso='S') 

    @metadata(mandatory=True)
    def sysRecord_TrasferimentoOut(self):
        return self.newrecord(codice='TRU', descrizione='Trasferimento in Uscita', verso='S') 

    @metadata(mandatory=True)
    def sysRecord_TrasferimentoIn(self):
        return self.newrecord(codice='TRE', descrizione='Trasferimento in Entrata', verso='C') 

    @metadata(mandatory=True)
    def sysRecord_Entrata(self):
        return self.newrecord(codice='ENT', descrizione='Entrata generica', verso='C')

    @metadata(mandatory=True)
    def sysRecord_Uscita(self):
        return self.newrecord(codice='USC', descrizione='Uscita generica', verso='S')