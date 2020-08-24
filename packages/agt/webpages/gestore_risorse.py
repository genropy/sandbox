# -*- coding: utf-8 -*-
from gnr.core.gnrbag import Bag
class GnrCustomWebPage(object):
    py_requires = 'public:Public,gnrcomponents/timesheet_viewer/timesheet_viewer:TimesheetViewer'

    def main(self, root, **kwargs):       
        pblroot = root.rootBorderContainer(title='Gestione appuntamenti', datapath='main',design='sidebar')
        self.tmshResourceManager(pblroot,resource_tbl='agt.agente')

    def tmshResourceManager(self,pane,resource_tbl=None):
        pane.dataRpc('.slots',self.getCalendario,_onStart=True,_fired='^.rebuild_slots')
       #pane.dataController("""frm.load({destPkey:appuntamento_id})""",
       #                frm=self.formAppuntamento.js_form,
       #                subscribe_modifica_appuntamento=True)
       #pane.dataController("""frm.newrecord({calendario_id:calendario_id,tipo_appuntamento:'APP'})""",
       #                frm=self.formAppuntamento.js_form,
       #                subscribe_nuovo_appuntamento=True)
        frame = pane.timesheetViewer(region='center',value='^.slots',
                                slotFiller='timetable',work_start=8,work_end=22,
                                slot_duration=20)
       #pane.onDbChanges("""FIRE .rebuild_slots""", 
       #                        table=resource_tbl',
       #                        frame=frame)

    
    def getCalendario(self):
        return Bag()
       