
from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method,oncalled
from gnr.core.gnrnumber import decimalRound

class ViewFromAgente(BaseComponent):
    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('agente_id', width='16em')
        r.fieldcell('ragione_sociale', width='16em')
        r.fieldcell('indirizzo')
        r.fieldcell('comune_id')
        r.fieldcell('provincia')
        r.fieldcell('@provincia.regione',name='Reg',width='4em')
        r.fieldcell('n_fatture')
        r.fieldcell('provv_calc')
        r.fieldcell('tot_fatturato',format='#,###.00',totalize=True)

class Form(BaseComponent):
    @oncalled
    def clienteTabs(self,tc,**kwargs):
        #TODO: [SAN-1] finire la demo
        tc.contentPane(title='Appuntamenti').dialogTableHandler(relation='@appuntamenti')
