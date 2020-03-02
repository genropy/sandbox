#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('cognome_nome', width='20em')
        r.fieldcell('codice', width='7em')
        r.fieldcell('partita_iva', width='13em')
        r.fieldcell('provvigione_base', width='6em', name='Provv')
        r.fieldcell('user_id',  width='8em')
        r.fieldcell('regioni',  width='20em',checkpref='agt.gestione_zone')

    def th_order(self):
        return 'cognome_nome'

    def th_query(self):
        return dict(column='cognome_nome', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        bc = form.center.borderContainer()
        self.topPane(bc.borderContainer(region='top', datapath='.record', height='200px'))
        tc = bc.tabContainer(region='center')
        self.schedaClienti(tc.contentPane(title='Clienti'))
        self.schedaFatture(tc.contentPane(title='Fatture',_tags='mono'))

    def topPane(self, bc):
        pane = bc.contentPane(region='center')
        fb = pane.div(margin_right='10px').formbuilder(cols=2, border_spacing='4px', colswidth='auto', fld_width='100%', width='100%')
        fb.field('cognome')
        fb.field('nome' )
        fb.field('partita_iva', colspan=2)
        fb.field('email', colspan=2)
        fb.field('codice' , width='10em')
        fb.field('provvigione_base', width='5em')
        fb.field('regioni', popup=True, colspan=2, 
                    tag='checkboxtext',checkpref='agt.gestione_zone',
                    table='glbl.regione', cols=3)
        bc.contentPane(region='right', width='500px').linkerBox('user_id',label='Informazioni Utente',formUrl='/adm/user_page',dialog_height='400px',
                        dialog_width='650px',
                        default_firstname='=#FORM.record.nome',
                        default_lastname='=#FORM.record.cognome',
                        default_email='=#FORM.record.email',
                        default_group_code = self.db.table('adm.group').sysRecord('AGT')['code'],
                        newRecordOnly=False,
                        margin='2px')

    def schedaClienti(self, pane):
        pane.plainTableHandler(relation='@clienti',viewResource='ViewFromAgente') #formResource='FormFromAgente')

    def schedaFatture(self, pane):
        pane.plainTableHandler(relation='@fatture',
                            viewResource='ViewFromAgente')

    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )
