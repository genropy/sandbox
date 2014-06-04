# -*- coding: UTF-8 -*-

from random import randint as rn
            
class GnrCustomWebPage(object):    
    def main(self,root,**kwargs):
        root.div('We use now some HTML elements',margin='10px',
                      font_size='24px',text_align='center',
                      color='#444') 
        #we receive a root and we add a div with a content and
        #some attributes.
        
        mybox=root.div(height='150px',width='400px',margin='auto',
                         padding='10px',
                         border='1px solid gray',rounded='10',
                         margin_top='50px',shadow='4px 4px 8px #666') 
        #we add now to the root a div that has not a content, 
        #just attributes.
        #this div is in a python variable named 'mybox'
        #we can now put some elements in container
                         
        for j in range(96):
            mybox.div(height='15px',width='15px',shadow='2px 2px 3px #666',
                      background_color='rgb(%i,%i,%i)'%(rn(0,255),rn(0,255),rn(0,255)),
                      rounded='10',float='left',margin='5px')
        
        mytable=root.table(margin='auto',margin_top='50px',
                           border_spacing=0,border_collapse='collapse')
        tbody=mytable.tbody(font_size='10px',color='gray')
        for r in range (10):
            row=tbody.tr()
            for c in range (10):
                row.td(padding='2px').div('cell<br/>%i-%i'%(r,c),
                                          padding_right='6px',padding_left='6px',
                         rounded=4,border='1px solid gray')
