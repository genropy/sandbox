#!/usr/bin/env python
# encoding: utf-8

class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('prodotto', pkey='id', name_long='!![it]Prodotto', 
                        name_plural='!![it]Prodotti',
                        caption_field='descrizione')
        self.sysFields(tbl)
        tbl.column('codice' ,size=':10',name_long='!![it]Codice')
        tbl.column('descrizione' ,size=':50',name_long='!![it]Descrizione')
        tbl.column('prodotto_tipo_id',size='22' ,group='_',name_long='!![it]Tipo Prodotto',name_short='Tipo').relation('prodotto_tipo.id',relation_name='prodotti',mode='foreignkey',onDelete='raise')
        tbl.column('prezzo_unitario',dtype='money',name_long='!![it]Prezzo unitario',name_short='P.U')
        tbl.column('tipo_iva_codice',size=':5' ,group='_',name_long='!![it]Tipo iva').relation('tipo_iva.codice',relation_name='prodotti',mode='foreignkey',onDelete='raise')
        tbl.column('foto_url' ,dtype='P',name_long='!![it]Foto',name_short='Foto')
        tbl.column('caratteristiche',dtype='X',name_long='!![it]Caratteristiche',subfields='prodotto_tipo_id')

    def onDuplicating_many(self, record, copy_number=None, copy_label=None):
        #Il metodo onDuplicating_many consente la copia multipla dei record dall'apposita icona nella Form tenendo premuto 
        #il tasto Maiusc. Riceve, oltre al record, copy_number (I) e copy_label (T)    

        record['descrizione'] = '{descrizione} {label}'.format(descrizione=record['descrizione'], label=copy_label)
        #Aggiungiamo alla descrizione la label personalizzata (es: 'PP1,PP2,PP3')

        #record['descrizione'] = '{descrizione} / Copia num. {number}'.format(descrizione=record['descrizione'], number=copy_number+1)
        #Aggiungiamo alla descrizione il numero della copia (es: 5). Aggiungiamo +1 perché copy_number comincia con 0
    
    def trigger_onInserting(self,record=None):
        print('Inserting in prodotto')


    def trigger_onUpdating(self,record=None,old_record=None):
        print('Updating in prodotto')