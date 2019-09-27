from gnr.web.batch.btcprint import BaseResourcePrint

caption = 'Stampa Fattura'

class Main(BaseResourcePrint):
    batch_title = 'Stampa Fattura'
    html_res = 'html_res/fattura_stampa'
    templates = 'carta_intestata'

