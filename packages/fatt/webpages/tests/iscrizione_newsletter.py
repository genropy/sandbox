# -*- coding: UTF-8 -*-
from gnr.core.gnrdecorator import public_method
from datetime import datetime

class GnrCustomWebPage(object):

    def main(self,root,**kwargs):
        fb = root.formbuilder(cols=1, margin='20px', datapath='main')
        fb.h3('Iscriviti alla newsletter')
        fb.dbselect(table='fatt.cliente', value='^.cliente_id', lbl='Cliente')
        fb.button('ISCRIVITI', action='FIRE .iscriviti')
        fb.dataRpc(None, self.iscrivitiNewsletter, cliente_id='=.cliente_id', iscrizione=True, _fired='^.iscriviti')
        fb.button('DISISCRIVITI', action='FIRE .disiscriviti')
        fb.dataRpc(None, self.iscrivitiNewsletter, cliente_id='=.cliente_id', iscrizione=False, _fired='^.disiscriviti')

    @public_method
    def iscrivitiNewsletter(self, cliente_id=None, iscrizione=None):
        tbl_cliente = self.db.table('fatt.cliente')
        cliente_rec = tbl_cliente.record(where='$id=:cliente', cliente=cliente_id, for_update=True).output('bag')
        if iscrizione is True: 
            cliente_rec['data_iscrizione_newsletter'] = datetime.now()
        elif iscrizione is False:
            cliente_rec['data_disiscrizione_newsletter'] = datetime.now()
        tbl_cliente.update(cliente_rec)
        self.db.commit()