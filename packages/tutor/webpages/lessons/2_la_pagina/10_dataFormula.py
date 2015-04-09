# -*- coding: UTF-8 -*-

from random import randint as rn
from gnr.core.gnrdecorator import public_method

class GnrCustomWebPage(object):
    
    def main(self,root,**kwargs):
        
        self.triangleArea(root.div(margin='15px',datapath='triangle'))
        
        self.colorMaker(root.div(margin='15px',datapath='colormaker'))
        self.personalBalance(root.div(margin='15px',datapath='balance'))
        
        
    def triangleArea(self,pane):
        
        pane.h1('Triangle Area')
        box=pane.div(width='500px',border='1px solid gray')
        fb = box.formbuilder(cols=3,fld_width='80px')
        fb.numberTextBox('^.base',lbl='Base',default_value=0)
        fb.numberTextBox('^.height',lbl='Height',default_value=0)
        fb.div('^.area',lbl='Area',_class='fakeTextBox',text_align='right')
        fb.div('^.areaserver',lbl='Area server',_class='fakeTextBox',text_align='right')
  
        fb.dataFormula('.area','b*h/2',b='^.base',h='^.height')
        fb.dataRpc('.areaserver',self.areaTriangolo,b='^.base',h='^.height')
        
    @public_method
    def areaTriangolo(self,b=None,h=None):
        print 'calcolo',b,h
        return (b or 0) * (h or 0) / 2
    
    
    def colorMaker(self,pane):
        
        pane.h1('Color Maker')
        box=pane.div(width='500px',border='1px solid gray')
        fb = box.formbuilder(cols=4,lblpos='T',lblalign='center',
                       lbl_font_weight='bold')
        
        self.colorRgb(fb.div(datapath='.bkg',lbl='Background'))
        self.colorRgb(fb.div(datapath='.color',lbl='Color'))
        self.colorRgb(fb.div(datapath='.shadow',lbl='Shadow'))
        
        fb.div(background_color='^.bkg.rgb',font_size='30px',
               width='100px', height='100px',color='^.color.rgb',
               shadow_color='^.shadow.rgb',margin='13px',rounded=8,
               shadow='6px 6px 12px red').div('Test',padding='6px')
        
        
    def colorRgb(self,pane):
      
        fb = pane.formbuilder(cols=3,lblpos='T',lblalign='center',
                              fldalign='center',border=1,
                             lbl_font_weight='bold')
        
        self.colorSlider(fb, value='^.red',lbl='Red')
        self.colorSlider(fb, value='^.green',lbl='Green')
        self.colorSlider(fb, value='^.blue',lbl='Blue')
        
        fb.dataFormula('.rgb',"'rgb(+'+red+','+green+','+blue+')'",
                       red='^.red',blue='^.blue',green='^.green',
                       _onStart=True)

    def colorSlider(self,fb,value=None,lbl=None):
        fb.verticalSlider(value,lbl=lbl[0],height='100px',
                          minimium=0,maximum=255,default_value=rn(0,255),
                          discreteValues=256,
                          lbl_background=lbl,
                          lbl_color='white',
                          lbl_padding='1px',
                          lbl_width='15px',
                          intermediateChanges=True)
        
        
    def personalBalance(self,pane):
        pane.h1('Personal Balance')
        box=pane.div(width='500px',
                      border='1px solid gray')

        fb = box.formbuilder(cols=1)
        fb.numberTextBox('^.income',lbl='Income')
        
        home_box=fb.div(border='1px solid silver',lbl='Home expenses')
        fb_home=home_box.formbuilder(cols=1,datapath='.home_detail',
                               fld_width='80px')
        fb_home.numberTextBox('^.rent',lbl='Rent')
        fb_home.numberTextBox('^.electricity',lbl='Electricity')
        fb_home.numberTextBox('^.internet',lbl='Internet')
        fb_home.numberTextBox('^.cleaning',lbl='Cleaning')
        fb_home.numberTextBox('^.insurance',lbl='Insurance')
        
        fb.dataFormula('.home_total','home_exp.sum()',
                             home_exp='^.home_detail')
        
        fb.div('^.home_total',lbl='Total Home Expenses',
                _class='fakeTextBox',text_align='right')
        fb.div('^.balance',lbl='Balance',
                 color='^.balance_color',font_weight='bold',
                _class='fakeTextBox',text_align='right')
        
        fb.dataFormula('.balance','income-home_total',
                       income='^.income',
                       home_total='^.home_total')
        
        fb.dataFormula('.balance_color',
                       "(balance>100)?'green':'blue'",
                        balance='^.balance',
                       _if='balance>0', _else="'red'")
