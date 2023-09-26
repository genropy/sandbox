#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method
from decimal import Decimal

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('codice')
        r.fieldcell('descrizione',width='20em')
        r.fieldcell('prodotto_marca', width='8em')
        r.fieldcell('prezzo_unitario')
        r.fieldcell('materiale_consumo', semaphore=True, name='Consum.')
        depositi = self.db.table('mag_light.deposito').query().fetch()
        for deposito in depositi:
            dep = deposito['codice']
            cset = r.columnset(dep, name=dep)
            cset.cell('quantita_disponibile_{dep}'.format(dep=dep), dtype='L', name='Giacenza', width='5em')
            cset.cell('quantita_attesa_{dep}'.format(dep=dep), dtype='L',name='Q.Attesa', width='5em')

    def th_order(self):
        return 'codice'

    def th_query(self):
        return dict(column='codice', op='contains', val='')

class Form(BaseComponent):
    py_requires="""gnrcomponents/dynamicform/dynamicform:DynamicForm,
                   gnrcomponents/attachmanager/attachmanager:AttachManager"""

    def th_form(self, form):
        bc = form.center.borderContainer()
        self.datiProdotto(bc.borderContainer(region='top',datapath='.record',height='180px'))
        tc = bc.tabContainer(region='center',margin='2px')
        if self.getPreference('campi_dinamici_magazzino', pkg='mag_light'):
            self.caratteristicheProdotto(tc.contentPane(title='Caratteristiche',datapath='.record'))
        self.movimentiProdotto(tc.contentPane(title='Movimenti'))
        self.allegatiProdotto(tc.contentPane(title='Allegati'))

    def allegatiProdotto(self,pane):
        pane.attachmentMultiButtonFrame()

    def caratteristicheProdotto(self,pane):
        pane.dynamicFieldsPane('caratteristiche')

    def datiProdotto(self,bc):
        left = bc.roundedGroup(region='center',title='Dati prodotto').div(margin='10px',margin_right='20px')
        fb = left.formbuilder(cols=3, border_spacing='4px',colswidth='auto',fld_width='100%',width='900px')
        fb.field('prodotto_tipo_id',tag='hdbselect',validate_notnull=True)
        fb.field('codice',validate_notnull=True,validate_case='U',validate_nodup=True)
        fb.field('prezzo_unitario')
        fb.field('descrizione',validate_notnull=True,colspan=2)
        fb.field('prodotto_marca') 
        fb.field('note', tag='simpleTextArea', colspan=2)
        fb.field('materiale_consumo')
        center = bc.roundedGroup(region='right',title='Immagine',width='130px')
        center.img(src='^.foto_url',crop_height='100px',crop_width='100px',margin='5px',
                    crop_border='2px dotted silver',crop_rounded=6,edit=True,
                    placeholder=True,upload_folder='site:prodotti/immagini',
                    upload_filename='=#FORM.record.codice')

    def movimentiProdotto(self,pane):
        pane.plainTableHandler(relation='@ordini', viewResource='ViewFromProdotto')

    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px', duplicate=True)

class FormFromMovimentoRiga(BaseComponent):
    py_requires="gnrcomponents/dynamicform/dynamicform:DynamicForm"
    
    def th_form(self, form):
        bc = form.center.borderContainer(datapath='.record')
        fb = bc.borderContainer(region='top', height='180px').formbuilder(cols=1, border_spacing='4px')
        fb.field('prodotto_tipo_id',tag='hdbselect',validate_notnull=True)
        fb.field('codice',validate_notnull=True,validate_case='U',validate_nodup=True)
        fb.field('prezzo_unitario')
        fb.field('prodotto_marca') 
        fb.field('descrizione',validate_notnull=True)
        fb.field('note', tag='simpleTextArea')
        fb.field('materiale_consumo')
        if self.getPreference('campi_dinamici_magazzino', pkg='mag_light'):
            bc.borderContainer(region='center').dynamicFieldsPane('caratteristiche')