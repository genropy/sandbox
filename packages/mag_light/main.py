#!/usr/bin/env python
# encoding: utf-8
from gnr.app.gnrdbo import GnrDboTable, GnrDboPackage

class Package(GnrDboPackage):
    def config_attributes(self):
        return dict(comment='mag light package',sqlschema='mag_light',
                    name_short='Mag', name_long='Magazzino Light', name_full='Gestione Magazzino')
                    
    def custom_type_money(self):
        return dict(dtype='N',format='#,###.00')
        
    def config_db(self, pkg):
        pass

class Table(GnrDboTable):
    pass
