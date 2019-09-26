#!/usr/bin/env python
# encoding: utf-8

from gnr.web.gnrbaseclasses import TableScriptToHtml


class Main(TableScriptToHtml):
    maintable = 'fatt.fattura'

    doc_header_height = 32
    doc_footer_height = 12
    grid_header_height = 5

    def defineCustomStyles(self):

        self.body.style(""".cell_label{
                            font-size:8pt;
                            text-align:left;
                            color:gray;
                            text-indent:1mm;}

                            .footer_content{
                            text-align:right;
                            margin:2mm;
                            }
                            """)
                    
    def gridQueryParameters(self):
        return dict(relation='@righe')

    def gridStruct(self,struct):
        r = struct.view().rows()
        r.fieldcell('prodotto_id',mm_width=0, name='Prodotto')
        r.fieldcell('quantita',mm_width=10)
        r.fieldcell('prezzo_unitario',mm_width=20)
        r.fieldcell('aliquota_iva',mm_width=20)
        r.fieldcell('prezzo_totale',mm_width=20, name='Totale')
        r.fieldcell('iva',mm_width=20)

    def docHeader(self, header):
        layout = header.layout(name='doc_header', margin='5mm', border_width=0)
        row = layout.row()
        self.datiFattura(row.cell(width=80).layout('dati_fattura',
                                                    lbl_class='cell_label',
                                                    border_width=0))
        row.cell(width=0)
        self.datiCliente(row.cell(width=80).layout('dati_cliente', border_width=0))

    def datiFattura(self,layout):
        r = layout.row(height=8)
        r.cell(self.field('data'), lbl='Data')
        r = layout.row(height=8)
        r.cell(self.field('protocollo'), lbl='N.Fattura')
 
    def datiCliente(self,layout):
        layout.row(height=5).cell('Spett.')
        layout.row(height=5).cell(self.field('@cliente_id.ragione_sociale'))
        layout.row(height=5).cell(self.field('@cliente_id.indirizzo'))
        comune = self.field('@cliente_id.@comune_id.denominazione')
        provincia = self.field('@cliente_id.provincia')
        layout.row(height=5).cell('%s (%s)' % (comune, provincia))

    def docFooter(self, footer, lastPage=None):
        l = footer.layout('totali_fattura',top=1,
                           lbl_class='cell_label', 
                           content_class = 'footer_content')
        r = l.row(height=12)
        r.cell()
        r.cell(self.field('totale_imponibile'),lbl='Imponibile',  width=20)
        r.cell(self.field('totale_iva'),lbl='IVA',  width=20)
        r.cell(self.field('totale_fattura'),lbl='Totale',  width=20)
