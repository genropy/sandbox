# -*- coding: utf-8 -*-
import datetime

from gnr.web.gnrbaseclasses import BaseComponent

from gnr.core.gnrdecorator import public_method,metadata


class View(BaseComponent):
    css_requires='agt'

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('resource_id',width='20em')
        cs = r.columnset('start',name='!![en]From')
        cs.cell('date_start',calculated=True,dtype='D',name='!![en]Date',
                formula='ts_calc_start')
        cs.cell('time_start',calculated=True,
                        dtype='H',name='!![en]Time',
                        formula='ts_calc_start')

        r.fieldcell('ts_calc_start',width='10em',sort='a',hidden=True)
        r.fieldcell('ts_end',width='10em',hidden=True)

        cs = r.columnset('end',name='!![en]To')

        cs.cell('date_end',calculated=True,dtype='D',name='!![en]Date',formula='ts_end')
        cs.cell('time_end',calculated=True,
                        dtype='H',name='!![en]Time',
                        formula='ts_end')

        r.fieldcell('allocation_description',width='20em',name='Allocated by')


    def th_query(self):
        return dict(column='resource_id', op='contains', val='')

class ViewFromResource(View):

    def th_top_custom(self,top):
        top.bar.replaceSlots('vtitle','sections@pastfuture,10,sections@allocation')
        
    def th_sections_pastfuture(self):
        return [dict(code='past',condition='($is_allocated IS TRUE AND $ts_end<:env_workdate)',
                            caption='!![en]Past'),
            
                dict(code='future',
                    condition='($ts_end IS NULL OR $ts_end>=:env_workdate)',
                    caption='!![en]Future',isDefault=True)
                ]

    @metadata(_if='pastfuture=="future"',_if_pastfuture='^.pastfuture.current')
    def th_sections_allocation(self):
        return [dict(code='free',condition='$is_allocated IS NOT TRUE',
                            caption='!![en]Free'),
                dict(code='busy',
                    condition='$is_allocated IS TRUE',
                    caption='!![en]Busy')]

class ViewFromAllocation(View):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('resource_id',width='20em')
        cs = r.columnset('start',name='!![en]From')
        cs.cell('date_start',calculated=True,dtype='D',name='!![en]Date',
                formula='ts_calc_start')
        cs.cell('time_start',calculated=True,
                        dtype='H',name='!![en]Time',
                        formula='ts_calc_start')

        r.fieldcell('ts_calc_start',width='10em',sort='a',hidden=True)
        r.fieldcell('ts_end',width='10em',hidden=True)

        cs = r.columnset('end',name='!![en]To')

        cs.cell('date_end',calculated=True,dtype='D',name='!![en]Date',formula='ts_end')
        cs.cell('time_end',calculated=True,
                        dtype='H',name='!![en]Time',
                        formula='ts_end')

        r.fieldcell('allocation_description',width='20em',name='Allocated by')

        r.cell('allocate',calculated=True,format_buttonclass='calendar iconbox',
                    format_isbutton=True,
                    format_onclick="""var row = this.widget.rowByIndex($1.rowIndex);
                                      genro.publish('agente_tmsh_allocate',row);""",
                    cellClassCB="""var row = cell.grid.rowByIndex(inRowIndex);
                                    if(row.allocation_description){
                                        return 'hidden';
                                    }""")
    def th_top_custom(self,top):
        bar = top.bar.replaceSlots('vtitle','sections@busy,10,fballocations,*')
        fb = bar.fballocations.formbuilder(border_spacing='2px')
        fb.dbSelect(value='^#FORM.selected_resource_id',dbtable='agt.agente',hasDownArrow=True,lbl='Agente')

    
    def th_sections_busy(self):
        return [dict(code='busy',condition='$le_appuntamento_id=:env_allocation_id',caption='Occupati'),
                dict(code='free',condition='$is_allocated IS NOT TRUE AND (:resource_id IS NULL OR $resource_id=:resource_id)',
                            condition_resource_id='=#FORM.selected_resource_id',
                            caption='Liberi'),
                dict(code='all',condition='(:resource_id IS NULL OR $resource_id=:resource_id)',
                            condition_resource_id='=#FORM.selected_resource_id',
                            caption='Tutti')
                ]


class FormFromAllocation(BaseComponent):
    def th_form(self,form):
        fb = form.record.formbuilder(cols=2)
        fb.field('resource_id',colspan=2)
        fb.dateTextBox(value='^.date_start',validate_notnull=True,
                        width='7em',lbl='!![en]Start date')
        fb.timeTextBox(value='^.time_start',validate_notnull=True,
                        width='7em',lbl='!![en]Hour/Min')
        fb.dateTextBox(value='^.date_end',validate_notnull=True,
                        width='7em',lbl='!![en]End date')
        fb.timeTextBox(value='^.time_end',validate_notnull=True,
                        width='7em',lbl='!![en]Hour/Min')
            
    
    @public_method
    def th_onSaving(self, recordCluster,recordClusterAttr, resultAttr=None):
        date_start = recordCluster.pop('date_start')
        time_start = recordCluster.pop('time_start')
        date_end = recordCluster.pop('date_end')
        time_end = recordCluster.pop('time_end')
        recordCluster['ts_start'] = datetime.datetime(date_start.year,
                                date_start.month,
                                date_start.day,
                                time_start.hour,
                                time_start.minute)
        recordCluster['ts_end'] = datetime.datetime(date_end.year,
                                date_end.month,
                                date_end.day,
                                time_end.hour,
                                time_end.minute)
    def th_options(self):
        return dict(dialog_height='300px',dialog_width='400px',modal=True)
