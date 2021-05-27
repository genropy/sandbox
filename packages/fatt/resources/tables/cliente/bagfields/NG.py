

from gnr.web.gnrbaseclasses import BagFieldForm

class BagField_dati(BagFieldForm):
    #py_requires='tariffe_component:TariffeComponent'
    
    def bf_main(self,pane,  provincia= None, **kwargs):
        fb = pane.formbuilder()
        fb.textbox(value='^.indirizzo',lbl=f'Indirizzo filiale {provincia}')
        fb.div('viva NG')