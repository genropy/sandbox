# -*- coding: UTF-8 -*-

# test_special_action.py
# Created by Saverio Porcari on 2010-07-02.
# Copyright (c) 2010 Softwell. All rights reserved.

from gnr.web.batch.btcprint import BaseResourcePrint

caption = 'Fattura auto'
tags = 'user'
description= 'Fattura auto'
user_selection = True

class Main(BaseResourcePrint):
    batch_prefix = 'fatt_auto'
    batch_title =  'Fattura auto'
    batch_cancellable = True
    batch_delay = 0.5
    html_res = 'html_res/fattura_auto'
    batch_immediate='print'