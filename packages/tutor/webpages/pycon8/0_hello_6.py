# -*- coding: UTF-8 -*-

class GnrCustomWebPage(object):
    def main(self,root,**kwargs):
        for k in range(3):
            self.sampleblock(root.div(datapath='block_%02i' %k))
        
    def sampleblock(self,pane):
        box = pane.div(border='1px solid silver',
                         margin='5px',padding='5px')
        fb = box.formbuilder(border_spacing='3px')
        fb.textbox('^.mytext',lbl='Text')
        fb.textbox('^.mycolor',lbl='Color')
        fb.textbox('^.myfontsize',lbl='Font size')
        fb.div('^.mytext',color='^.mycolor',text_align='center',
               font_size='^.myfontsize',lbl='Result')

        