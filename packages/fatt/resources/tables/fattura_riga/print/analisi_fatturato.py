from gnr.web.batch.btcprint import BaseResourcePrint

caption = 'Stampa Analisi.Fatt'

class Main(BaseResourcePrint):
    batch_title = 'Analisi fatturato'
    html_res = 'html_res/stampa_analisi_fatturato'
    templates = 'carta_intestata'

    def table_script_parameters_pane(self, pane, **kwargs):
        fb = pane.formbuilder(cols=1,border_spacing='3px')
        fb.checkbox(value='^.use_current_selection',
                label='Selezione corrente', default=True)
        fb.dateTextBox(value='^.dal',lbl='Dal', period_to='.al', hidden='^.use_current_selection?=#v')
        fb.dateTextBox(value='^.al',lbl='Al', hidden='^.use_current_selection?=#v')
