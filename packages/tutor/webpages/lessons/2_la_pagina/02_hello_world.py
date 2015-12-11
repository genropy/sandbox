# -*- coding: UTF-8 -*-
"""The first example of Genropy page"""

class GnrCustomWebPage(object):
    
    def main(self,root,**kwargs):
        root.div('Hello python', font_size='64px',color='green')