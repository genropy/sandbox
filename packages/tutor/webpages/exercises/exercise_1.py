# -*- coding: UTF-8 -*-
"""The first example of Genropy page"""
class GnrCustomWebPage(object):
    def main(self, root, **kwargs):
        sl = root.slotBar('x,y,blur,color,inset,*,test1,*',
                          lbl_font_size='10px',lbl_width='12px',
                          lbl_position='L',lbl_transform_rotate='-90',lbl_color='teal',
                          cell_border='1px dotted gray',datapath='test')
        sl.x.verticalSlider(value='^.x',minimum=-30,maximum=30,intermediateChanges=True,
                            height='100px',lbl='X')
        sl.y.verticalSlider(value='^.y',minimum=-30,maximum=30,intermediateChanges=True,
                            height='100px',lbl='Y')
        sl.blur.verticalSlider(value='^.blur',minimum=-30,maximum=30,intermediateChanges=True,
                               height='100px',lbl='blur')
        sl.color.comboBox(value='^.color',width='90px',lbl='color',
                          values="""aqua,black,blue,fuchsia,gray,green,lime,maroon,navy,olive,purple,red,silver,teal,white,yellow""")
        sl.inset.checkbox(value='^.inset',label='shadow_inset')
        sl.test1.div(margin='5px',display='inline-block',border='1px solid gray',
                     width='100px', height='80px',shadow='3px 3px 5px gray inset',
                     shadow_x='^.x',shadow_y='^.y',shadow_blur='^.blur',
                     shadow_color='^.color',shadow_inset='^.inset')