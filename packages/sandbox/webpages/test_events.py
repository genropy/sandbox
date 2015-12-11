# -*- coding: UTF-8 -*-


class GnrCustomWebPage(object):
    def main(self,root,**kwargs):
        fb = root.formbuilder(cols=1,border_spacing='3px',datapath='test',_class='selectable')
        fb.div('aaa',lbl='Test',onCreated="""
                                 console.log(this)
                                 window.addEventListener("keypress",function(evt){
                                        genro.bp(true)
                                    });
                                
                                 """)
        fb.div('^.output',lbl='Output')
