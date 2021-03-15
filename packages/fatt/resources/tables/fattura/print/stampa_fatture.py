#!/usr/bin/env pythonw
# -*- coding: UTF-8 -*-
#
#  Stampa fatture
#
#  Created by Davide Paci on 2021 03
#  Copyright (c) 2007-2021 Softwell. All rights reserved.
 
from gnr.web.batch.btcprint import BaseResourcePrint

caption = 'Stampa Fattura'

class Main(BaseResourcePrint):
    batch_title = 'Stampa Fattura'
    batch_immediate='print'
    #Con batch_immediate='print' viene immediatamente aperta la stampa alla conclusione
    html_res = 'html_res/mia_fattura'
    templates = 'carta_intestata'

    #Non utilizziamo il table_script_parameters_pane perché ci limiteremo a stampare la selezione corrente