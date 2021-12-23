# -*- coding: UTF-8 -*-

from gnr.core.gnrdecorator import public_method
class GnrCustomWebPage(object):
    
    @public_method
    def pippo(self,name=None,**kwargs):
        return 'pippo'
