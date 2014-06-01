#!/usr/bin/env python
# encoding: utf-8
from gnr.app.gnrdbo import GnrDboTable, GnrDboPackage

class Package(GnrDboPackage):
    def config_attributes(self):
        return dict(comment='sandbox package',sqlschema='tutor',
                    name_short='Tutor', name_long='Tutor', name_full='Tutor')
                    
    def config_db(self, pkg):
        pass
        
class Table(GnrDboTable):
    pass

class WebPage(object):
    package_py_requires = 'gnrcomponents/source_viewer/source_viewer:SourceViewer'