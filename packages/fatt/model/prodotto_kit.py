# encoding: utf-8

class Table(object):

    def config_db(self,pkg):
        tbl = pkg.subtable('prodotto_kit', maintable='fatt.prodotto',
                         name_long='Kit prodotto', 
                         name_plural='Kit prodotti',
                         relation_name='kit_prodotti')

        #copia tutte le colonne di prodotto        
        tbl.column('numero_componenti',dtype='L')        
        tbl.column('distinta', dtype='X', name_long='Distinta')

    def trigger_onInserting(self,record=None):
        print('Inserting in kit')


    def trigger_onUpdating(self,record=None,old_record=None):
        print('Updating in kit')