# -*- coding: UTF-8 -*-
"""The first example of Genropy page"""

class GnrCustomWebPage(object):
    def main(self,root,**kwargs):
        #1.Div semplice senza attributi
        root.div('Hello world')

        #2.Div con attributi agglomerati nello style
        root.div('Hello world', style='color:green; font-size:64px; margin:20px')

        #3.Div con attributi espliciti
        root.div('Hello world', color='green', font_size='50px', margin='50px')

        #4.Div con attributi espliciti, caso più complesso
        root.div('Hello Italy', background='red', color='white', font_size='50px', margin='50px',
                    font_weight='bold', border='6px solid green', rounded_top_right=15,
                    rounded_bottom_left=15, text_align='center', padding='4px',
                    shadow='3px 3px 6px silver')