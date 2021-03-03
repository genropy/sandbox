#!/usr/bin/env python
# encoding: utf-8

from gnr.web.gnrbaseclasses import TableScriptToHtml
from gnr.core.gnrbag import Bag

class Main(TableScriptToHtml):
    row_table = 'fatt.cliente'
    doc_header_height = 16
    grid_row_height = 5
    cliente_height = 10
    #Definisco un parametro cliente_height che userò per calcolare l'altezza delle righe di intestazione e
    #l'avviso di mancanza di righe fatture per il cliente

    def docHeader(self, header):
        l = header.layout(name='doc_header', border_width=0)
        l.row().cell("""<center><div style='font-size:20pt; margin-top:2px;'><strong>Vendite per cliente</strong></div>::HTML""")

    def gridStruct(self,struct):
        r = struct.view().rows()
        #Trattandosi di stampa "custom", la griglia verrà ridefinita con il metodo prepareRows

    def gridData(self):
        #Usiamo sempre la selezione corrente (pkeys=self.record['selectionPkeys']) per individuare le righe fattura
        condition = ['$cliente_id IN :pkeys AND @fattura_id.data <= :data_fine']
        if self.parameter('data_inizio'):
            condition.append('@fattura_id.data >= :data_inizio')
        where = ' AND '.join(condition)
        #Se è presente una data inizio usiamo anche quella per filtrare per data
        
        self.vendite_per_cliente = self.db.table('fatt.fattura_riga').query(columns="""$cliente_id, 
                                                    @prodotto_id.descrizione AS prodotto, 
                                                    SUM($quantita) AS quantita, 
                                                    SUM($prezzo_totale) AS prezzo_totale""",
                                                    where = where,
                                                    pkeys=self.record['selectionPkeys'],
                                                    data_inizio = self.parameter('data_inizio'),
                                                    data_fine = self.parameter('data_fine'),
                                                    group_by='$cliente_id,@prodotto_id.descrizione',
                                                    order_by='SUM($prezzo_totale) DESC').fetchGrouped('cliente_id')
                                                    #Raggruppiamo righe risultato della query per cliente e poi per prodotto
                                                    #Con la fetchGrouped costruiamo poi un dizionario con chiave il cliente_id e valori la lista delle righe

        #Facciamo anche una query sulla row_table, per individuare dalle pkeys i "clienti" oggetto della stampa
        clienti = self.db.table('fatt.cliente').query(columns='$id,$ragione_sociale', where='$id IN :pkeys', 
                                                    pkeys=self.record['selectionPkeys']).fetch()
        return clienti

    def gridLayoutParameters(self):
        dflt_parameters = super(TableScriptToHtml, self).gridLayoutParameters()
        #Importiamo il gridLayoutParameters di default e ridefinamo solo il border_width.
        dflt_parameters['border_width']=0
        return dflt_parameters

    def prepareRow(self, row):
        l = row.cell().layout(top=2, bottom=2, left=1, right=1, border_width=0, font_size='9pt', style='text-indent:1mm;')
        cliente_row = l.row(height=self.cliente_height)
        intestazione = "I 10 prodotti più venduti a {cliente}".format(cliente=self.rowField('ragione_sociale'))
        if self.parameter('data_inizio'):
            intestazione = intestazione + " dal {data_inizio} a {data_fine}".format(data_inizio=self.parameter('data_inizio'), 
                                                                                data_fine=self.parameter('data_fine'))

        cliente_row.cell("""<div style='font-size:14px;'><strong>{intestazione}</strong></div>::HTML""".format(
                                                    intestazione=intestazione))
        
        cliente_id = self.rowField('id')
        vendite_cliente = self.vendite_per_cliente.get(cliente_id)

        if not vendite_cliente:
            #Stampiamo una riga con l'operazione e una nota che segnala la mancanza dei movimenti di pareggio
            nota_row = l.row(height=self.cliente_height)
            nota_row.cell('Nessuna vendita al cliente')
            return
        else:
            vendite_cliente = vendite_cliente[:10]
            #Se ci sono, prendiamo le prime 10 vendite_per_cliente del singolo cliente_id
        vendite_row = l.row(height=self.grid_row_height * (len(vendite_cliente)))
        venditeLayout = vendite_row.cell().layout(name='vendite',
                                    border_width=0.3,
                                    left=1,
                                    #Aggiungiamo un margine left di 1 per non far coincidere i layout dei vari livelli
                                    style='text-indent:1mm;')
        
        header_row = venditeLayout.row(background='grey', color='white',height=5)
        header_row.cell('Prodotto', content_class='aligned_center', width=0)
        header_row.cell('Quantità', content_class='aligned_center', width=20)
        header_row.cell('Prezzo tot.', content_class='aligned_center', width=20)
        #Queste saranno le righe di intestazione, una per ogni cliente
        
        for vendita in vendite_cliente:
            r = venditeLayout.row(height=5)
            r.cell(vendita['prodotto'], width=0)
            r.cell(self.toText(vendita['quantita'], format='#,###'), width=20)
            r.cell(self.toText(vendita['prezzo_totale'], format=self.currencyFormat), width=20)
            #Queste saranno le righe di vendita, una per ogni vendita

    def calcRowHeight(self):
        cliente_id = self.rowField('id')
        vendite_cliente = self.vendite_per_cliente.get(cliente_id)
        if not vendite_cliente:
            return self.cliente_height * 2
            #Se non ci sono vendite l'altezza della riga è quella dell'intestazione e della nota
        else:
            vendite_cliente = vendite_cliente[:10]
            #Anche qui prendiamo le prime 10 vendite_per_singolo_cliente del cliente_id
        n = len(vendite_cliente)
        n = n + 2
        height = (self.grid_row_height * n) + self.cliente_height
        return height 
        #Se invece ci sono le vendite l'altezza è quella delle righe di vendita (n), dell'intestazione e dei titoli della griglia

    def outputDocName(self, ext=''):
        docname = 'Vendite per cliente'
        if self.parameter('data_inizio'):
            docname = docname + " dal {data_inizio} a {data_fine}".format(data_inizio=self.parameter('data_inizio'), 
                                                                                data_fine=self.parameter('data_fine'))
        return '{docname}.{ext}'.format(ext=ext, docname=docname)     