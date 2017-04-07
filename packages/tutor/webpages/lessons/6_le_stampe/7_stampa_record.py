# -*- coding: UTF-8 -*-


class GnrCustomWebPage(object):
    py_requires = 'print_tutorial'
    print_table = 'fatt.cliente' 
    record_mode = True


    def printContent(self,body,data=None):
        l = body.layout(height=280,width=200,top=5,left=5,border_width=0.3)
        top = l.row(height=30)
        center = l.row().cell().layout(top=3,left=3,
                                       right=3,bottom=3,border_width=0,
                                      cell_border=False,row_border=False)
        top.cell(width=50)
        top.cell().h1(data['ragione_sociale'])
        r = top.cell(width=50).layout()
        r.row().cell(data['indirizzo'],lbl='Indirizzo')
        r.row().cell(data['@comune_id.denominazione'],lbl='Comune')
        r = center.row(height=10)
