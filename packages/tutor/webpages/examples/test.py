# -*- coding: UTF-8 -*-


class GnrCustomWebPage(object):
    def main(self,root,**kwargs):
        fb = root.formbuilder(cols=7,lblpos='T',
                              border_spacing='5px 2px',
                             fld_text_align='right',
                             row_border_bottom='1px solid red',
                             border_collapse='collapse',
                             fld_padding='2px',lbl_border=0)
        fb.div('Aprile 2015')
        fb.div(100,lbl='Attivo')
        fb.div(230,lbl='Passivo')
        fb.div(500,lbl='Costi')
        fb.div(630,lbl='Ricavi')
        fb.div(130,lbl='Utile')
        fb.div(9,lbl='Perdita')

        fb.div('Aprile 2014')
        fb.div(50)
        fb.div(45)
        fb.div(555)
        fb.div(99)
        fb.div(22)
        fb.div(0)
        
        