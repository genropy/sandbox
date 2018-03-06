# -*- coding: UTF-8 -*-
#from gnr.core.gnrbag import Bag
from gnr.core.gnrdecorator import public_method
from gnr.core.gnrbag import DirectoryResolver

class GnrCustomWebPage(object):
    def main(self,root,**kwargs):
        root.div('Ciao io sono la versione mobile %s e sono mobile? %s' %(id(self), self.isMobile))