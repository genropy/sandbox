# -*- coding: UTF-8 -*-
            
class GnrCustomWebPage(object):
    
    def main(self,root,**kwargs):
        self.setClientData(root)
        self.showClientData(root)
        
        
    def showClientData(self,pane):
        
        box=pane.div(margin='20px',font_size='14px',color='#888')
        box.div('Fixed Data',font_size='18px',margin_bottom='10px')
        self.setRow(box,'Name','=client.name')
        self.setRow(box,'Location','=client.location')
        self.setRow(box,'Age','=client.age')
        
        box=pane.div(margin='20px',font_size='14px')
        box.div('Variable Data',font_size='18px',
                 margin_bottom='10px',color='red')
        self.setRow(box,'Name','^client.name')
        self.setRow(box,'Location','^client.location')
        self.setRow(box,'Age','^client.age')

        
    def setRow(self,pane,label,path):
        pars=dict(label=label,path=path)
        ondblclick="""var curr_value=this.getRelativeData('%(path)s');
                   var new_value=prompt('%(label)s',curr_value);
                   genro.setRelativeData('%(path)s',new_value)""" % pars
        
        r=pane.div(margin_top='4px')
        r.span('%(label)s: '%pars)
        r.span(path, connect_ondblclick=ondblclick)
        
        
    def setClientData(self,pane):
        pane.data('client.name','John Brown')
        pane.data('client.location','London')
        pane.data('client.age',33)
        
 
