# -*- coding: UTF-8 -*-
"""The first example of Genropy page"""

class GnrCustomWebPage(object):
    
    def main(self,root,**kwargs):
        root.div('Edit me', font_size='64px')