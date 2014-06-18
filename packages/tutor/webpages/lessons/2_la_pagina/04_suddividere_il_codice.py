# -*- coding: UTF-8 -*-

from random import randint as rn
            
class GnrCustomWebPage(object):  
    
    def main(self,root,**kwargs):
        
        root.div('Splitting Code', margin='10px',
                      font_size='24px', text_align='center',
                      color='#888') 
                       
        self.multicolorPane(root, howmany=96, width='400px', 
                            margin_top='50px',margin='auto',
                            shadow='4px 4px 8px #666')
        
        block = root.div(margin='auto', margin_top='50px',width='460px')
        
        for k in range(6) :              
            self.multicolorPane(block, howmany=24, width='200px', 
                            display='inline-block',margin='4px')

    def multicolorPane(self, pane, howmany=None, **box_kwargs):
        """we receive a root and we add a div with a content and
        some attributes."""
        mybox=pane.div(padding='10px',
                       border='1px solid silver',rounded='10',
                       **box_kwargs) 
        #we add now to the root a div that has not a content, 
        #just attributes.
        #this div is in a python variable named 'mybox'
        #we can now put some elements in container
                         
        for j in range(howmany):
            mybox.div(height='15px', width='15px', shadow='2px 2px 3px #666',
                      background_color=self.randomColor(),
                      rounded='10', display='inline-block', margin='5px')
    
    def randomColor(self):
        return 'rgb(%i,%i,%i)'%(rn(0,255),rn(0,255),rn(0,255))
        
   