
class GnrCustomWebPage(object):  
    
    def main(self,root,**kwargs):        
        bc=root.borderContainer(datapath='hello') 
        bc.sharedObject('hello',shared_id='shared_helloworld',
                        autoLoad=True)
        fb=bc.contentPane(region='top').formbuilder(cols=1) 
        
        fb.textBox('^.text',lbl='Text to show')        
        fb.textBox('^.border',lbl='Border')        
        fb.textBox('^.margin',lbl='Margin')        
        fb.textBox('^.padding',lbl='Padding')        
        fb.textBox('^.color',lbl='Color')        
        fb.textBox('^.background',lbl='Background')        
        fb.textBox('^.text_align',lbl='Text Allign')        
        fb.textBox('^.font_size',lbl='Font Size')        
        fb.textBox('^.shadow',lbl='Shadow')  
        fb.textBox('^.rounded',lbl='Rounded')  
        
        bc.contentPane(region='center').div('^.text',border='^.border',
                        margin='^.margin',padding='^.padding',
                        color='^.color',background='^.background',
                       text_align='^.text_align',font_size='^.font_size',
                       shadow='^.shadow',rounded='^.rounded')