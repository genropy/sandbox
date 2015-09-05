# -*- coding: UTF-8 -*-
            
from gnr.core.gnrdecorator import public_method
 

class GnrCustomWebPage(object):
    py_requires='gnrcomponents/externalcall:XmlRpc'

    @public_method
    def test(self,*args,**kwargs):
        print args, kwargs
        return "prova"

    @public_method
    def sum(self,a=0,b=0):
        print "sum of numbers: %s+%s=%s" % (a,b,a+b)
        return a+b


    @public_method(tags='admin')
    def lista_fatture(self,cliente=None,importo=None,columns=None):
         where = []
         columns= columns or '$protocollo,$data,@cliente_id.ragione_sociale AS cliente,$data,$totale_imponibile,$totale_iva,$totale_fattura'
         if cliente:
             where.append("@cliente_id.ragione_sociale ILIKE :cli")
             cliente = '%%%s%%' %cliente
         if importo:
             where.append('$totale_fattura>=:tot')
         selection = self.db.table('fatt.fattura').query(where=' AND '.join(where),cli=cliente,tot=importo,
                 columns=columns).selection()
         result = selection.output('dictlist')
         return result