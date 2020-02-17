# encoding: utf-8

from gnr.core.gnrdecorator import metadata

class Table(object):

    @metadata(mandatory=True)  
    def sysRecord_AGT(self):
        return self.newrecord(description='Agenti',
                              code='AGT')
