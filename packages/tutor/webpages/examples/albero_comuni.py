# -*- coding: UTF-8 -*-
from gnr.core.gnrdecorator import public_method,extract_kwargs
from gnr.core.gnrbag import Bag

class GnrCustomWebPage(object):
    def source_viewer_open(self):
        return False
        
    def main(self,root,**kwargs):
        tblnuts = self.db.table('glbl.nuts')
        b = Bag()
        root_id = tblnuts.readColumns(columns='$id',where='$code=:c',c='IT')
        z = tblnuts.query(condition='$hierarchical_pkey LIKE :p%%',p=root_id).fetch()
        print x
        root.div('Albero comuni')
