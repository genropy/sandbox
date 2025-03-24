#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method


class View(BaseComponent):
    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('protocollo',width='10em')
        r.fieldcell('data',width='7em')
        r.fieldcell('cliente_id',zoom=True,width='15em')
        r.fieldcell('totale_imponibile',width='7em',name='Tot.Imp')
        r.fieldcell('totale_iva',width='7em',name='Tot.Iva')
        r.fieldcell('totale_fattura',width='7em',name='Totale')

    def th_struct_bis(self,struct):
        "Vista alternativa"
        r = struct.view().rows()
        r.fieldcell('protocollo')
        r.fieldcell('cliente_id',zoom=True)
        r.fieldcell('data')

    def th_order(self):
        return 'protocollo'

    def th_query(self):
        return dict(column='protocollo', op='contains', val='')

    def th_options(self):
        return dict(view_preview_tpl='r_fatt_riga')

class ViewFromCliente(BaseComponent):
    css_requires='fatturazione'
    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('protocollo')
        r.fieldcell('data')
        r.fieldcell('totale_imponibile')
        r.fieldcell('totale_iva')
        r.fieldcell('totale_fattura')

    def th_order(self):
        return 'protocollo'

class Form(BaseComponent):
    py_requires='proxies/proxy_fattura:Fattura AS fattura'

    def th_form(self, form):
        bc = form.center.borderContainer()
        self.fattura.testata(bc,region='top',height='140px')
        self.fattura.righe(bc,region='center',
                            storepath='#FORM.record._righe_documento')

    def th_options_copypaste(self):
        return '*'

    def th_options_defaultPrompt(self):
        return dict(title='Nuova fattura',fields=self.fattura.defaultPromptFields())


    @public_method
    def th_onSaving(self, recordCluster, recordClusterAttr, resultAttr):
        righe_fattura = recordCluster.pop('_righe_documento')
        return dict(righe_fattura=righe_fattura)



    @public_method
    def th_onSaved(self, record, resultAttr,righe_fattura=None,**kwargs):
        tblrighe = self.db.table('fatt.fattura_riga')
        fattura_id = record['id']
        righe_correnti = tblrighe.query(where='$fattura_id=:fid',fid=record['id']).fetchAsDict('id')
        if righe_fattura:
            for v, pkey, newrecord in righe_fattura.digest('#v,#a._pkey,#a._newrecord'):
                if newrecord:
                    v['fattura_id'] = fattura_id
                    tblrighe.insert(v)
                else:
                    righe_correnti.pop(pkey)
                    with tblrighe.recordToUpdate(pkey=pkey) as record:
                        record.update(v)
        for v in righe_correnti.values():
            tblrighe.delete(v)
    
    @public_method
    def th_onLoading(self, record, newrecord, loadingParameters, recInfo):
        if not newrecord:
            tblrighe = self.db.table('fatt.fattura_riga')
            righe_fattura = tblrighe.query(where='$fattura_id=:fid',
                                          fid=record['id'],
                                          bagFields=True).selection().output('baglist')
            #<r1 nome='cacciavite' prezzo='11.33::N' pkey='zyoorrp'  />

            #<r1> <nome>Cacciavite</nome> <prezzo _T="N">11.33</prezzo>  <pkey>XYOOO</npkeyome> </r1>

            record.setItem('_righe_documento', righe_fattura, _sendback=True)