#!/usr/bin/python3
# -*- coding: utf-8 -*-

import dateutil
from gnr.core.gnrbag import Bag
from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('cognome_nome', width='20em')
        r.fieldcell('codice', width='7em')
        r.fieldcell('tipo_codice', width='7em')
        r.fieldcell('partita_iva', width='13em')
        r.fieldcell('provvigione_base', width='6em', name='Provv')
        r.fieldcell('user_id',  width='8em')
        r.fieldcell('regioni',  width='20em')

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
        self.schedaFatture(tc.contentPane(title='Fatture'))
        self.schedaOrari(tc.contentPane(title='Orari'))

        self.schedaAppuntamenti(tc.contentPane(title='Appuntamenti'))

    def topPane(self, bc):
        pane = bc.contentPane(region='center')
        fb = pane.div(margin_right='10px').formbuilder(cols=2, border_spacing='4px', colswidth='auto', fld_width='100%', width='100%')
        fb.field('cognome')
        fb.field('nome' )
        fb.field('partita_iva', colspan=2)
        fb.field('email', colspan=2)
        fb.field('codice' , width='10em')
        fb.field('provvigione_base', width='5em')
        fb.field('tipo_codice' , width='20em')
        fb.field('regioni', popup=True, colspan=2, tag='checkboxtext', table='glbl.regione', cols=3)
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
        pane.plainTableHandler(relation='@fatture',viewResource='ViewFromAgente')

    def schedaOrari(self,pane):
        bc = pane.borderContainer()
        top = bc.contentPane(region='top', height='50%')
        bottom = bc.contentPane(region='center')

        timerules_th = top.dialogTableHandler(relation='@timerules',
                                viewResource='ViewFromResource',
                                condition='$is_exception IS NOT TRUE',
                                margin='2px',pbl_classes=True,
                                grid_multiSelect=False,grid_selfDragRows=True) # 540px
        timerules_th.form.store.handler('load',default_rule_order ='=#FORM/parent.view.store?totalrows')

                                
        exception_th = bottom.dialogTableHandler(relation='@timerules',
                                datapath='.exceptions',
                                formResource='ExceptionForm',
                                viewResource='ExceptionView',
                                condition='$is_exception IS TRUE',
                                dialog_height='280px',
                                dialog_width='600px', # 540px
                                dialog_title='Exceptions',
                                title='Exceptions',
                                margin='2px',pbl_classes=True,
                                grid_multiSelect=False,grid_selfDragRows=True)

        exception_th.form.store.handler('load',default_is_exception=True,
                                        default_rule_order ='=#FORM/parent.view.store?totalrows')

    def schedaAppuntamenti(self,pane):
        pane.plainTableHandler(relation='@tmsh_items',delrow=True,viewResource='ViewFromResource')

    #def calendario(self,pane):
    #    pane.dataRpc('#FORM.calendar',self.getTimesheetBag,_onStart=True,_fired='^.rebuild_calendar')
    #   #pane.dataController("""frm.load({destPkey:appuntamento_id})""",
    #   #                frm=self.formAppuntamento.js_form,
    #   #                subscribe_modifica_appuntamento=True)
    #   #pane.dataController("""frm.newrecord({calendar_id:calendar_id,tipo_appuntamento:'APP'})""",
    #   #                frm=self.formAppuntamento.js_form,
    #   #                subscribe_nuovo_appuntamento=True)
    #    frame = pane.timesheetViewer(region='center',value='^#FORM.calendar',
    #                           # selfsubscribe_edit_timesheet="""
    #                           # PUBLISH nuovo_appuntamento = {calendar_id:$1.calendar_id};
    #                           # """,
    #                            #selfsubscribe_edit_slot="PUBLISH modifica_appuntamento = {appuntamento_id:$1.appuntamento_id}",
    #                            slotFiller='timetable',work_start=8,work_end=22,
    #                            slot_duration=20)
    #    pane.onDbChanges("""FIRE #FORM.rebuild_calendar""", 
    #                            table='agt.agente_tmsh',
    #                            frame=frame)
#
    #
    #@public_method
    #def getTimesheetBag(self,resource_id=None):
    #    tmsh = self.db.table('agt.agente_tmsh')
    #    #tblapp = self.db.table('barber.appuntamento')
    #    calendario = tmsh.query(where='$ts_start>=:env_workdate',
    #                columns="""$id,$staff_id,$slots,$ora_inizio,$ora_fine,$data,$barber,@staff_id.colore AS background""",
    #                            order_by='$data').fetch()
    #    barber_cols = sorted(list(set([r['barber'] for r in calendario])))
    #    barber_colors = dict([(r['barber'],r['background']) for r in calendario])
#
    #    result = Bag()
    #    appuntamenti = self.db.table('barber.appuntamento').query(where='$data>=:env_workdate',
    #                                                             columns="""$id,$cognome,$nome,$telefono,
    #                                                             $ora_inizio,$ora_fine,
    #                                                             $prestazioni_prenotate,$calendario_id,
    #                                                             $colore""",order_by='$ora_inizio').fetchGrouped('calendario_id')
    #    tpl = """<div style="font-size:.9em;">$nome $cognome<br><i>$prestazioni_prenotate</i></div>"""
#
    #    for cal_day in calendario:
    #        daylabel = self.toText(cal_day['data'],format='yyyy_MM_dd')
    #        calcontent = result.getItem(daylabel)
    #        if calcontent is None:
    #            calcontent = Bag()
    #            for barber in barber_cols:
    #                calcontent.setItem(barber,Bag(),name=barber,background=barber_colors[barber])
    #            result.setItem(daylabel,calcontent,day=cal_day['data'])
    #        appuntamentiNode = calcontent.getNode(cal_day['barber'])
    #        appuntamentiNode.attr.update(time_start=cal_day['ora_inizio'],
    #                                 time_end=cal_day['ora_fine'],
    #                                  calendario_id=cal_day['id'])
    #        cal_appuntamenti = appuntamenti.get(cal_day['id'],[])
    #        val = appuntamentiNode.value
    #        for r in cal_appuntamenti:
    #            val.setItem(self.toText(r['ora_inizio'],format='HH_mm'),
    #                                            None,time_start=r['ora_inizio'],
    #                                            time_end=r['ora_fine'],
    #                                            appuntamento_id=r['id'],
    #                                            background_color=r['colore'],
    #                                            template=tpl,nome=r['nome'],
    #                                            cognome=r['cognome'],
    #                                            prestazioni_prenotate=r['prestazioni_prenotate'])
    #    return result,dict(channels=barber_cols,colors=barber_colors)
    
    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )
