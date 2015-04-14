# -*- coding: UTF-8 -*-


class GnrCustomWebPage(object):
    py_requires = 'print_tutorial'

    def printContent(self,body,data=None):
        l = body.layout(height=290,width=200,top=5,left=5,border=0.3)
        top = l.row(height=50)
        top_left = top.cell(width=100)
        top_center = top.cell()
        top_right = top.cell(width=40)
        center = l.row()
        bottom = l.row(height=20)
        bottom_left = bottom.cell(width=100)
        bottom_center = bottom.cell()
        bottom_right = bottom.cell(width=40)
        top_center.div('Hello world',color='red',font_size='80px',text_align='center')