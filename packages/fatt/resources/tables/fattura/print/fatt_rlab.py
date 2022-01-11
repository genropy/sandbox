from gnr.web.batch.btcprint import BaseResourcePrint

caption = 'Stampa Fattura RLAB'

class Main(BaseResourcePrint):
    batch_title = 'Stampa Fattura RLAB'
    rlab_res = 'rlab_res/mia_fattura'
    templates = 'carta_intestata'
