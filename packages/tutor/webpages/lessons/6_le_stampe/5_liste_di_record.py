# -*- coding: UTF-8 -*-


class GnrCustomWebPage(object):
    py_requires = 'print_tutorial'
    print_table = 'glbl.regione' 

    def printContent(self,body,data=None):
        l = body.layout(height=280,width=200,top=5,left=5,border=0)
        top = l.row(height=30)
        center = l.row().cell().layout(top=3,left=3,
                                       right=3,bottom=3,border=0,
                                      cell_border=False,row_border=False)
        top.cell(width=50)
        top.cell().h1("Regioni d'Italia")
        top.cell(width=50)
        r = center.row(height=10)
        r.cell('Sigla',width=20,border_right=0)
        r.cell('Nome',border_right=0)
        r.cell('Zona',width=30)
        for record in data:
            r = center.row(height=10)
            r.cell(record['sigla'],width=20,border_right=0,border_top=0)
            r.cell(record['nome'],border_right=0,border_top=0)
            r.cell(record['zona'],width=30,border_top=0)
        r = center.row()
        r.cell(width=20,border_right=0,border_top=0)
        r.cell(border_right=0,border_top=0)
        r.cell(width=30,border_top=0)