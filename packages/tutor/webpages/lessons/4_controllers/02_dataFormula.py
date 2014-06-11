# -*- coding: UTF-8 -*-

            
class GnrCustomWebPage(object):
    
    def main(self,root,**kwargs):
        
        self.personalBalance(root.div(margin='15px'))
        
    def personalBalance(self,pane):
        pane.h1('Personal Balance')
        box=pane.div(datapath='sheet', width='700px',
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
        
        fb.dataFormula('.home_total','home_exp.sum()',home_exp='^.home_detail')
        fb.numberTextBox('^.home_total',lbl='Total Home Expenses')
        fb.numberTextBox('^.balance',lbl='Balance',
                         color="==value>0?'green':'red'")
        fb.dataFormula('.balance','income-home_total',
                       income='^.income',
                       home_total='^.home_total')

        
 
        
        
        
        
        
        
        


        
   
