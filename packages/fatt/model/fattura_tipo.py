# encoding: utf-8
from gnr.core.gnrdecorator import metadata


class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('fattura_tipo', pkey='id', name_long='Tipo fattura', 
                    name_plural='Tipi fattura',caption_field='descrizione')
        self.sysFields(tbl)
        tbl.column('codice_contatore', size=':1', name_long='Codice contatore')
        tbl.column('descrizione', size=':40', name_long='Descrizione')
        
        #tbl.column('tipo_documento', size=':12', name_long='!![it]Tipo documento')
        tbl.column('conf_print', dtype='X', name_long='!![it]Conf.Stampa')
        tbl.column('conf_grid', dtype='X', name_long='!![it]Conf.Griglia')

    
    @metadata(mandatory=True)
    def sysRecord_STD(self):
        return self.newrecord(
            descrizione='Standard',
            codice_contatore='F'
        )