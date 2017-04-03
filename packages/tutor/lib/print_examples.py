from gnr.core.gnrhtml import GnrHtmlBuilder
from random import randint
from gnr.app.gnrapp import GnrApp


def example_0(body):
    body.layout(height=200,width=200,top=5,left=5,border_width=0.2)

def example_1(body):
    #con due righe
    l = body.layout(height=200,width=200,top=5,left=5,border_width=0.3)
    l.row(height=30).cell('Top')    
    l.row(height=20).cell('Bottom')

def example_2(body):
    #con numero casuale di righe in mezzo

    l = body.layout(height=240,width=200,top=5,left=5,border_width=0.2)
    l.row(height=30).cell('Top')
    
    n_rows=randint(2,9)
    for i in range(n_rows):
        l.row().cell('Middle: %i' %i)
        
    l.row(height=20).cell('Bottom')

def example_3(body):
    l = body.layout(height=200,width=200,top=5,left=5,
        border_width=0.3,
        border_color='grey',
        border_style='solid')

    for i in range(1,5):
        r = l.row()
        for j in range(1,5):
            r.cell(content='Row %i Cell %i' % (i,j))
        
def example_4(body):
    body.style(""".mycontent{text-align: center;
                             margin-top:20mm;
                             font-style:italic;
                             font-size:14pt;}
                   .mylabel{text-align: left;
                             font-style:bold;
                             font-size:9pt;
                             background-color:navy;
                             color:white;
                             padding:2mm;}""")

    l = body.layout(height=200,width=200,top=5,left=5,
        border_width=0.3,
        border_color='grey',
        border_style='solid', 
        content_class='mycontent', lbl_class='mylabel', lbl_heigth=10)

    for i in range(1,5):
        r = l.row()
        for j in range(1,5):
            r.cell(content='Cell %i' % j, lbl='Row %i ' %i)

def example_5(body):
    body.style(""".mycontent{text-align: center;
                             margin-top:20mm;
                             font-style:italic;
                             font-size:14pt;}
                   .mylabel{text-align: left;
                             font-style:bold;
                             font-size:9pt;
                             background-color:navy;
                             color:white;
                             padding:2mm;}
                    .small_content{font-size:9pt;
                                   text-align: left;
                                   text-indent:2mm;
                                   margin-top:10mm;}
                    .innerlabel{
                            text-align: center;
                             font-style:bold;
                             font-size:7pt;
                             background-color:red;
                             color:white;
                             padding:2mm;
                    }""")

    l = body.layout(height=200,width=200,top=5,left=5,
        border_width=0.3,
        border_color='grey',
        border_style='solid', 
        content_class='mycontent',
        lbl_class='mylabel', lbl_heigth=10)

    first_row = l.row(height=80)
    first_row.cell('Big content', lbl='Big cell')

    inner_layout = first_row.cell().layout(content_class='small_content', lbl_class='innerlabel')
    for i in range(1,5):
        r = inner_layout.row()
        r.cell('Sub cell %i' %i, lbl='Code')
        r.cell(randint(10,50), lbl='Price')

def example_6(body):

    sandbox_app = GnrApp('sandbox')
    glbl_table = sandbox_app.db.table('glbl.provincia')
    province = glbl_table.query().fetch()

    l = body.layout(width=200,top=5,left=5,
        border_width=0.3,
        border_color='grey',
        border_style='solid')
    
    headers_row = l.row(height=10)
    headers_row.cell('Sigla', width=20, style='text-align:center; font-weight:bold;')
    headers_row.cell('Nome', style='text-indent:10mm; font-weight:bold;')

    for pr in province:
        r = l.row(height=10)
        r.cell(pr['sigla'], width=20, style='text-align:center;')
        r.cell(pr['nome'],  style='text-indent:10mm;')

if __name__ == '__main__':
    builder = GnrHtmlBuilder(page_height=297, page_width=21, page_margin_top=5,
                             page_margin_left=5)
    builder.initializeSrc()
    builder.styleForLayout()

    example_1(builder.body)

    builder.toHtml('/Users/saverioporcari/esempi_stampa/example.html')

