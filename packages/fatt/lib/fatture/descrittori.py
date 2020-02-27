# from __future__ import division
# from past.utils import old_div

from gnr.core.gnrstructures import GnrStructData, valid_children
from gnr.core.gnrbag import Bag

class FatturaStruttura(GnrStructData):
    default_childname = '*'

    @valid_children(riga_fattura='1:')
    def fattura(self, cliente_id=None, data=None):
        return self.child('fattura', cliente_id=cliente_id, data=data)

    @valid_children()
    def riga_fattura(self, prodotto_id=None, quantita=None):
        return self.child('riga_fattura', prodotto_id=prodotto_id, quantita=quantita)

class FattureManager(object):
    def __init__(self, db):
        self.db = db

        self.fattura_record = GnrStructData() # o Bag() ?
        self.tblfattura = self.db.table('fatt.fattura')
        self.tblfatturariga = self.db.table('fatt.fattura_riga')

    def creaDescrittoreFattura(self, fattura_id): # fattura_corrente
        fattura_corrente = self.tblfattura.record(fattura_id, mode='bag')
        
        self.fattura_record = FatturaStruttura() # creo lo scheletro della Fattura in formato Struct
        fatt = self.fattura_record.fattura(cliente_id=fattura_corrente['cliente_id'], data=self.db.workdate) # inserisco i dati della "testata" e mi posiziono, per così dire, a questo livello
        
        # adesso localizza le righe di questa fattura_corrente perché dobbiamo caricarle nella Struct
        righe_correnti = self.tblfatturariga.query(where='$fattura_id = :fattura_id', fattura_id=fattura_corrente['id']).fetch()

        for riga in righe_correnti: # nella 'struttura' della fattura inserisce le righe usando i dati delle righe originali
            fatt.riga_fattura(prodotto_id=riga['prodotto_id'], quantita=riga['quantita'] )

    def scriviFatturaDaDescrittore(self):
        self.fattura_record.validate()

        self.tblfattura.insert(self.fattura_record.getAttr('fattura'))
        
        for riga_node in self.fattura_record['fattura']: # mmm ogni riga è un BagNode
            riga_record = riga_node.attr
            riga_record['fattura_id'] = self.fattura_record.getAttr('fattura', 'id')
            self.tblfatturariga.insert(riga_record)

        self.db.commit()
