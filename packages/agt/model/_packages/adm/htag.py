# encoding: utf-8
from gnr.core.gnrdecorator import metadata

class Table(object):
    @metadata(mandatory=True)
    def sysRecord_monomandatario(self):
        return self.newrecord(code='mono',description='Mononomandatario',
                                hierarchical_code='mono')
