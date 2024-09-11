# encoding: utf-8


class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('scaglione',name_long='Scaglione',name_plural='Scaglioni',pkey='id',caption_field='caption')
        self.sysFields(tbl)
        tbl.column('da', dtype='N')
        tbl.column('a', dtype='N')
        tbl.column('ordine', dtype='I')
        
        tbl.formulaColumn('caption', """
                          COALESCE('DA: '||$da,'')||COALESCE(' A: '||$a,'')""", dtype='T')