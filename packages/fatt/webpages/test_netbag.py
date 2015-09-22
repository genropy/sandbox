# -*- coding: UTF-8 -*-
            
from gnr.core.gnrdecorator import public_method
 

class GnrCustomWebPage(object):
    py_requires='gnrcomponents/externalcall:NetBagRpc'


    @public_method(tags='ext')
    def netbag_lista_fatture(self,cliente=None,importo=None,columns=None,**kwargs):
        where = []
        columns= columns or '$protocollo,$data,@cliente_id.ragione_sociale AS cliente,$data,$totale_imponibile,$totale_iva,$totale_fattura'
        if cliente:
            where.append("@cliente_id.ragione_sociale ILIKE :cli")
            cliente = '%%%s%%' %cliente
        if importo:
            where.append('$totale_fattura>=:tot')
        selection = self.db.table('fatt.fattura').query(where=' AND '.join(where),cli=cliente,tot=importo,
                columns=columns).selection()
        return self.selectionToNetBag(selection,output='v')

    @public_method(tags='ext')
    def netbag_selection(self,table=None,**kwargs):
        selection = self.db.table(table).query(**kwargs).selection()
        return self.selectionToNetBag(selection,mode='v')

    @public_method(tags='ext')
    def netbag_record(self,table=None,pkey=None,**kwargs):
        kwargs.setdefault('addPkeyColumn',False)
        record = self.db.table(table).record(pkey=pkey,**kwargs)
        result = record.output('record')
        return result


