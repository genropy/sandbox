from gnr.web.batch.btcprint import BaseResourcePrint

caption = 'Scheda cliente'

class Main(BaseResourcePrint):
    batch_title = 'Scheda cliente'
    html_res = 'html_res/stampa_scheda_cliente'
    batch_immediate = 'print'