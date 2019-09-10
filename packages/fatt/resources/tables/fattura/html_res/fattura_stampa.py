#!/usr/bin/env python
# encoding: utf-8

from gnr.web.gnrbaseclasses import TableScriptToHtml


class Main(TableScriptToHtml):
    maintable = 'fatt.fattura'

    doc_header_height = 35
    doc_footer_height = 15 
    grid_header_height = 4.3

    def gridQueryParameters(self):
        return dict(relation='@righe')

    def gridStruct(self,struct):
        r = struct.view().rows()
        r.fieldcell('prodotto_id',mm_width=0, name='Prodotto')
        r.fieldcell('quantita',mm_width=10)
        r.fieldcell('prezzo_unitario',mm_width=20)
        r.fieldcell('aliquota_iva',mm_width=20)
        r.fieldcell('prezzo_totale',mm_width=20)
        r.fieldcell('iva',mm_width=20)

    def gridLayoutParameters(self):
        return dict(lbl_class='intestazioni')

    def defineCustomStyles(self):
         self.body.style("""
            .intestazioni{
                background:whitesmoke;
                color:gray;
                font-size:8pt;
                line-height:8px;
                text-align:center;
            }
            .datiTestata{
                font-size:12pt;
                line-height:10px;
                text-align:right;
                padding:2mm;
            }
        

            """)
        

    def docHeader(self, header):
        layout = header.layout(name='doc_header',um='mm',
                                   top=0,bottom=0,left=0,right=0,
                                   lbl_height=3,
                                   border_width=0)
        row = layout.row()
        self.datiFattura(row.cell(width=80).layout('dati_fattura',top=1,left=1, right=1,bottom=1,border_width=0,  lbl_class='intestazioni',
                                   content_class='datiTestata',))
        row.cell()
        self.datiCliente( row.cell(width=50).layout('dati_cliente',top=1,left=1,right=1,bottom=1,border_width=0,  lbl_class='intestazioni',
                                   content_class='datiTestata',))

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

    def docFooter(self,footer, lastPage=None):
        l = footer.layout('totali_fattura',top=1,left=1,right=1,bottom=1,
                                    border_width=.3,border_color='silver',
                                    lbl_class='intestazioni',
                                    content_class='datiTestata')
        r = l.row()
        r.cell()
        r.cell(self.field('totale_imponibile',format=self.currencyFormat),lbl='Imponibile',  width=30)
        r.cell(self.field('totale_iva',format=self.currencyFormat),lbl='IVA',  width=30)
        r.cell(self.field('totale_fattura',format=self.currencyFormat),lbl='Totale',  width=30)
