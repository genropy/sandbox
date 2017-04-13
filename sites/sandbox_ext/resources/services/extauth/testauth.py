#!/usr/bin/env pythonw
# -*- coding: UTF-8 -*-
#
#  Created by Saverio Porcari on 2013-04-06.
#  Copyright (c) 2013 Softwell. All rights reserved.


from gnr.core.gnrbaseservice import GnrBaseService
from subprocess import call
import os


class Main(GnrBaseService):
    def __init__(self, parent=None,key=None):
        self.parent = parent
        self.key = key

    def __call__(self,user=None, password=None,**kwargs):
        if password=='%s%s' %(user,self.key):
            return dict(username=user)
        else:
            return False
        