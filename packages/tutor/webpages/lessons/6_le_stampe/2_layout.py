# -*- coding: UTF-8 -*-


class GnrCustomWebPage(object):
    py_requires = 'print_tutorial'

    def printContent(self,body,data=None):
        l = body.layout(height=200,width=250,top=3,left=5
                    ,border_width=0.3)
        l.row().cell()
        l.row().cell()
        l.row().cell()