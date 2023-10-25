#!/usr/bin/env pythonw
# -*- coding: UTF-8 -*-
#
#  Stampa vendite clienti
#
#  Created by Davide Paci on 2021 03
#  Copyright (c) 2007-2021 Softwell. All rights reserved.

from gnr.web.batch.btcprint import BaseResourcePrint

caption = 'Vendite per cliente'

class Main(BaseResourcePrint):
    batch_title = 'Vendite per cliente'
    html_res = 'html_res/stampa_vendite_clienti'
    batch_immediate = 'print'

    def table_script_parameters_pane(self, pane, **kwargs):
        fb = pane.formbuilder(cols=1,border_spacing='3px')
        fb.div('Stai per stampare i 10 prodotti più venduti a ' + str(kwargs['record_count']) + ' clienti')
        #In kwargs['record_count'] viene automaticamente immagazzinato il conteggio dei record della selezione
        fb.dateTextBox(value='^.data_inizio',lbl='Dal', period_to='.data_fine')
        fb.dateTextBox(value='^.data_fine', lbl='Al', default=self.db.workdate)
