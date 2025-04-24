#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method,metadata,customizable

class ViewEditable(BaseComponent):
    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('ragione_sociale', edit=True)
        r.fieldcell('indirizzo')
        r.fieldcell('comune_id')
        r.fieldcell('provincia')


class View_mobile(BaseComponent):
    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('ragione_sociale')
        

class View(BaseComponent):
    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('ragione_sociale')
        r.fieldcell('cliente_tipo_codice')
        r.fieldcell('indirizzo')
        r.fieldcell('comune_id')
        r.fieldcell('provincia')

    def th_struct_contotali(self,struct):
        "Vista con totali fattura"
        r = struct.view().rows()
        r.fieldcell('ragione_sociale')
        r.fieldcell('cliente_tipo_codice')
        r.fieldcell('pagamento_tipo_codice')
        r.fieldcell('indirizzo')
        r.fieldcell('n_fatture')
        r.fieldcell('tot_fatturato',format='#,###.00')

    def th_order(self):
        return 'ragione_sociale'

    def th_query(self):
        return dict(column='ragione_sociale', op='contains', val='')

    @metadata(variable_struct=True)
    def th_sections_acquisti(self):
        return [dict(code='tutti',caption='Tutti'),
                dict(code='con_acquisti',caption='Con Acquisti',
                        condition='$n_fatture>0',struct='contotali'),
                dict(code='senza_acquisti',caption='Senza Acquisti',condition='$n_fatture=0')]
    
    @metadata(_if='acq=="con_acquisti"',_if_acq='^.acquisti.current')
    def th_sections_volumeacquisti(self):
        return [
            dict(code='basso',condition='$tot_fatturato<:tot',caption='Basso',
                    condition_tot=5000),
            dict(code='medio',condition='$tot_fatturato>=:mintot AND $tot_fatturato<:maxtot',
                    caption='Medio',
                    condition_mintot=5000,condition_maxtot=100000),
            dict(code='grande',condition='$tot_fatturato>:maxtot',
                    caption='Alto',
                    condition_maxtot=100000) 
        ]

    def th_top_toolbarsuperiore(self,top):
        if self.isMobile:
            return
        top.slotToolbar('5,sections@acquisti,10,sections@volumeacquisti,*,sections@cliente_tipo_codice,5',
                        childname='superiore',_position='<bar',
                        gradient_from='#999',gradient_to='#666')

    def th_bottom_bottoniera(self,bottom):
        bar = bottom.slotToolbar('*,sections@iniziali,*')

    def th_options(self):
        return dict(view_preview_tpl='cliente_row')


class Form(BaseComponent):

    def th_form(self, form):
        bc = form.center.borderContainer()
        self.datiCliente(bc.roundedGroupFrame(title='Dati cliente',region='top',datapath='.record',height='200px'))
        self.clienteTabs(bc.tabContainer(region = 'center',margin='2px'))
        #self.fattureCliente(tc.contentPane(title='Fatture'))

    @customizable
    def clienteTabs(self,tc):
        self.prodottiCliente(tc.contentPane(title='Prodotti Acquistati'))
        self.noteCliente(tc.contentPane(title='Note',datapath='.record'))
        self.datiEstesi(tc.contentPane(title='Dati estesi',datapath='.record'))
    
    def datiEstesi(self,pane):
        pane.bagField(value='^.dati',
                    resource='^.cliente_tipo_codice',
                    table='fatt.cliente', 
                    remote_provincia='=.provincia')

    
    def datiCliente(self,pane):
        fb = pane.div(margin_left='50px',margin_right='80px').formbuilder(cols=2, border_spacing='4px',colswidth='auto',fld_width='100%')
        fb.field('ragione_sociale',colspan=2)
        fb.field('cliente_tipo_codice',keepable=True)
        fb.field('pagamento_tipo_codice')
        fb.field('indirizzo',colspan=2)
        fb.field('provincia',keepable=True)
        fb.field('comune_id',condition='$sigla_provincia=:provincia',
                    condition_provincia='^.provincia')
        fb.field('email',validate_email=True, colspan=2)

    def noteCliente(self,frame):
        frame.simpleTextArea(value='^.note')

    def fattureCliente(self,pane):
        pane.dialogTableHandler(relation='@fatture',
                                viewResource='ViewFromCliente')

    def prodottiCliente(self,pane):
        pane.plainTableHandler(table='fatt.prodotto',
                                condition='@righe_fattura.@fattura_id.cliente_id =:cl_id',
                                condition_cl_id='^#FORM.record.id',export=True)

    def th_options(self):
        return dict(dialog_height='650px', dialog_width='800px',selector=True)
