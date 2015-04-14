# -*- coding: UTF-8 -*-


class GnrCustomWebPage(object):
    py_requires = 'print_tutorial'

    def printContent(self,body,data=None):
        l = body.layout(height=280,width=200,top=5,left=5,border=0)
        l.row(height=30)
        l.row()