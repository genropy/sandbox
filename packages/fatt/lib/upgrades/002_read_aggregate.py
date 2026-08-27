from gnr.app.gnrapp import GnrApp
from gnr.core.gnrbag import Bag



def main(db):
    tbl_fattura = db.table('fatt.fattura')
    tbl_cliente = db.table('fatt.cliente')
    print('\n')
    print ("\nFETCH NORMALE: colonna_testo è None")
    for row in map(dict,tbl_cliente.query(columns="@fatture.colonna_testo").fetch()):    
        row.pop('pkey')
        print ("\t", dict(row))

    print ("\nSELECTION NORMALE: colonna_testo è None")
    for row in tbl_cliente.query(columns="@fatture.colonna_testo").selection().output('dictlist'):
        row.pop('pkey')
        print ("\t", row)

    print ("\nSELECTION CON _aggregateRows: colonna_testo è ''")
    for row in tbl_cliente.query(columns="@fatture.colonna_testo").selection(_aggregateRows=True).output('dictlist'):
        row.pop('pkey')
        print ("\t", row,  "<<== DEVE ESSERE None")

    print ("\nSELECTION CON _aggregateRows e colonna rinominata: torna a essere None")
    for row in tbl_cliente.query(columns="@fatture.colonna_testo as prova").selection(_aggregateRows=True).output('dictlist'):
        row.pop('pkey')
        print ("\t", row)


    print("\nIpotesi: problema in gnrsqldata.SqlSelection._aggregateRows")
    print('''Nella riga "mixColumns = [c for c in explodingColumns if c in index and not self.colAttrs[c].get('one_one') and not( aggregateDict and (c in aggregateDict))]"''')

    print ("\nriavviami con python 002_read_aggregate.py")

if __name__ == '__main__':
    gnrapp = GnrApp('sandbox')
    db = gnrapp.db
    
    main(db)
    db.commit()