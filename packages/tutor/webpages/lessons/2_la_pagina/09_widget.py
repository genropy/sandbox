# -*- coding: UTF-8 -*-

            
class GnrCustomWebPage(object):
    
    def main(self,root,**kwargs):
        
        weekdays='1:Monday,2:Tuesday,3:Wednesday,4:Thursday,5:Friday,6:Saturday,7:Sunday'
        colors='DeepSkyBlue,Fuchsia,Coral,Crimson,GoldenRod,Gray,Navy,Maroon,Teal'

        pane=root.div(width='720px',datapath='widgets',
                      background='white',border='1px solid #F6F6F6',rounded='^.rounded',
                      margin='30px',shadow='1px 1px 2px #666 inset')

        fb = pane.div(margin='20px').formbuilder(cols=2,lbl_font_weight='bold',
                                                 lbl_color='^.lblcolor',
                                                 fld_width='100%')
        
        fb.textBox('^.name',lbl='Name',placeholder='John',
                     tooltip="This is a textBox")

        fb.numberTextBox('^.age',lbl='Age', placeholder='33',
                     tooltip="This is a NumberTextBox")
        
        fb.dateTextBox('^.birthday',lbl='Birthday',
                     tooltip="This is a DateTextBox and you can click on icon")
        
        fb.checkBox('^.specialstuff',label='Special',
                                   tooltip="This is a checkBox")
        
          
        fb.comboBox('^.lblcolor',lbl='Labels Color', default_value='Gray',
                    values=colors,
                    tooltip="""This is a comboBox. <br/>
                               Select a default color for labels or type a new one.""" )
        
        fb.filteringSelect('^.dayofweek',lbl='Day of week', 
                       tooltip="""FilteringSelect: you can select only an existing value.<br/>
                                  You see the description but in the store we will have the value.""",
                       values=weekdays)
                       
        fb.dbselect('^.tipo_cliente',dbtable='fatt.cliente_tipo',
                   lbl='Customer type',hasDownArrow=True,
                   tooltip="""dbSelect. Select a customer type from the menu or type in the field.""")
       
        fb.dbselect('^.town',dbtable='glbl.comune',lbl='Town',
                   auxColumns='$sigla_provincia,@sigla_provincia.@regione.nome',
                   tooltip="""dbSelect. Select a town from the menu or type in the field.""")
        
        fb.checkBoxText('^.preferred_days',values=weekdays,
                        lbl='Preferred days',colspan=2,
                    tooltip="""CheckBoxText.Select your preferred days.""")

        fb.checkBoxText('^.preferred_days',values=weekdays,
                        lbl='Preferred days',popup=True,colspan=2,
                        tooltip="""CheckBoxText.Select your preferred days in popup or type them.""")
    
        fb.radioButtonText('^.oneday',values=weekdays,
                        lbl='One Day',colspan=2,
                        tooltip="""radioButtonText.Select your preferred day.""")

        fb.horizontalSlider('^.rounded',lbl='Border Round',minimum=0,maximum=59,
                               discreteValues=60,width='160px',
                             intermediateChanges=True,
                                tooltip="""HorizontaSlider.Change the box rounded border radius.""")
        
        fb.br()
        fb.Button('Submit',action="alert(data.toXml())",
                  tooltip="""Button.Click to get the xml of the data.""",
                  data='=widgets')

        
   
