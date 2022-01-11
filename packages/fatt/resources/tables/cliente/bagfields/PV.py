

from gnr.web.gnrbaseclasses import BagFieldForm

class BagField_dati(BagFieldForm):
    #py_requires='tariffe_component:TariffeComponent'
    
    def bf_main(self,pane,  provincia= None, **kwargs):
        fb = pane.formbuilder()
        fb.textbox(value='^.indirizzo',lbl=f'Indirizzo di casa {provincia}')
        fb.numberTextBox(value='^.numero_di_piede',lbl='Numero di piede')
        fb.div('viva i privati')