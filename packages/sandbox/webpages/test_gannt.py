# -*- coding: utf-8 -*-

from gnr.core.gnrdecorator import public_method
from gnr.core.gnrbag import Bag
import datetime


class GnrCustomWebPage(object):
    py_requires = "gnrcomponents/testhandler:TestHandlerFull,gantt/gantt"
    
    #def test_0(self, pane):
    #    "Insert your test here"
    #    fb = pane.formbuilder(cols=2)
    #    fb.datetextbox('^.birthday', lbl='Your next birthday')
    #    fb.dataRpc('.days_left', self.timeLeft, birthday='^.birthday')
    # #   fb.div('^.days_left', lbl='Days left')
#
    #@public_method
    #def timeLeft(self, birthday=None):
    #    today = datetime.today().date()
    #    time_left = birthday - today
    #    print(x)
    #    return time_left

    def test_0_gantt(self, pane):
        bc = pane.borderContainer(height='800px')
        top = bc.borderContainer(region='top', height='300px')
        top_left = top.contentPane(region='left', width='50%')
        top_center = top.contentPane(region='center')
        top.data('.options',self.optionsData())
        fb = top_center.formbuilder(cols=1, datapath='.options')
        fb.numbertextbox('^.header_height', lbl='Header height')
        fb.numbertextbox('^.column_width', lbl='Column width')
        fb.numbertextbox('^.step', lbl='Step')
        fb.checkboxtext('^.view_modes', values='Quarter Day,Half Day,Day,Week,Month', 
                        lbl='View modes',popup=True)
        fb.numbertextbox('^.bar_height', lbl='Bar height')
        fb.numbertextbox('^.bar_corner_radius', lbl='Bar corner radius')
        fb.numbertextbox('^.arrow_curve', lbl='Arrow curve')
        fb.numbertextbox('^.padding', lbl='Padding')
        fb.filteringSelect('^.view_mode', values='^.view_modes', lbl='Curr View mode')
        fb.textbox('^.date_format', lbl='Date format', default='YYYY-MM-DD')
        fb.simpleTextArea('^.custom_popup_html', lbl='Custom popup HTML')
        top.data('.tasks',self.taskData())
        grid = top_left.quickGrid(value='^.tasks')
        grid.tools('addrow,delrow')
        grid.column('id', name='ID',edit=True)
        grid.column('name', name='Name',edit=True)
        grid.column('start', name='Start',edit=True,dtype='DH')
        grid.column('end', name='End',edit=True,dtype='DH')
        grid.column('progress', name='Progress',edit=True,dtype='L')
        grid.column('dependencies', name='Dependencies',edit=True)
        grid.column('custom_class', name='Custom class',edit=True)


        bc.ganttPane('mygantt', region='center',tasks='^.tasks',
                    opt_header_height='^.options.header_height',
                opt_column_width='^.options.column_width',
                opt_step='^.options.step',
                opt_view_modes='^.options.view_modes',
                opt_bar_height='^.options.bar_height',
                opt_bar_corner_radius='^.options.bar_corner_radius',
                opt_arrow_curve='^.options.arrow_curve',
                opt_padding = '^.options.padding',
                opt_view_mode = '^.options.view_mode',
                opt_date_format = '^.options.date_format',
                opt_custom_popup_html = '^.options.custom_popup_html')

    def optionsData(self):
        result = Bag(dict( {
                'header_height': 50,
                'column_width': 30,
                'step': 24,
                'view_modes': ','.join(['Quarter Day', 'Half Day', 'Day', 'Week', 'Month']),
                'bar_height': 20,
                'bar_corner_radius': 3,
                'arrow_curve': 5,
                'padding': 18,
                'view_mode': 'Day',   
                'date_format': 'YYYY-MM-DD',
                'custom_popup_html': None
            }))
        return result


    def taskData(self):
        result = Bag()
        result.addItem('r_1',Bag({
                'id': 'Task 1',
                'name': 'Redesign website',
                'start': datetime.datetime(2021,7,14,12,33),
                'end': datetime.datetime(2021,7,15,12,55),
                'progress': 20,
                'dependencies': None
        }))
        return result