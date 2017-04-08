# -*- coding: UTF-8 -*-


class GnrCustomWebPage(object):
    py_requires = 'print_tutorial'
    print_table = 'glbl.regione' 

    def printContent(self, body, data=None):
        
        l = body.layout(width=200,top=5,left=5,
                        border_width=0.3,
                         border_color='grey',
                         border_style='solid', style='line-height:7mm;')
        headers_row = l.row(height=10)
        headers_row.cell('Sigla', width=20, style='text-align:center; font-weight:bold;')
        headers_row.cell('Nome', style='text-indent:10mm; font-weight:bold;')

        for pr in data:
            r = l.row(height=8)
            r.cell(pr['sigla'], width=20, style='text-align:center;')
            r.cell(pr['nome'],  style='text-indent:10mm;')
