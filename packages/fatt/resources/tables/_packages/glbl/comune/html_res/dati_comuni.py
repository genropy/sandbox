#!/usr/bin/env python
# encoding: utf-8

from gnr.web.gnrbaseclasses import TableScriptToHtml

class Main(TableScriptToHtml):

    row_table = 'glbl.comune'
   # page_orientation = 'H'
    #Specifichiamo una page_orientation per indicare che la stampa sarà sempre orizzontale
    doc_header_height = 20
    doc_footer_height = 0
    grid_header_height = 5
    grid_row_height = 5
    #Questo valore specifica l'altezza di ogni singola riga, per poi modificarla nel metodo calcRowHeight
    totalize_footer=True
    #Inserendo totalize_footer=True verrà semplicemente calcolato un totale senza etichetta
    totalize_mode='page'
    #Con totalize_mode='page' la totalizzazione sarà calcolata a ogni pagina, invece che in fondo al documento (totalize_mode='doc')

    def docHeader(self, header):
        #Questo metodo definisce il layout e il contenuto dell'header della stampa
        head = header.layout(name='doc_header', margin='5mm', border_width=0)
        row = head.row()
        row.cell("""<center><div style='font-size:18pt;'><strong>
                    Riepilogo principali comuni per popolazione della Regione {regione}</strong></div></center>::HTML""".format(
                    regione=self.parameter('regione_nome')))

    def defineCustomStyles(self):
        #Questo metodo definisce gli stili del body dell'html
        self.body.style(""".cell_label{
                            font-size:11pt;
                            text-align:left;
                            color:grey;
                            text-indent:1mm;}

                            .caption, .x_br{
                            font-size:9.5pt;}
                            """)

    def gridStruct(self,struct):
        #Questo metodo definisce la struttura della griglia di stampa definendone colonne e layout
        r = struct.view().rows()
        r.fieldcell('denominazione', mm_width=0, white_space='pre-line')
        com = r.columnset('com', name='DATI COMUNE', background='lightblue', color='white', 
                                font_size='14px', font_weight='bold')
        com.fieldcell('@localita.codice_istat', mm_width=15, name='Codice')
        com.fieldcell('@localita.prefisso_tel', mm_width=15, name='Pref.Tel.')
        com.fieldcell('@localita.cap', mm_width=14)
        com.fieldcell('zona_altimetrica', mm_width=12, name='Zona')
        com.fieldcell('altitudine', mm_width=16, name='Altitudine')
        com.fieldcell('litoraneo', mm_width=16)
        com.fieldcell('comune_montano', mm_width=16, name='Montagna')
        com.fieldcell('superficie', mm_width=15, totalize=True, name='Superficie')
        com.fieldcell('popolazione_residente', mm_width=20, totalize=True, name='Popolazione')
        prov = r.columnset('prov', name='DATI PROVINCIA', background='lightgreen', color='white', 
                                font_size='14px', font_weight='bold')
        prov.fieldcell('sigla_provincia', mm_width=12, name='Sigla')
        prov.fieldcell('@sigla_provincia.nome', mm_width=24, white_space='pre-line')
        prov.fieldcell('@sigla_provincia.codice_istat', mm_width=15, name='Codice')
        prov.fieldcell('@sigla_provincia.numero_abitanti', mm_width=20, totalize=True, name='Popolazione')
        prov.fieldcell('@sigla_provincia.tot_superficie', mm_width=20, totalize=True, name='Superficie')
        incid = r.columnset('incid', name='INCIDENZA', background='lightcoral', color='white', 
                                font_size='14px', font_weight='bold')
        incid.cell('superficie_perc', sqlcolumn="$superficie/@sigla_provincia.tot_superficie*100 AS superficie_perc", 
                            format='#,###.00', mm_width=15, name='Sup.%', content_class='aligned_right')
        incid.cell('popolazione_perc', sqlcolumn="$popolazione_residente/@sigla_provincia.numero_abitanti*100 AS popolazione_perc",  
                            format='#,###.00', mm_width=15, name='Pop.%', content_class='aligned_right')

    def gridQueryParameters(self):
        #Questo metodo fornisce a gridData i parametri (condizioni, relation, table) sulla base dei quali costruire 
        #le righe con i dati da riportare in griglia. In questo caso uso una condizione, ordino sulla base della popolazione e
        #prendo solo i primi 100 risultati.
        return dict(condition='@sigla_provincia.regione=:regione', condition_regione=self.parameter('regione'), 
                        order_by='$popolazione_residente DESC', limit=100)

    def calcRowHeight(self):
        #Determina l'altezza di ogni singola riga con approssimazione partendo dal valore di riferimento grid_row_height
        nome_offset = 22
        #Stabilisco un offset in termini di numero di caratteri oltre il quale stabilirò di andare a capo.  
        #Attenzione che in questo caso ho una dimensione in num. di caratteri, mentre la larghezza della colonna è definita 
        #in mm, e non avendo utti i caratteri la stessa dimensione si tratterà quindi di individuare la migliore approssimazione
        n_rows_nome_comune = len(self.rowField('denominazione'))//nome_offset + 1
        n_rows_nome_provincia = len(self.rowField('_sigla_provincia_nome'))//nome_offset + 1
        #In caso di valori in relazione, è necessario utilizzare "_" nel metodo rowField per recuperare correttamente i valori
        #A tal proposito si consiglia comunque sempre di utilizzare le aliasColumns
        n_rows = max(n_rows_nome_comune, n_rows_nome_provincia)
        height = (self.grid_row_height * n_rows)
        return height

    def outputDocName(self, ext=''):
        #Questo metodo definisce il nome del file di output
        if ext and not ext[0] == '.':
            ext = '.%s' % ext
        doc_name = 'Dati Comuni_{regione}{ext}'.format(regione=self.parameter('regione'), ext=ext)
        return doc_name