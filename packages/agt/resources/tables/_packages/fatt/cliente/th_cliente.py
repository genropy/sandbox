
from gnr.web.gnrbaseclasses import BaseComponent

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('agente_id', width='16em')
        r.fieldcell('ragione_sociale', width='16em')
        r.fieldcell('indirizzo')
        r.fieldcell('comune_id')
        r.fieldcell('provincia')
        r.fieldcell('n_fatture')
        r.fieldcell('provv_calc')
        r.fieldcell('tot_fatturato',format='#,###.00')

    #def th_options(self):
    #    return dict(partitioned=True)


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
