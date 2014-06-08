# -*- coding: UTF-8 -*-
            
class GnrCustomWebPage(object):
    
    def main(self,root,**kwargs):
        
        client_list = [{'name':'John Brown','location':'London'},
                       {'name':'Mary Bartlet','location':'Brighton'},
                       {'name':'Frank Wing','location':'Denver'},
                       {'name':'Jean Morans','location':'Boston'}
                      ]
        
        client_pane = root.div(datapath='clients',
                      margin='30px',width='500px',
                               padding='15px',
                               background='#2A7ACC',
                               rounded=10)
        
        for k,client in enumerate(client_list):
            self.clientRow(client_pane,k,client)

    def clientRow(self, pane, k, client):
        identifier='c%i' % k
        
        row=pane.div(datapath='.%s' % identifier,
                        margin_bottom='20px',padding='8px',rounded=10,
                        background='white')
        
        self.setClientData(row, name=client['name'],
                                location=client['location'])
    
        row.div(identifier, font_size='18px')
        row_content = row.div(border='1px solid silver')
        self.editClientData(row_content)
        self.showClientData(row_content)
        
        
    def editClientData(self,pane):
        box=pane.div(display='inline-block', 
                     width='250px',padding='5px',
                     border_right='1px solid silver')
        self.labelDiv(box,'Name').input('^.name')
        self.labelDiv(box,'Location').input('^.location')
   
    def showClientData(self,pane):
        box=pane.div(display='inline-block',font_size='18px',
                     margin_left='30px', padding='5px')
        box.div('^.name')
        box.div('^.location')
        
    def labelDiv(self,pane,label):
        row = pane.div(margin_top='3px')
        row.span('%s: ' % label,font_sixe='9px', font_weight='bold')
        return row

    def setClientData(self, pane, name=None, location=None):
        pane.data('.name',name)
        pane.data('.location',location)
    

