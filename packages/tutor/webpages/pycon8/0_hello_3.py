# -*- coding: UTF-8 -*-

class GnrCustomWebPage(object):
    def main(self,root,**kwargs):
        root.data('foo','Hello world')
        root.h1('^foo',text_align='center')
        root.textbox('^foo',margin_top='20px')
        