# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('agente_tipo', pkey='codice', name_long='Tipo agente', name_plural='Tipi agente',
                        caption_field='descrizione',lookup=True)
        self.sysFields(tbl,id=False)
        tbl.column('codice', size=':10', name_long='Codice')
        tbl.column('descrizione', size=':40', name_long='Descrizione')
