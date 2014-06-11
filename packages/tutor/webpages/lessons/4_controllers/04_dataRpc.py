# -*- coding: UTF-8 -*-
            
class GnrCustomWebPage(object):
    
    def main(self,root,**kwargs):
        pane=root.div(datapath='test',width='650px',margin='20px',
                                border='1px solid gray')
        
        self.dataformula_1(pane)
        pane=root.div(datapath='test',width='650px',margin='20px',
                                border='1px solid gray')
        self.dataformula_2(pane)
        
    def dataformula_1(self, pane):
        fb=pane.formbuilder(cols=3,fld_width='100px',datapath='.onetriangle')
        fb.numberTextBox(value='^.t_base',lbl='Triangle base')
        fb.numberTextBox(value='^.t_height',lbl='Triangle height')
        fb.div('^.t_area',lbl='Triangle area',_class='fakeTextBox',text_align='right')
        fb.dataFormula('.t_area','tb*ta/2',tb='^.t_base',ta='^.t_height')
        
    def dataformula_2(self, pane):
        fb=pane.formbuilder(cols=3,datapath='.triangles',fld_width='100px')
        for k in range(6):
            fb.numberTextBox(value='^.t_%i.t_base'%k,lbl='Triangle %i base'%k)
            fb.numberTextBox(value='^.t_%i.t_height'%k,lbl='Triangle %i height'%k)
            fb.div('^.t_%i.t_area'%k,lbl='Triangle %i area'%k,_class='fakeTextBox',text_align='right')
            fb.dataFormula('.t_%i.t_area'%k,'tb*ta/2',
                           tb='^.t_%i.t_base'%k,ta='^.t_%i.t_height'%k)
        r=pane.div(font_size='18px',margin='20px')
        r.span('Area Total:')
        r.span('^.total',lbl='Total Area',padding_left='10px')
        pane.dataFormula('.total','t.sum("#v.t_area")',t='^.triangles')
                
