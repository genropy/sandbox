from gnr.web.gnrbaseclasses import BaseComponent

class View(BaseComponent):
    def th_struct(self,struct):
        r=struct.view().rows()
        r.fieldcell('sigla')
        r.fieldcell('nome')
        r.fieldcell('tariffa_spedizione')