from gnr.web.batch.btcprint import BaseResourcePrint

caption = 'Stampa Dati Comuni'

class Main(BaseResourcePrint):
    batch_title = 'Stampa Dati Comuni'
    batch_immediate='print'
    #Con batch_immediate='print' viene immediatamente aperta la stampa alla conclusione
    html_res = 'html_res/dati_comuni'
    #Questo parametro indica la risorsa di stampa da utilizzare

    def table_script_parameters_pane(self, pane,**kwargs):
        #Questo metodo consente l'inserimento di alcuni parametri da utilizzare per la stampa
        fb = pane.formbuilder(cols=1, width='220px')
        fb.dbselect(value='^.regione', table='glbl.regione', lbl='Regione', selected_nome='.regione_nome', hasDownArrow=True)