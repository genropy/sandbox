#!/usr/bin/env python
# encoding: utf-8
from gnr.app.gnrdbo import GnrDboTable, GnrDboPackage

class Package(GnrDboPackage):
    def config_attributes(self):
        return dict(comment='agt package',sqlschema='agt',sqlprefix=True,
                    name_short='Agt', name_long='Agenti', name_full='Agt')
                    
    def config_db(self, pkg):
        pass
        
    def custom_type_money(self):
        return dict(dtype='N',format='#,###.00')

    def custom_type_percent(self):
        return dict(dtype='N',format='##.00')


class Table(GnrDboTable):
    
    pass
