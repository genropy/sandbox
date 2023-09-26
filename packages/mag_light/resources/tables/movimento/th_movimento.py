#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import customizable, metadata
class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('protocollo')
        r.fieldcell('movimento_tipo')
        r.fieldcell('deposito_codice', width='10em')
        r.fieldcell('data')
        r.fieldcell('status')
        r.fieldcell('data_conferma')
        r.fieldcell('confermato_da')
        r.fieldcell('note')

    def th_order(self):
        return 'data:d'

    def th_query(self):
        return dict(column='data', op='contains', val='questo mese')

    def th_options(self):
        return dict(partitioned=True, virtualStore=False)

    @metadata(isMain=True)
    def th_sections_statoMovimento(self):
        return [dict(code='in_arrivo', caption='!![it]In Arrivo',condition="$verso='C' AND $in_attesa IS TRUE"),
                dict(code='arrivati',caption='!![it]Arrivati',condition="$verso='C' AND $in_attesa IS NOT TRUE"),
                dict(code='in_uscita',caption='!![it]In Uscita',condition="$verso='S' AND $in_attesa IS TRUE"),
                dict(code='ritirati',caption='!![it]Ritirati',condition="$verso='S' AND $in_attesa IS NOT TRUE"),
                dict(code='tutti', caption='!![it]Tutti')]
    
    def th_top_custom(self,top):
        top.slotToolbar('10,sections@statoMovimento,*', childname='upper')

class ViewFromTipoMovimento(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('protocollo')
        r.fieldcell('movimento_tipo')
        r.fieldcell('deposito_codice', width='10em')
        r.fieldcell('data')
        r.fieldcell('status')
        r.fieldcell('note')

    def th_order(self):
        return 'data:d'

    def th_options(self):
        return dict(addrow=False, delrow=False, virtualStore=True)

class Form(BaseComponent):
    py_requires="gnrcomponents/dynamicform/dynamicform:DynamicForm"

    def th_form(self, form):
        bc = form.center.borderContainer()
        self.movimentoTestata(bc.borderContainer(region='top', datapath='.record', height='150px'))
        self.movimentoRighe(bc.contentPane(region='center'))

    @customizable
    def movimentoTestata(self,bc):
        left = bc.borderContainer(region='left', width='50%')
        dati_mov = left.roundedGroup(title='Dati movimento', region='left', width='50%')
        dati_mov.templateChunk(table='mag_light.movimento', record_id='^#FORM.record.id', 
                                    template='dati_movimento', margin='5px')
        note = left.contentPane(region='center').roundedGroupFrame(title='Note')
        note.simpleTextArea(value='^.record.note', editor=True, speech=True)
        center = bc.borderContainer(region='center')
        altri_dati = center.roundedGroup(region='left', title='Altri dati', width='50%') 
        fb = altri_dati.formbuilder(cols=2, border_spacing='4px', padding='10px 10px 0 10px', margin='0 10px -10px 0')
        fb.field('numero_vettura', hidden="^#FORM.record.movimento_tipo?=#v!='TRU'")
        fb.field('rif_ordine', hidden="^#FORM.record.movimento_tipo?=#v!='ACQ'")
        fb.field('causale_eliminazione', hidden="^#FORM.record.movimento_tipo?=#v!='ELI'")
        fb.field('rif_vendita', hidden="^#FORM.record.movimento_tipo?=#v!='VEN'")      
        
        if self.getPreference('campi_dinamici_magazzino', pkg='mag_light'):
            altri_dati.dynamicFieldsPane('campi_aggiuntivi')
        
        campi_aggiuntivi = center.contentPane(region='center')
        self.datiAggiuntivi(campi_aggiuntivi)

    def datiAggiuntivi(self, campi_aggiuntivi):
        """Spazio libero da customizzare nell'istanza con dati aggiuntivi specifici"""
        pass

    def movimentoRighe(self,pane):
        pane.dialogTableHandler(relation='@movimento_righe', viewResource='ViewFromMovimento')

    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px', duplicate=True)

    @customizable
    def th_top_custom(self,top):
        bar = top.bar
        bar.replaceSlots('navigation','navigation,10,consegnato,5,azioni')

        bar.consegnato.button('^.etichetta', action="PUBLISH consegnato = {movimento_id:movimento_id}", 
                            movimento_id='=#FORM.record.id', disabled='^#FORM.record.in_attesa?=!#v')
        bar.consegnato.dataController("""if (verso=='C'){var etichetta = 'Conferma Carico'}
                                         else {var etichetta = 'Conferma Scarico'}
                                         SET .etichetta = etichetta""",
                                         verso="^#FORM.record.verso")

        trasferimento_fields=[dict(name='deposito_codice', table='mag_light.deposito', lbl='Deposito', tag='dbselect')] 
        bar.azioni.button('!![it]Genera trasferimento',  
                            action="PUBLISH trasferimento = {movimento_id:movimento_id,deposito_codice:deposito_codice}", 
                            movimento_id='=#FORM.record.id', deposito_codice='=.deposito_codice',
                            hidden='^#FORM.record.movimento_tipo?=#v!="TRU"',
                            disabled='^#FORM.record.@movimento.id',
                            ask=dict(title='Genera trasferimento',fields=trasferimento_fields, dlg_width='320px'))

        top.dataRpc(None,self.db.table('mag_light.movimento').confermaMovimento, 
                        subscribe_consegnato=True, _onResult='this.form.reload();')

        top.dataRpc(None,self.db.table('mag_light.movimento').creaTrasferimento, 
                        subscribe_trasferimento=True, _onResult='this.form.reload();')
        
        return bar
        
    def th_options(self):
        return dict(dialog_windowRatio=.7, 
                    defaultPrompt=dict(title='Nuovo movimento', fields=self.newRecParameters(),
                    doSave=True))

    def newRecParameters(self):
        return [dict(value='^.movimento_verso', values='C:Carico,S:Scarico', lbl='Verso Movimento',
                    validate_notnull=True, tag='filteringselect', hasDownArrow=True),
                dict(value='^.movimento_tipo', table='mag_light.movimento_tipo', lbl='Tipo Movimento',
                    condition="$verso=:mov_v AND $codice!='TRE'", condition_mov_v='=.movimento_verso',
                    validate_notnull=True, tag='dbselect', hasDownArrow=True)]