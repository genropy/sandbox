# encoding: utf-8
from gnrpkg.multidb.storetable import StoreTable
from gnr.core.gnrbag import Bag

class Table(StoreTable):
    def config_db(self,pkg):
        tbl=pkg.table('shop', pkey='id', name_long='!![en]Shop', 
                      name_plural='!![en]Shops',caption_field='description')
        self.sysFields(tbl)
        tbl.column('denominazione',unique=True)
        tbl.column('partita_iva',unique=True)
        tbl.column('indirizzo', name_long='Indirizzo')



    def trigger_onUpdated(self,record,old_record):
        if record['startup_data_ts'] and not old_record['startup_data_ts']:
            if self.db.usingRootstore():
                with self.db.tempEnv(storename=record['dbstore']):
                    self.creaImpostazioniDiDefault(record)

    
        
    def multidb_setStartupData_whitelist(self):
        return [
            'adm.htag',
            'adm.group',
            'adm.preference',
            'adm.user',
            'adm.user_group',
            'adm.user_tag',
            'fatt.prodotto_tipo',
            'fatt.prodotto'
        ]
    
    def creaImpostazioniDiDefault(self,record):
        if self.db.usingRootstore():
            return
        self.db.application.setPreference('instance_data.owner_name', record['denominazione'],
                                          pkg='adm')
        
        servicetbl = self.db.table('sys.service')
        newservices = []
        with self.db.tempEnv(storename=False):
            storages = servicetbl.query(where='$service_type=:s AND $implementation=:imp',imp='aws_s3',s='storage',bagFields=True).fetch()
            for storage in storages:
                s = dict(storage)
                parameters = Bag(s.pop('parameters'))
                parameters['base_path'] = parameters['base_path'].replace('_main_',record['dbstore'])
                newservices.append(servicetbl.newrecord(
                    parameters=parameters,
                    **s
                ))
        for ns in newservices:
            servicetbl.insert(ns)
