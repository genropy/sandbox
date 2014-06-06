# -*- coding: UTF-8 -*-
            
class GnrCustomWebPage(object):
    
    def main(self,root,**kwargs):
        self.setClientData(root)
        self.showClientData(root)
        
    def showClientData(self,pane):
        box=pane.div(margin='20px',font_size='14px',color='#888')
        box.div('Client Data',font_size='18px',margin_bottom='10px')
        r=box.div()
        r.span('Name: ')
        r.span('=client.name')
        r=box.div()
        r.span('Location: ')
        r.span('=client.location')
        r=box.div()
        r.span('Age: ')
        r.span('=client.age')
        
    def setClientData(self,pane):
        pane.data('client.name','John Brown')
        pane.data('client.location','London')
        pane.data('client.age',33)
        
