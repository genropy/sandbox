from gnr.app.gnrapp import GnrApp
from gnr.core.gnrbag import Bag



def main(db):
    tbl_fattura = db.table('fatt.fattura')
    tbl_cliente = db.table('fatt.cliente')

    name = 'Mario Rossi Srl'
    #if tbl_cliente.query(where='$ragione_sociale=:nn', nn=name).count()==0:

    # inserisco il cliente    
    cliente_record = tbl_cliente.newrecord(ragione_sociale=name)
    tbl_cliente.insert(cliente_record)

    # inserisco 10 fatture
    # il campo colonna_testo è None
    for _ in range(10):
        tbl_fattura.insert(tbl_fattura.newrecord(cliente_id=cliente_record['id']))
