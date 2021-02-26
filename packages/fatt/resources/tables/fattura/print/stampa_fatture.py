from gnr.web.batch.btcprint import BaseResourcePrint

caption = 'Stampa Fattura'

class Main(BaseResourcePrint):
    batch_title = 'Stampa Fattura'
    batch_immediate='print'
    #Con batch_immediate='print' viene immediatamente aperta la stampa alla conclusione
    html_res = 'html_res/mia_fattura'
    templates = 'carta_intestata'

    #Non utilizziamo il table_script_parameters_pane perché ci limiteremo a stampare la selezione corrente