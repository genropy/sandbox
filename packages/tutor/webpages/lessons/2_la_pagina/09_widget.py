# -*- coding: UTF-8 -*-
            
class GnrCustomWebPage(object):
    
    def main(self,root,**kwargs):
        pane=root.div(width='700px',datapath='widgets',margin='30px')
        fb = pane.formbuilder(cols=2)
        fb.textBox('^.textvalue',lbl='TextBox')
        fb.numberTextBox('^.numbervalue',lbl='NumberTextBox')
        fb.dateTextBox('^.datevalue',lbl='DateTextBox')
        fb.checkBox('^.boolvalue',lbl='CheckBox')
        fb.comboBox('^.combo_value',lbl='ComboBox', 
                       values='red,green,yellow,black,white')
        fb.filteringSelect('^.filtering_value',lbl='FilteringSelect', 
                       values='S:Small,L:Large,XL:ExtraLage')
        
        
        
        
        
   
