#!/usr/bin/env pythonw
# -*- coding: UTF-8 -*-
#
#  Stampa scheda cliente
#
#  Created by Davide Paci on 2021 03
#  Copyright (c) 2007-2021 Softwell. All rights reserved.
 
from gnr.web.batch.btcprint import BaseResourcePrint

caption = 'Scheda cliente'

class Main(BaseResourcePrint):
    batch_title = 'Scheda cliente'
    html_res = 'html_res/stampa_scheda_cliente'
    batch_immediate = 'print'