# -*- coding: UTF-8 -*-
            
class GnrCustomWebPage(object):
    
    def main(self,root,**kwargs):
        
        block = root.div(datapath='clients')
        
        self.handleClient(block,title='Client 1', datapath='.c_1',
                          name='John Brown',
                          location='London',
                          age=33)
        
        self.handleClient(block, title='Client 2',datapath='.c_2',
                          name='Mary Bartlet',
                          location='New York',
                          age=42)
       
        self.handleClient(block,title='Client 3', datapath='.c_3',
                          name='Frank Bonzo',
                          location='Boston',
                          age=12)
        
        
       
        
        
    def handleClient(self, pane, title=None,datapath=None,
                     name=None,location=None,age=None,**kwargs):

        block=pane.div(datapath=datapath, **kwargs)
        self.setClientData(block,
                           name=name,
                           location=location,
                           age=age)
        self.showClientData(block,title=title,**kwargs)
        
    def showClientData(self,pane,title):
        box=pane.div(margin='20px',font_size='14px')
        box.div(title, font_size='18px', margin_top='10px')
        self.setRow(box,'Name','^.name')
        self.setRow(box,'Location','^.location')
        self.setRow(box,'Age','^.age')

        
    def setRow(self,pane,label,path):
        pars=dict(label=label,path=path)
        ondblclick="""var curr_value=this.getRelativeData('%(path)s');
                   var new_value=prompt('%(label)s',curr_value);
                   this.setRelativeData('%(path)s',new_value)""" % pars
        
        r=pane.div(margin_top='4px')
        r.span('%(label)s: '%pars)
        r.span(path,connect_ondblclick=ondblclick)
        
        
    def setClientData(self,pane, name=None, location=None, age=None):
        pane.data('.name',name)
        pane.data('.location',location)
        pane.data('.age',age)
        
 
