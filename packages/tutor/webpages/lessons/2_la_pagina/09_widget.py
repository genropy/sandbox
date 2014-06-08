# -*- coding: UTF-8 -*-
            
class GnrCustomWebPage(object):
    
    def main(self,root,**kwargs):
        weekdays='1:Monday,2:Tuesday,3:Wednesday,4:Thursday,5:Friday,6:Saturday,7:Sunday'

        pane=root.div(width='700px',datapath='widgets',
                      background='white',border='1px solid silver',
                      margin='30px')
        fb = pane.div(margin='10px').formbuilder(cols=2,lbl_font_weight='bold',
                                                 fld_width='100%')
        fb.textBox('^.textvalue',lbl='TextBox')
        fb.numberTextBox('^.numbervalue',lbl='NumberTextBox')
        fb.dateTextBox('^.datevalue',lbl='DateTextBox')
        fb.checkBox('^.boolvalue',lbl='CheckBox',label='Special')
        fb.comboBox('^.combo_value',lbl='ComboBox', 
                       values='red,green,yellow,black,white')
        fb.filteringSelect('^.filtering_value',lbl='FilteringSelect', 
                       values=weekdays)
        fb.dbselect('^.provincia',dbtable='glbl.provincia',
                   lbl='DbSelect 1')
        fb.dbselect('^.provincia',dbtable='fatt.cliente_tipo',
                   lbl='DbSelect 2',hasDownArrow=True)
        fb.checkBoxText('^.cbtext_1',values=weekdays,
                        lbl='CheckBoxText',colspan=2)
        fb.checkBoxText('^.cbtext_2',values=weekdays,
                        lbl='CheckBoxText 2',popup=True,colspan=2)
        fb.radioButtonText('^.radiobutton_txt',values=weekdays,
                        lbl='RadioButtonText',colspan=2)
        
        
   
