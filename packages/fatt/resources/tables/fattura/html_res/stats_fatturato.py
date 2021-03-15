#!/usr/bin/env pythonw
# -*- coding: UTF-8 -*-
#
#  Stampa statistiche fatturato
#
#  Created by Davide Paci on 2021 03
#  Copyright (c) 2007-2021 Softwell. All rights reserved.

from gnr.web.gnrbaseclasses import TableScriptToHtml

class Main(TableScriptToHtml):

    row_table = 'fatt.fattura'
    page_width = 210
    page_height = 297
    doc_header_height = 30
    doc_footer_height = 8
    grid_header_height = 5
    totalize_footer='Totale fatturato'
    #Fornendo a totalize_footer una stringa testuale, questa verrà usata come etichetta della riga di totalizzazione

    def docHeader(self, header):
        #Questo metodo definisce il layout e il contenuto dell'header della stampa
        head = header.layout(name='doc_header', margin='5mm', border_width=0)
        row = head.row()
        row.cell("""<center><div style='font-size:18pt;'><strong>Statistiche fatturato per periodo</strong></div>
                    <div style='font-size:14pt;'>Esercizio {anno}</div></center>::HTML""".format(anno=self.parameter('anno')))
        if self.parameter('cliente_id'):
            row = head.row()
            row.cell("""<center><div style='font-size:14pt;'>{cliente}</div></center>::HTML""".format(
                                cliente=self.parameter('ragione_sociale')))

    def defineCustomStyles(self):
        #Questo metodo definisce gli stili del body dell'html
        self.body.style(""".cell_label{
                            font-size:8pt;
                            text-align:left;
                            color:grey;
                            text-indent:1mm;}

                            .footer_content{
                            text-align:right;
                            margin:2mm;
                            }
                            """)

    def gridStruct(self,struct):
        #Questo metodo definisce la struttura della griglia di stampa definendone colonne e layout
        r = struct.view().rows()
        r.fieldcell('data', mm_width=15)
        r.fieldcell('mese_fattura', hidden=True, subtotal='Totale {breaker_value}', subtotal_order_by="$data")
        #Questa formulaColumn verrà utilizzata per creare i subtotali per mese
        r.fieldcell('protocollo', mm_width=20, name='Documento')
        r.fieldcell('cliente_id', mm_width=0)
        r.fieldcell('totale_imponibile', mm_width=20, totalize=True)
        r.fieldcell('totale_iva', mm_width=20, totalize=True)
        r.fieldcell('totale_fattura', mm_width=20, totalize=True)

    def gridQueryParameters(self):
        #Questo metodo fornisce a gridData i parametri (condizioni, relation, table) sulla base dei quali costruire 
        #le righe con i dati da riportare in griglia. In questo caso uso una condizione.
        condition=['$anno_fattura=:anno']
        if self.parameter('cliente_id'):
            condition.append('$cliente_id=:cliente')
        return dict(condition=' AND '.join(condition), condition_anno=self.parameter('anno'), 
                        condition_cliente=self.parameter('cliente_id'))

    def docFooter(self, footer, lastPage=None):
        #Questo metodo definisce il layout e il contenuto dell'header della stampa
        foo = footer.layout('totali_fattura',top=1,
                           lbl_class='cell_label', 
                           content_class = 'footer_content')
        r = foo.row()
        r.cell('Documento stampato il {oggi}'.format(oggi=self.db.workdate))

    def outputDocName(self, ext=''):
        #Questo metodo definisce il nome del file di output
        if ext and not ext[0] == '.':
            ext = '.%s' % ext
        if self.parameter('cliente_id'):
            doc_name = 'Fatturato_{anno}_{cliente}{ext}'.format(anno=self.parameter('anno'), 
                        cliente=self.parameter('ragione_sociale'), ext=ext)
        else: 
            doc_name = 'Fatturato_{anno}{ext}'.format(anno=self.parameter('anno'), ext=ext)
        return doc_name