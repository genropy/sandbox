#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):
    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('ragione_sociale')
        #r.fieldcell('cliente_tipo_codice')
        #r.fieldcell('pagamento_tipo_codice')
        r.fieldcell('indirizzo')
        r.fieldcell('comune_id')
        r.fieldcell('provincia')
        r.fieldcell('iscritto_newsletter', semaphore=True)
        #Con semaphore=True si utilizza la visualizzazione a semaforo (ma solo a due stati) anche nella vista.
        #r.fieldcell('n_fatture')
        #r.fieldcell('tot_fatturato',format='#,###.00')


    def th_order(self):
        return 'ragione_sociale'

    def th_query(self):
        return dict(column='ragione_sociale', op='contains', val='')

    def th_sections_acquisti(self):
        return [dict(code='tutti',caption='Tutti'),
                dict(code='con_acquisti',caption='Con Acquisti',condition='$n_fatture>0'),
                dict(code='senza_acquisti',caption='Senza Acquisti',condition='$n_fatture=0')]


    def th_top_toolbarsuperiore(self,top):
        top.slotToolbar('5,sections@acquisti,*,sections@cliente_tipo_codice,5',
                        childname='superiore',_position='<bar',gradient_from='#999',gradient_to='#666')


class Form(BaseComponent):

    def th_form(self, form):
        bc = form.center.borderContainer()
        self.datiCliente(bc.roundedGroupFrame(title='Dati cliente',region='top',datapath='.record',height='185px'))
        tc = bc.tabContainer(region = 'center',margin='2px')
        self.fattureCliente(tc.contentPane(title='Fatture'))
        self.prodottiCliente(tc.contentPane(title='Prodotti Acquistati'))
        self.noteCliente(tc.contentPane(title='Note',datapath='.record'))

    def datiCliente(self,pane):
        fb = pane.div(margin_left='50px',margin_right='80px').formbuilder(cols=2, border_spacing='4px',colswidth='auto',fld_width='100%')
        fb.field('ragione_sociale',colspan=2)
        fb.field('cliente_tipo_codice',keepable=True)
        fb.field('pagamento_tipo_codice')
        fb.field('indirizzo',colspan=2)
        fb.field('provincia',keepable=True)
        fb.field('comune_id',condition='$sigla_provincia=:provincia',
                    condition_provincia='^.provincia')
        fb.field('email',validate_email=True)
        fb2 = pane.div(margin_left='50px',margin_right='80px').formbuilder(cols=3)
        fb2.field('data_iscrizione_newsletter', readOnly=True)
        fb2.field('data_disiscrizione_newsletter', readOnly=True)
        #fb2.div('^.iscritto_newsletter', lbl='Iscritto alla newsletter', _virtual_column='$iscritto_newsletter')
        #Con questo div semplice si visualizza come risultato la stringa testuale "true" o "false"
        #fb2.checkbox('^.iscritto_newsletter', lbl='Iscritto alla newsletter', _virtual_column='$iscritto_newsletter')
        #Con la checkbox si visualizza la casella di testo, ma non si distingue lo status "null" dal "false", inoltre stimola il clic
        #fb2.div('^.iscritto_newsletter', lbl='Iscritto alla newsletter', _virtual_column='$iscritto_newsletter',
        #            format='semaphore', dtype='B')
        fb2.semaphore('^.iscritto_newsletter', lbl='Iscritto alla newsletter', _virtual_column='$iscritto_newsletter')
        #Il semaphore, nella sua versione estesa o compatta, è la soluzione migliore per rappresentare booleani di sola lettura con tre stati            
    
    def noteCliente(self,frame):
        frame.ckeditor(value='^.note')

    def fattureCliente(self,pane):
        pane.dialogTableHandler(relation='@fatture',
                                viewResource='ViewFromCliente')

    def prodottiCliente(self,pane):
        pane.plainTableHandler(table='fatt.prodotto',
                                condition='@righe_fattura.@fattura_id.cliente_id =:cl_id',
                                condition_cl_id='^#FORM.record.id',export=True)
    
    def th_bottom_custom(self, bottom):
        bar = bottom.slotBar('10,*,stampa_scheda,10')
        bar.stampa_scheda.button('Stampa scheda', iconClass='print',
                                    action="""genro.publish("table_script_run",{table:"fatt.cliente",
                                                                               res_type:'print',
                                                                               resource:'scheda_cliente',
                                                                               pkey: pkey})""",
                                                                               pkey='=#FORM.pkey')


    def th_options(self):
        return dict(dialog_height='550px', dialog_width='800px',selector=True)
