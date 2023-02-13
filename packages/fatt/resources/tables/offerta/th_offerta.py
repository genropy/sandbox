# -*- coding: utf-8 -*-

# th_staff.py
# Created by Saverio Porcari on 2011-04-10.
# Copyright (c) 2011 Softwell. All rights reserved.
import datetime
from dateutil import rrule
from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method,metadata,customizable


class View(BaseComponent):
    def th_options(self):
        return dict(excludeDraft=False,addrow=self.db.table('fatt.offerta_tipo').getMenuTipi())

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('offerta_tipo', name='Tipo ', width='15em')      
        r.fieldcell('protocollo', name='Ordine', width='10em')
        r.fieldcell('data_protocollo', name='Data', width='10em')
        r.fieldcell('@cliente_id.ragione_sociale',width='30em',name='Cliente')

                               
    def th_order(self):
        return 'protocollo:d'

    def th_query(self):
        return dict(column='data_protocollo',op='equal', val='questo mese',runOnStart=True)  

    def th_queryBySample(self):
        return dict(fields=[dict(field='data_protocollo',lbl='Data',width='7em'),
                            dict(field='protocollo', lbl='Protocollo',width='10em'),
                            dict(field='@cliente_id.ragione_sociale', lbl='Cliente')],
                            cols=3,isDefault=True)


    def th_top_fatt(self,top):
        top.slotToolbar('5,sections@archiviazione,*',childname='upper')

    @metadata(isMain=True)
    def th_sections_archiviazione(self):
        return [dict(code='bozze',caption='!![it]Bozze',
                        condition='$__is_draft IS TRUE',
                        includeDraft=True),
                dict(code='protocollati',caption="!![it]Confermati"),] 


class Form(BaseComponent):  
    py_requires="""proxies/offerta/proxy_offerta:Offerta AS offerta,
                   gnrcomponents/attachmanager/attachmanager:AttachManager"""
    def th_form(self, form,**kwargs):
        form.store.handler('load',default_data_protocollo='=gnr.workdate')
        bc = form.center.borderContainer()
        self.offerta.testata(bc.borderContainer(region='top',height='250px',datapath='.record'))        
        self.offerta.tabCentrale(bc.tabContainer(region='center',margin='2px'))

    def th_top_custom_trasf(self,top):
        bar = top.bar.replaceSlots('left_placeholder','draft,10,left_placeholder')
        box = bar.draft.div()
        box.dataFormula('#FORM.offertaInDraft','__is_draft',__is_draft='=#FORM.record.__is_draft',_fired='^#FORM.controller.loaded')
        box.div(hidden='^#FORM.offertaInDraft?=!#v').checkbox(value='^.record.__is_draft',label='!![it]Bozza')
        box_nodraft = box.div(hidden='^#FORM.offertaInDraft')
        btn = box_nodraft.button('Riporta a bozza',fire='.riporta_a_bozza',
                    disabled='^#FORM.controller.changed',parentForm=True)
        btn.dataRpc(self.db.table('fatt.offerta').riportaABozza,
                    offerta_id='=#FORM.record.id',
                    _lockScreen=True,
                    _onResult='this.form.reload();')
        box_nodraft.span('&nbsp;')

    @public_method
    def th_onSaving(self, recordCluster, recordClusterAttr, resultAttr):
        righe_offerta = None
        if not recordCluster['__is_draft']:
            righe_offerta = recordCluster.pop('_righe_documento')
        return dict(righe_offerta=righe_offerta)

    @public_method
    def th_onSaved(self, record, resultAttr,righe_offerta=None,**kwargs):
        if not record['__is_draft']:
            self.db.table('fatt.offerta').aggiornaRigheOfferta(record,righe_offerta)

    @public_method
    def th_onLoading(self, record, newrecord, loadingParameters, recInfo):
        if not newrecord and not record['__is_draft']:
            _righe_documento = self.db.table('fatt.offerta').righeDocumento(offerta_id=record['id'])
            record.setItem('_righe_documento', _righe_documento, _sendback=True)


    def th_options(self):
        return dict(form_add=self.db.table('fatt.offerta_tipo').getMenuTipi(),printMenu=True)
