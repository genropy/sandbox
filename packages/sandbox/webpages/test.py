# -*- coding: utf-8 -*-

from gnr.core.gnrdecorator import public_method
from gnr.core.gnrbag import Bag
from datetime import datetime


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
        bc = pane.borderContainer(height='600px')
        top = bc.borderContainer(region='top', height='200px')
        top_left = top.contentPane(region='left', width='50%')
        top_center = top.contentPane(region='center')

        fb = top_center.formbuilder(cols=1, datapath='.options')
        fb.numbertextbox('^.header_height', lbl='Header height')
        fb.numbertextbox('^.column_width', lbl='Column width')
        fb.numbertextbox('^.step', lbl='Step')
        fb.checkboxtext('^.view_modes', values='Quarter Day,Half Day,Day,Week,Month', lbl='View modes')
        fb.numbertextbox('^.bar_height', lbl='Bar height')
        fb.numbertextbox('^.bar_corner_radius', lbl='Bar corner radius')
        fb.numbertextbox('^.arrow_curve', lbl='Arrow curve')
        fb.numbertextbox('^.padding', lbl='Padding')
        fb.filteringSelect('^.view_mode', values='^.view_modes', lbl='Curr View mode')
        fb.textbox('^.date_format', lbl='Date format', default='YYYY-MM-DD')
        fb.simpleTextArea('^.custom_popup_html', lbl='Custom popup HTML')
        
        grid = top_left.quickGrid(value='^.tasks')
        grid.tools('addrow,delrow')
        grid.column('id', name='ID')
        grid.column('name', name='Name')
        grid.column('start', name='Start')
        grid.column('end', name='End')
        grid.column('progress', name='Progress')
        grid.column('dependencies', name='Dependencies')
        grid.column('custom_class', name='Custom class')

        bc.ganttPane('mygantt', region='center')