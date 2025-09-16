#!/usr/bin/env python
# encoding: utf-8
from gnr.app.gnrdbo import GnrDboTable, GnrDboPackage

class Package(GnrDboPackage):
    def config_attributes(self):
        return dict(comment='shop package',sqlschema='shop',sqlprefix=True,
                    name_short='Shop', name_long='Shop', name_full='Shop')
                    
    def config_db(self, pkg):
        pass
        
class Table(GnrDboTable):
    pass
