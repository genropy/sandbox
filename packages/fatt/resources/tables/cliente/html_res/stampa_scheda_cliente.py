#!/usr/bin/env pythonw
# -*- coding: UTF-8 -*-
#
#  Stampa scheda cliente
#
#  Created by Davide Paci on 2021 03
#  Copyright (c) 2007-2021 Softwell. All rights reserved.

from gnr.web.gnrbaseclasses import TableScriptToHtml

class Main(TableScriptToHtml):
    maintable = 'fatt.cliente'
    virtual_columns = '$n_fatture,$tot_fatturato,$iscritto_newsletter'
    #Con virtual_columns aggiungo a self.record anche le formulaColumn calcolate che altrimenti di default non verrebbero compilate 
    
    def main(self):
        self.schedaCliente()
        #Nel metodo main specifichiamo tutti i metodi da eseguire: in questo caso solo un metodo schedaCliente totalmente customizzato

    def schedaCliente(self):
        self.paperpage = self.getNewPage()
        layout = self.paperpage.layout(
                            um='mm',top=5,left=4,right=4, bottom=3,
                            border_width=1,
                            font_family='Helvetica',
                            font_size='9pt',
                            lbl_height=4,lbl_class='caption',
                            border_color='grey')

        layout.row(height=10).cell("<div style='font-size:20pt;padding:5px'><strong>Dati Anagrafici</strong></div>::HTML")
        dati_cliente = layout.row(height=20, lbl_height=4, lbl_class='smallCaption')
        layout.row(height=10).cell("<div style='font-size:20pt;padding:5px'><strong>Fatture Cliente</strong></div>::HTML")
        griglia_fatture = layout.row(height=150, lbl_height=4, lbl_class='smallCaption')
        layout.row(height=10).cell("<div style='font-size:20pt;padding:5px'><strong>Prodotti Cliente</strong></div>::HTML")
        griglia_prodotti = layout.row(height=74, lbl_height=4, lbl_class='smallCaption')
        
        self.datiCliente(dati_cliente)
        self.righeFatture(griglia_fatture)
        self.righeProdotti(griglia_prodotti)
     
    def datiCliente(self, row):
        indirizzo = self.field('indirizzo') + ', ' + self.field('@comune_id.denominazione') + ' (' + self.field('provincia') + ')'
        
        dati_layout = row.cell().layout(name='datiCliente', um='mm', border_color='grey', lbl_class='smallCaption',
                                    lbl_height=3, style='line-height:5mm;text-indent:2mm;')
                            
        dati_layout.row().cell(self.field('ragione_sociale'), lbl="Ragione sociale")
        dati_layout.row().cell(indirizzo, lbl="Indirizzo")

        contatti_layout = row.cell().layout(name='contattiCliente', um='mm', border_color='grey', lbl_class='smallCaption',
                                    lbl_height=3, style='line-height:5mm;text-indent:2mm;')
        contatti_layout.row().cell(self.field('email'), lbl="Email")
        contatti_layout.row().cell(self.field('iscritto_newsletter'), lbl="Iscritto newsletter")

    def righeFatture(self, row):
        fatture_layout = row.cell().layout(name='datiFatture', um='mm', border_color='grey', lbl_class='smallCaption',
                                    lbl_height=3, style='line-height:5mm;text-indent:2mm;')
        
        fatture_layout.row(height=8).cell("Elenco delle fatture emesse al cliente dal momento dell'acquisizione a oggi")

        intestazione = fatture_layout.row(height=6)
        intestazione.cell("Estremi documento", content_class='aligned_center')
        intestazione.cell("Imponibile", content_class='aligned_center')

        fatture = self.record['@fatture']
        for f in fatture.values():
            estremi_documento = "Fattura num. {protocollo} del {data}".format(protocollo=f['protocollo'], data=f['data'])
            r = fatture_layout.row(height=5)
            r.cell(estremi_documento)
            r.cell(self.toText(f['totale_imponibile'], format=self.currencyFormat), content_class='aligned_right')

        fatture_layout.row().cell()
        footer_fatture = fatture_layout.row(height=10)
        footer_fatture.cell(self.record['n_fatture'], lbl="Num. Fatture", content_class='aligned_right')
        footer_fatture.cell(self.toText(self.record['tot_fatturato'], format=self.currencyFormat), lbl="Tot. Fatturato", content_class='aligned_right')
    
    def righeProdotti(self, row):
        prodottiLayout = row.cell().layout(name='datiProdotti', um='mm', border_color='grey', lbl_class='smallCaption',
                                    lbl_height=3, style='line-height:5mm;text-indent:2mm;')
    
        prodottiLayout.row(height=8).cell("Elenco dei 10 prodotti più venduti al cliente ordinati per fatturato totale, dal momento dell'acquisizione a oggi")

        intestazione = prodottiLayout.row(height=6)
        intestazione.cell("Prodotto", width=0, content_class='aligned_center')
        intestazione.cell("Quantità", width=30, content_class='aligned_center')
        intestazione.cell("Tot.Fatturato", width=30, content_class='aligned_center')

        prodotti = self.db.table('fatt.fattura_riga').query(columns="""$cliente_id, 
                                                    @prodotto_id.descrizione AS prodotto, 
                                                    SUM($quantita) AS quantita, 
                                                    SUM($prezzo_totale) AS prezzo_totale""",
                                                    where = '$cliente_id=:cliente',
                                                    cliente=self.record['id'],
                                                    group_by='$cliente_id,@prodotto_id.descrizione',
                                                    order_by='SUM($prezzo_totale) DESC',
                                                    limit=10).fetch()
                                                    #Raggruppiamo righe risultato della query per prodotto

        for p in prodotti:
            r = prodottiLayout.row(height=6)
            r.cell(p['prodotto'], width=0)
            r.cell(p['quantita'], width=30, content_class='aligned_right')
            r.cell(self.toText(p['prezzo_totale'], format=self.currencyFormat), width=30, content_class='aligned_right')

    def outputDocName(self, ext=''):
        return 'Scheda cliente_{cliente}.{ext}'.format(cliente=self.record['ragione_sociale'], ext=ext)