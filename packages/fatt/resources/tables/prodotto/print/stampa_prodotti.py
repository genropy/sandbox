#!/usr/bin/env pythonw
# -*- coding: UTF-8 -*-
#
#  Stampa prodotti
#
#  Created by Davide Paci on 2021 03
#  Copyright (c) 2007-2021 Softwell. All rights reserved.

from gnr.web.batch.btcprint import BaseResourcePrint

caption = 'Stampa Statistiche Prodotti'

class Main(BaseResourcePrint):
    batch_title = 'Stampa Statistiche Prodotti'
    batch_immediate='print'
    #Con batch_immediate='print' viene immediatamente aperta la stampa alla conclusione
    html_res = 'html_res/stats_prodotti'
    #Questo parametro indica la risorsa di stampa da utilizzare

    def table_script_parameters_pane(self, pane,**kwargs):
        #Questo metodo consente l'inserimento di alcuni parametri da utilizzare per la stampa
        fb = pane.formbuilder(cols=1, width='220px')
        fb.filteringSelect(value='^.anno', values='2018,2019,2020', validate_notnull=True, lbl='!![it]Anno')
        fb.dbselect(value='^.cliente_id', table='fatt.cliente', lbl='Cliente', selected_ragione_sociale='.ragione_sociale')