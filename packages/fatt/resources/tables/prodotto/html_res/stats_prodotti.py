#!/usr/bin/env python
# encoding: utf-8

from gnr.web.gnrbaseclasses import TableScriptToHtml

class Main(TableScriptToHtml):

    maintable = 'fatt.prodotto'
    row_table = 'fatt.prodotto'
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
        row.cell("""<center><div style='font-size:18pt;'><strong>Statistiche prodotti</strong></div>
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
    def gridData(self):
        #Questo metodo permette di specificare i criteri di funzionamento della query (condizioni, raggruppamenti) ed eventualmente
        #intervenire direttamente modificando la selezione. Nell'esempio aggiungiamo infatti una categoria principale alle colonne
        #già calcolate dalla query, per poter calcolare dei subtotali per gruppo "parent" della gerarchia  
        condition=['@fattura_id.anno_fattura=:anno']
        if self.parameter('cliente_id'):
            condition.append('@fattura_id.cliente_id=:cliente')
        where=' AND '.join(condition)

        fatturato_grouped_by_prodotto = self.db.table('fatt.fattura_riga').query(columns="""
                                            SUM($prezzo_totale) AS prezzo_totale,
                                            SUM($iva) AS iva,
                                            @prodotto_id.codice AS codice,
                                            @prodotto_id.descrizione AS descrizione,
                                            @prodotto_id.@prodotto_tipo_id.hierarchical_descrizione AS prodotto_gerarchia,
                                            @prodotto_id.@prodotto_tipo_id.descrizione AS prodotto_tipo""",
                                            where=where,
                                            anno=self.parameter('anno'),
                                            cliente=self.parameter('cliente_id'),
                                            group_by="""@prodotto_id.codice, @prodotto_id.descrizione, 
                                            @prodotto_id.@prodotto_tipo_id.hierarchical_descrizione,
                                            @prodotto_id.@prodotto_tipo_id.descrizione""").fetch()

        for prodotto in fatturato_grouped_by_prodotto:
            categoria_principale = prodotto['prodotto_gerarchia'].split('/')[0]
            prodotto['categoria_principale'] = categoria_principale
        
        return fatturato_grouped_by_prodotto

    def gridStruct(self,struct):
        #Questo metodo definisce la struttura della griglia di stampa definendone colonne e layout
        r = struct.view().rows()
        r.fieldcell('codice', mm_width=15)
        r.fieldcell('descrizione', mm_width=0)
        r.cell('prodotto_tipo', mm_width=20, name='Tipo prodotto')
        r.cell('categoria_principale', hidden=True, subtotal='Totale {breaker_value}')
        r.cell('prezzo_totale', mm_width=20, name='Fatturato tot.', totalize=True)
        r.cell('iva', mm_width=20, name='IVA tot.',totalize=True)

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
            doc_name = 'Prodotti_{anno}_{cliente}{ext}'.format(anno=self.parameter('anno'), 
                        cliente=self.parameter('ragione_sociale'), ext=ext)
        else: 
            doc_name = 'Prodotti_{anno}{ext}'.format(anno=self.parameter('anno'), ext=ext)
        return doc_name