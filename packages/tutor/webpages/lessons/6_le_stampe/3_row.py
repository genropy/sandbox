# -*- coding: UTF-8 -*-


class GnrCustomWebPage(object):
    py_requires = 'print_tutorial'

    def printContent(self,body,data=None):
        l = body.layout(height=290,width=200,top=3,left=5,border_width=0.3)
        l.row(height=30).cell('Top')
        l.row().cell('Middle')
        l.row(height=20).cell('Bottom')