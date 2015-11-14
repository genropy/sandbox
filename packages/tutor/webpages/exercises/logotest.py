# -*- coding: UTF-8 -*-


class GnrCustomWebPage(object):
    def main(self,root,**kwargs):
        fb = root.formbuilder(cols=2,border_spacing='3px',datapath='conf')
        fb.numberTextBox(value='^.rounded',lbl='Rounded',default=3)
        fb.filteringSelect(value='^.text_transform',values='lowercase,uppercase',lbl='Transform',default='uppercase')
        fb.textbox(value='^.margin',lbl='Margin',default='1px')
        fb.textbox(value='^.color_1',lbl='Color 1',default='white')
        fb.textbox(value='^.background_1',lbl='Background 1',default='#FF3B2F')

        fb.textbox(value='^.color_2',lbl='Color 2',default='white')
        fb.textbox(value='^.background_2',lbl='Background 2',default='#025268')
        fb.horizontalSlider(value='^.zoom',minimum=0.1,maximum=3,lbl='Zoom',default=1,width='10em',intermediateChanges=True)

        parent = root.div(margin='10px',padding='10px',datapath='conf',zoom='^.zoom')
        self.creaLinea(parent,fb,'Miller',color_first='^.color_1',color_default='^.color_2',
                            background_first='^.background_1',background_default='^.background_2')
        self.creaLinea(parent,fb,'Biller',color_first='^.color_2',color_default='^.color_1',
                            background_first='^.background_2',background_default='^.background_1')

    def creaLinea(self,parent,fb,testo,color_first=None,color_default=None,
                background_first=None,background_default=None):
        box = parent.div()
        for j,l in enumerate(testo):
            background=background_default
            color = color_default
            if j==0:
                background=background_first
                color = color_first
            self.squareChar(box,l,background=background,color=color)

    def squareChar(self,pane,content,**kwargs):
        pane.div(height='50px',width='50px',display='inline-block',text_align='center',
                 margin='^.margin',rounded='^.rounded',
                 text_transform='^.text_transform',**kwargs).div(content.strip() or '&nbsp;',font_size='40px')