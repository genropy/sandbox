#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method
from gnr.core.gnrbag import Bag
from gnr.core.gnrhtml import GnrHtmlBuilder

class PrintTutorial(BaseComponent):
    py_requires = 'gnrcomponents/source_viewer/source_viewer'
    source_viewer_rebuild = False
    print_table = None
    record_mode = False

    def main(self,root,**kwargs):
        root.attributes['overflow'] = 'hidden'
        frame = root.framePane(frameCode='print_tutorial',datapath='main')
        bar = frame.top.slotToolbar('2,vtitle,2,selector,*,reload,printCurrent,2',vtitle='Print Tester',height='20px')
        if self.print_table and self.record_mode:
            fb = bar.selector.formbuilder(cols=1,border_spacing='3px')
            fb.dbSelect(value='^.record_id',dbtable=self.print_table,lbl='Record %s' %self._(self.db.table(self.print_table).name_long))
        bar.reload.slotButton('Reload',action='genro.publish("rebuildPage")')
        bar.printCurrent.slotButton('Print',action="dojo.byId('preview_iframe').contentWindow.print()")
        center = frame.center.contentPane(region='center',overflow='hidden')
        center.iframe(rpcCall=self.print_tutorial_content,height='100%',width='100%',id='preview_iframe',
                       rpc_record_id='^.record_id',
                        subscribe_rebuildPage="""this.reloadIframe(300);""",border=0)

    @public_method
    def print_tutorial_content(self,record_id=None,**kwargs):
        builder = GnrHtmlBuilder()
        builder.initializeSrc()
        data = Bag()
        if self.print_table:
            if self.record_mode:
                if record_id:
                    data = self.db.table(self.print_table).record(pkey=record_id).output('bag')
            else:
                data = self.db.table(self.print_table).query().selection().output('records')
        self.printContent(builder.body,data=data)
        return builder.toHtml()

    def printContent(self,body,record=None):
        pass

