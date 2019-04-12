#!/usr/bin/env python
# encoding: utf-8
from gnr.app.gnrdbo import GnrDboTable, GnrDboPackage

class Package(GnrDboPackage):
    def config_attributes(self):
        return dict(comment='sandbox package',sqlschema='sabdbox',
                    name_short='Sandbox', name_long='Genropy Sandbox', name_full='Sandbox')
                    
    def config_db(self, pkg):
        pass
               
class Table(GnrDboTable):
    pass



class WebPage(object):
    package_py_requires = 'gnrcomponents/source_viewer/source_viewer:SourceViewer,gnrcomponents/doc_handler/doc_handler:DocHandler'

    def mainWrapper(self,rootwdg,**kwargs):
        if self.isDeveloper():
            self.main(rootwdg, **kwargs)
            return
        try:
            self.main(rootwdg, **kwargs)
        except Exception,e:
            rootwdg._nodes = []
            rootwdg.h1('Wrong main %s' %str(e))

    def source_viewer_open(self):
        return self._call_kwargs.get('_source_viewer') is not None
    
    def source_viewer_customroot(self,root):
        if not self._call_kwargs.get('_source_viewer'):
            return 
        return root.value.contentPane(region='top',
                       height='50%',overflow='hidden',
                       splitter=True,border_bottom='1px solid #efefef')