# -*- coding: UTF-8 -*-
from gnr.core.gnrdecorator import public_method


class GnrCustomWebPage(object):
    py_requires='gnrcomponents/externalcall:BaseRpc'

    @public_method
    def somma(self,a=0,b=0,**kwargs):
        print('richiesta somma',a,b,kwargs)
        return int(a)+int(b)


    @public_method
    def moltiplica(self,a=0,b=0,**kwargs):
        return int(a)*int(b)
    
    @public_method(tags='_SYSTEM_')
    def elenco_clienti(self,provincia=None):
        return self.db.table('fatt.cliente').query(
            where='$provincia=:pr' if provincia else '$id IS NOT NULL',
            pr=provincia,columns='$ragione_sociale,$indirizzo,$provincia'
        ).selection().output('baglist')
        
    @public_method
    def controlla_ordine(self,ordine=None,**kwargs):
        print('ordine',ordine)

