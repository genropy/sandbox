#!/usr/bin/env python
# encoding: utf-8

from gnr.web.gnrbaseclasses import TableScriptToHtml

class Main(TableScriptToHtml):
    row_table = 'fatt.fattura_riga'
    doc_header_height = 32
    doc_footer_height = 12
    grid_header_height = 5

    def docHeader(self, header):
        l = header.layout(name='doc_header', margin='5mm', border_width=0)
        l.row(height=5).cell('Analisi del fatturato su base geografica')

    def gridStruct(self,struct):
        r = struct.view().rows()
        fatt = r.columnset('fatt', name='Dati fattura', 
                                background='rgba(38, 88, 32, 1.00)',
                                cell_width='5em',cell_background='rgba(38, 88, 32, 0.20)')

        geo = r.columnset('geo', name='Dati geografici', 
                                background='rgba(38, 88, 32, 1.00)',
                                cell_width='5em',cell_background='rgba(38, 88, 32, 0.20)')

        geo.fieldcell('@fattura_id.@cliente_id.@provincia.@regione.zona', 
                        mm_width=20, name='Zona', subtotal=True, subtotal_caption='Totale zona')
        geo.fieldcell('@fattura_id.@cliente_id.@provincia.regione', 
                        mm_width=20, name='Regione', subtotal=True, subtotal_caption='Totale regione')
        geo.fieldcell('@fattura_id.@cliente_id.provincia', 
                        mm_width=20, name='Prov.')

        fatt.fieldcell('@fattura_id.data',mm_width=20, name='Data')
        fatt.fieldcell('@fattura_id.protocollo',mm_width=20, name='Protocollo')
        fatt.fieldcell('@fattura_id.@cliente_id.ragione_sociale',mm_width=30, name='Cliente')
        
        r.fieldcell('prodotto_id', name='Prodotto')
        r.fieldcell('quantita', name='Qt', mm_width=12, totalize=True)
        r.fieldcell('prezzo_totale', mm_width=12, totalize=True)

    def gridQueryParameters(self):
        return dict(table='fatt.fattura_riga',
                    condition='@fattura_id.data BETWEEN :dal AND :al',
                    condition_dal= self.parameter('dal'),
                    condition_al = self.parameter('al'))
        #Il metodo gridQueryParameters imposterà le condizioni che verranno utilizzate solo se self.parameter('use_current_selection')=False
        #Questo check verrà effettuato automaticamente da Genropy
