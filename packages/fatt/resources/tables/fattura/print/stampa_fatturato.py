#!/usr/bin/env pythonw
# -*- coding: UTF-8 -*-
#
#  Stampa statistiche fatturato
#
#  Created by Davide Paci on 2021 03
#  Copyright (c) 2007-2021 Softwell. All rights reserved.

from datetime import datetime
from gnr.web.batch.btcprint import BaseResourcePrint

caption = 'Stampa Statistiche Fatturato'

class Main(BaseResourcePrint):
    batch_title = 'Stampa Statistiche Fatturato'
    batch_immediate='print'
    #Con batch_immediate='print' viene immediatamente aperta la stampa alla conclusione
    html_res = 'html_res/stats_fatturato'
    #Questo parametro indica la risorsa di stampa da utilizzare

    def table_script_parameters_pane(self, pane,**kwargs):
        #Questo metodo consente l'inserimento di alcuni parametri da utilizzare per la stampa
        current_year = datetime.today().year
        last_years = [current_year, current_year-1, current_year-2, current_year-3, current_year-4]
        years = ','.join(str(e) for e in last_years)
        #Prepariamo la stringa con gli ultimi 5 anni separati da virgola da passare alla filteringSelect
        fb = pane.formbuilder(cols=1, width='220px')
        fb.filteringSelect(value='^.anno', values=years, validate_notnull=True, lbl='!![it]Anno')
        fb.dbselect(value='^.cliente_id', table='fatt.cliente', lbl='Cliente', selected_ragione_sociale='.ragione_sociale')