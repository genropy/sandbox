
from gnr.web.gnrbaseclasses import BaseComponent

class View(BaseComponent):
    def th_struct(self,struct):
        r=struct.view().rows()
        r.fieldcell('protocollo',width='10em')
        r.fieldcell('data',width='7em')
        r.fieldcell('cliente_id',zoom=True,width='15em')
        cs = r.columnset('totali',name='Totali')
        cs.fieldcell('totale_imponibile',width='7em',name='Tot.Imp')
        cs.fieldcell('totale_iva',width='7em',name='Tot.Iva')
        cs.fieldcell('totale_fattura',width='7em',name='Totale')
        pr = r.columnset('provvigioni',name='Provvigioni')
        pr.fieldcell('agente_id',width='15em',name='Agente')
        pr.fieldcell('importo_agente',width='7em',name='Provvigione')

   #def th_options(self):
   #    return dict(partitioned=True)
    
    def th_order(self):
        return 'protocollo'

class ViewFromAgente(BaseComponent):
    def th_struct(self,struct):
        r=struct.view().rows()
        r.fieldcell('protocollo',width='10em')
        r.fieldcell('data',width='7em')
        r.fieldcell('cliente_id',zoom=True,width='15em')
        cs = r.columnset('totali',name='Totali')
        cs.fieldcell('totale_imponibile',width='7em',name='Tot.Imp')
        cs.fieldcell('totale_iva',width='7em',name='Tot.Iva')
        cs.fieldcell('totale_fattura',width='7em',name='Totale')
        pr = r.columnset('provvigioni',name='Provvigioni')
        pr.fieldcell('agente_id',width='15em',name='Agente')
        pr.fieldcell('importo_agente',width='7em',name='Provvigione',totalize=True)
    def th_order(self):
        return 'protocollo'
