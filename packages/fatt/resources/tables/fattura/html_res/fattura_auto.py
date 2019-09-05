#!/usr/bin/env python
# encoding: utf-8

from gnr.web.gnrbaseclasses import TableScriptToHtml

class Main(TableScriptToHtml):
    maintable = 'fatt.fattura'
   
    row_table = 'fatt.fattura_riga'
    row_viewResource ='th_fattura_riga:ViewFromFattura'

    #rows_relation = '@righe' 

    #rows_resource = ''
    #rows_columns = "$pippo,$pluto"

    doc_header_height = 35
    doc_footer_height = 32 
    grid_header_height = 4.3
    grid_footer_height = 0
    
    #grid_columns= [dict(name='Prodotto',   mm_width=0,field='@prodotto_id.descrizione'),
    #               dict(name=u'Quantità', mm_width=20, field='quantita'),
    #               dict(name='Pr.Unitario', mm_width=20, field='prezzo_unitario', dtype='N'),
    #               dict(name='Pr.Totale', mm_width=20, field='prezzo_totale', dtype='N'),
    #               dict(name='Aliquota', mm_width=20, field='aliquota_iva', dtype='N', format=currencyFormat),
    #               dict(name='IVA', mm_width=20, field='iva', dtype='N', format=currencyFormat)]
#

    #hook method.
    #header is a cell item
    def docHeader(self, header):
        layout = header.layout(name='doc_header',um='mm',
                                   top=0,bottom=0,left=0,right=0,
                                   lbl_height=3,
                                   border_width=0)
        row = layout.row()
        self.datiFattura(row.cell(width=80).layout('dati_fattura',top=1,left=1, right=1,bottom=1,border_width=0))
        row.cell()
        self.datiCliente( row.cell(width=50).layout('dati_cliente',top=1,left=1,right=1,bottom=1,border_width=0))

    def datiFattura(self,layout):
        r1 = layout.row(height=8)
        r1.cell('N.Fattura')
        r1.cell(self.field('protocollo'))
        r2 = layout.row(height=8)
        r2.cell('Data Fattura')
        r2.cell(self.field('data'))
        layout.row()

    def datiCliente(self,layout):
        layout.row(height=5).cell('Spett.')
        layout.row(height=5).cell(self.field('@cliente_id.ragione_sociale'))
        layout.row(height=5).cell(self.field('@cliente_id.indirizzo'))
        layout.row(height=5).cell('%s (%s)' %(self.field('@cliente_id.@comune_id.denominazione'),self.field('@cliente_id.provincia')))
        layout.row()

    def mainLayout(self, page):
        return page.layout('principale',top=1,left=1,right=1,bottom=1,border_width=0)

    def gridLayout(self, body):
        # hook method obbligatorio per le stampe con griglia inclusa
        # here you receive the body (the center of the page) and you can define the layout that contains the grid
        return body.layout(name='rowsL',um='mm',border_color='gray',
                            top=1,bottom=1,left=1,right=1,
                            border_width=.3,lbl_class='caption',
                            style='text-align:left;font-size:10pt')

    def onRecordLoaded(self):
        query = self.db.table(self.row_table).query(columns=self.grid_sqlcolumns, where='$fattura_id=:fid', 
                                                             fid=self.record['id'])
        self.setData(self.rows_path, query.selection().output('grid'))