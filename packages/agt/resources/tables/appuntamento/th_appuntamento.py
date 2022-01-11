#!/usr/bin/python3
# -*- coding: utf-8 -*-
import datetime
from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('dtstart')
        r.fieldcell('dtend')
        r.fieldcell('cliente_id')
        r.fieldcell('descrizione')
        

    def th_order(self):
        return 'dtstart'

    def th_query(self):
        return dict(column='cliente_id', op='contains', val='')
    

class Form(BaseComponent):
    css_requires='agt'
    def th_form(self, form):
        bc = form.center.borderContainer()
        fb = bc.contentPane(region='top').formbuilder(cols=2, border_spacing='4px',datapath='.record')
        fb.field('cliente_id',colspan=2)
        fb.field('descrizione',colspan=2)
        fb.dateTextBox(value='^.date_start',validate_notnull=True,
                        width='7em',lbl='!![en]Start date')
        fb.timeTextBox(value='^.time_start',validate_notnull=True,
                        width='7em',lbl='!![en]Hour/Min')
        fb.dateTextBox(value='^.date_end',validate_notnull=True,
                        width='7em',lbl='!![en]End date')
        fb.timeTextBox(value='^.time_end',validate_notnull=True,
                        width='7em',lbl='!![en]Hour/Min')

        bc.contentPane(region='center').plainTableHandler(
            viewResource='ViewFromAllocation',
            formResource='FormFromAllocation',
            table='agt.agente_tmsh',
            delrow=True,
            view_store_dbenv_allocation_id='^#FORM.record.id',
            view_store_dbenv_dtstart='=#FORM.record.dtstart',
            view_store_dbenv_dtend='=#FORM.record.dtend',
            view_store_sel_agente='^#FORM.selected_resource_id',
            grid_rowCustomClassesCb="""function(row){
                                    if(row.allocation_description){
                                        return 'allocated';
                                    }
                                }"""
        )
        self.dialogAllocaRisorsa(bc)
    
    def dialogAllocaRisorsa(self,pane):
        dlg = pane.dialog(title='Assegna',closable=True)
        pane.dataController("""
                var pars = new gnr.GnrBag({date_start:date_start,date_end:date_end,
                                        time_end:time_end,time_start:time_start,
                                        allocation_id:allocation_id,pkey:_pkey});
                SET .alloca_risorsa = pars;
                dlg.show();
                
                """, 
                dlg=dlg.js_widget,date_start='=#FORM.record.date_start',
                date_end='=#FORM.record.date_end',
                time_end='=#FORM.record.time_end',
                time_start='=#FORM.record.time_start',
                allocation_id='=#FORM.record.id',
                subscribe_agente_tmsh_allocate=True)
        frame = dlg.framePane(height='300px',width='400px')
        fb = frame.formbuilder(cols=2,datapath='.alloca_risorsa')
        fb.dateTextBox(value='^.date_start',validate_notnull=True,
                        width='7em',lbl='!![en]Start date')
        fb.timeTextBox(value='^.time_start',validate_notnull=True,
                        width='7em',lbl='!![en]Hour/Min')
        fb.dateTextBox(value='^.date_end',validate_notnull=True,
                        width='7em',lbl='!![en]End date')
        fb.timeTextBox(value='^.time_end',validate_notnull=True,
                        width='7em',lbl='!![en]Hour/Min')
        fb.dataController('this.setRelativeData(".ts_start",combineDateAndTime(d,t),{dtype:"DHZ"});',
                            d='^.date_start',t='^.time_start',_if='d&&t')
        fb.dataController('this.setRelativeData(".ts_end",combineDateAndTime(d,t),{dtype:"DHZ"});',
                        d='^.date_end',t='^.time_end',_if='d&&t')

        bar = frame.bottom.slotBar('*,confirm,2',_class='slotbar_dialog_footer')
        bar.confirm.slotButton('Assegna',fire='.alloca')
        bar.dataRpc(None,self.allocaRisorsa,allocazione='=.alloca_risorsa',_fired='^.alloca')

    @public_method
    def allocaRisorsa(self,allocazione=None,**kwargs):
        tt = self.db.table('agt.agente_tmsh')
  
        with tt.recordToUpdate(allocazione['pkey']) as rec:
            rec['le_appuntamento_id'] = allocazione['allocation_id']
            rec['ts_start'] = allocazione['ts_start']
            rec['ts_end'] = allocazione['ts_end']
        self.db.commit()


    @public_method
    def th_onLoading(self, record, newrecord, loadingParameters, recInfo):
        dtstart,dtend = record['dtstart'],record['dtend']
        if dtstart:
            record.setItem('date_start', dtstart.date(),_sendback=True)
            record.setItem('time_start',dtstart.time(),_sendback=True)
        if dtend:
            record.setItem('date_end', dtend.date(),_sendback=True)
            record.setItem('time_end',dtend.time(),_sendback=True)
    
    @public_method
    def th_onSaving(self, recordCluster,recordClusterAttr, resultAttr=None):
        recordCluster['dtstart'] = datetime.datetime(recordCluster['date_start'].year,
                                recordCluster['date_start'].month,
                                recordCluster['date_start'].day,
                                recordCluster['time_start'].hour,
                                recordCluster['time_start'].minute)
        recordCluster['dtend'] = datetime.datetime(recordCluster['date_end'].year,
                                recordCluster['date_end'].month,
                                recordCluster['date_end'].day,
                                recordCluster['time_end'].hour,
                                recordCluster['time_end'].minute)

    def th_options(self):
        return dict(dialog_parentRatio=.8)
