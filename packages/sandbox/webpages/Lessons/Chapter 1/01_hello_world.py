# -*- coding: UTF-8 -*-
            
class GnrCustomWebPage(object):
    dojo_source=True
    def main(self,root,**kwargs):
        root.div('Hello world')
        root.div('ciao')