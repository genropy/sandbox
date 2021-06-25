#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

try:
    from gnrpkg.fatt.fatture.descrittori import FattureManager, FatturaStruttura
except:
    print('FattureManager/FatturaStruttura NOT imported')


class View(BaseComponent):
    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('protocollo',width='10em')
        r.fieldcell('data',width='7em')
        r.fieldcell('cliente_id',zoom=True,width='15em')
        r.fieldcell('totale_imponibile',width='7em',name='Tot.Imp')
        r.fieldcell('totale_iva',width='7em',name='Tot.Iva')
        r.fieldcell('costo_spedizione',width='7em',name='Sped.')
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
        r.fieldcell('costo_spedizione')
        r.fieldcell('totale_iva')
        r.fieldcell('totale_fattura')

    def th_order(self):
        return 'protocollo'

class Form(BaseComponent):

    def th_form(self, form):
        bc = form.center.borderContainer()
        self.fatturaTestata(bc.borderContainer(region='top',datapath='.record',height='150px'))
        self.fatturaRighe(bc.contentPane(region='center'))

    def fatturaTestata(self,bc):
        bc.contentPane(region='center').linkerBox('cliente_id',margin='2px',openIfEmpty=True, validate_notnull=True,
                                                    columns='$ragione_sociale,$provincia,@cliente_tipo_codice.descrizione',
                                                    auxColumns='@comune_id.denominazione,$provincia',
                                                #    clientTemplate=True,
                                                    newRecordOnly=True,formResource='Form',
                                                    dialog_height='500px',dialog_width='800px')
        left = bc.roundedGroup(title='Dati fattura',region='left',width='50%')
        fb = left.formbuilder(cols=1, border_spacing='4px')
        fb.field('protocollo',readOnly=True)
        fb.field('data')
        fb.field('peso_spedizione')
        fb.field('costo_spedizione', hidden='^.peso_spedizione?=!#v')
        fb.dataRpc('^.costo_spedizione', self.leggiSpeseSpedizione, peso_spedizione='^.peso_spedizione', _userChanges=True)
        #La dataRpc scatta all'inserimento del peso di spedizione per reperire il range e il costo dalle preferenze
        
    @public_method
    def leggiSpeseSpedizione(self, peso_spedizione=None):
        spese_spedizione = self.getPreference('generali.spese_spedizione', pkg='fatt')
        if not peso_spedizione:
            return 0
        for v in spese_spedizione.values():
            if peso_spedizione >= int(v['peso_min']) and peso_spedizione < int(v['peso_max']):
                return v['costo']        

    
    def fatturaRighe(self,pane):
        pane.inlineTableHandler(relation='@righe',viewResource='ViewFromFattura',
                            picker='prodotto_id',
                            picker_structure_field='prodotto_tipo_id')

    def th_options(self):
        return dict(dialog_height='500px', dialog_width='700px')
