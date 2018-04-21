from gnr.web.gnrbaseclasses import BaseComponent
from gnr.web.gnrwebstruct import struct_method

class LayoutBelli(BaseComponent):
    def makeTab(self,tc,**kwargs):
        alfa = tc.contentPane(**kwargs)
        fb = alfa.formbuilder()
        fb.textbox(value='^.nome',lbl='Nome')
        fb.textbox(value='^.cognome',lbl='Cognome')
        fb.textbox(value='^.indirizzo',lbl='Indirizzo')
