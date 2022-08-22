# -*- coding: UTF-8 -*-
            
from gnr.core.gnrdecorator import public_method
from datetime import date,datetime
 

class GnrCustomWebPage(object):
    py_requires='gnrcomponents/externalcall:XmlRpc'

    @public_method
    def test(self,*args,**kwargs):
        print(args, kwargs)
        return "prova"

    @public_method
    def sum(self,a=0,b=0):
        print("sum of numbers: %s+%s=%s" % (a,b,a+b))
        return a+b


    @public_method(tags='ext')
    def lista_fatture(self,cliente=None,importo=None,columns=None,a_partire_dal=None):
        where = []
        columns= columns or '$protocollo,$data,@cliente_id.ragione_sociale AS cliente,$data,$totale_imponibile,$totale_iva,$totale_fattura'
        if cliente:
            where.append("@cliente_id.ragione_sociale ILIKE :cli")
            cliente = '%%%s%%' %cliente
        if importo:
            where.append('$totale_fattura>=:tot')
        if a_partire_dal:
            where.append('$data>=:a_partire_dal')
        selection = self.db.table('fatt.fattura').query(where=' AND '.join(where),cli=cliente,tot=importo,
                columns=columns,a_partire_dal=a_partire_dal).selection()
        result = selection.output('dictlist')
        return result

    @public_method
    def testnow(self):
        return datetime.now()

    @public_method
    def testdate(self):
        return date.today()

    @public_method
    def testtoday(self):
        return datetime.today()

    @public_method
    def testlist(self):
        return [[1,2],['a','b',33]]