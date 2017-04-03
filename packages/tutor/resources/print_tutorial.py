#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method
from gnr.core.gnrbag import Bag
from gnr.core.gnrhtml import GnrHtmlBuilder

class PrintTutorial(BaseComponent):
    print_table = None
    record_mode = False
    py_requires = 'gnrcomponents/source_viewer/source_viewer'
    source_viewer_rebuild = False

    def main(self,root,**kwargs):
        root.attributes['overflow'] = 'hidden'
        frame = root.framePane(frameCode='print_tutorial',datapath='main')
        bar = frame.top.slotToolbar('5,vtitle,2,selector,*,reload,100',vtitle='Print Tester',height='20px')
        if self.print_table and self.record_mode:
            fb = bar.selector.formbuilder(cols=1,border_spacing='3px')
            fb.dbSelect(value='^.record_id',dbtable=self.print_table,lbl='Record %s' %self._(self.db.table(self.print_table).name_long))
        else:
            bar.selector.div()
        bar.reload.slotButton('Make',action='FIRE .run;')
        center = frame.center.tabContainer()
        bar.dataRpc(None,self.print_tutorial_content,
                        rpc_record_id='^.record_id',
                        _onResult="""
                            SET .htmlsource = result.getItem('htmlsource');
                            SET .pdfsrc = result.getItem('pdfsrc')+'?='+(new Date().getTime());
                        """,_fired='^.run',subscribe_rebuildPage=True)
        center.contentPane(title='HTML',overflow='hidden').codemirror(value='^.htmlsource',readOnly=True,
                        config_mode='htmlmixed',config_lineNumbers=True,height='100%')
        center.contentPane(title='PDF',overflow='hidden').iframe(src='^.pdfsrc',height='100%',width='100%',border=0)

    @public_method
    def print_tutorial_content(self,record_id=None,**kwargs):
        builder = GnrHtmlBuilder(page_height=297, page_width=21, page_margin_top=5,
                             page_margin_left=5)
        builder.initializeSrc()
        builder.styleForLayout()
        data = Bag()
        if self.print_table:
            if self.record_mode:
                if record_id:
                    data = self.db.table(self.print_table).record(pkey=record_id).output('bag')
            else:
                data = self.db.table(self.print_table).query().selection().output('records')
        self.printContent(builder.body,data=data)
        result = Bag()
        result['htmlsource'] = builder.toHtml()
        builder.toPdf(self.site.getStaticPath('page:testpdf','preview.pdf',autocreate=-1))
        result['pdfsrc'] = self.site.getStaticUrl('page:testpdf','preview.pdf')
        return result

    def printContent(self,body,data=None):
        pass

