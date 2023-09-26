#!/usr/bin/env python
# encoding: utf-8

class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('deposito', pkey='codice', name_long='!![it]Deposito', 
                                    name_plural='!![it]Deposito', caption_field='nome', lookup=True)
        self.sysFields(tbl, id=False)
        
        tbl.column('codice', size='3', name_long='!![it]Codice', unique=True, indexed=True,
                                validate_len='3', 
                                validate_len_error='!![it]Codice deve essere di 3 caratteri')
        tbl.column('nome', size=':50', name_long='!![it]Nome')
        

    def partitionioning_pkeys(self):
        sezione_id = self.db.currentEnv.get('current_sezione_id')
        if sezione_id:
            return [r['pkey'] for r in self.query(where='$sezione_id=:sez_id', sez_id=sezione_id).fetch()]
        else:
            return [r['pkey'] for r in self.query().fetch()]