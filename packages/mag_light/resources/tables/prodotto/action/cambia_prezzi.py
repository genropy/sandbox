# -*- coding: UTF-8 -*-

from __future__ import print_function
from gnr.web.batch.btcaction import BaseResourceAction
from decimal import Decimal
from time import sleep
import os 

caption = 'Aggiorna prezzi' #nome nel menu dei batch
tags = 'admin'  #autorizzazione al batch
description =  'Aggiorna prezzi del prodotto' #nome piu completo

class Main(BaseResourceAction):
    batch_prefix = 'prz' #identificatore di batch (univoco)
    batch_title = 'Aggiorna prezzi' #titolo all'interno del visore del batch
    batch_delay = 0.5  #periodo campionamento termometro
    batch_steps='main'
    batch_cancellable = True
    #batch_selection_savedQuery = 'nomequerysalvata' #inserire solo se presente

    def step_main(self):
        
        print('page_id',self.db.currentPage.page_id)
        selection = self.get_selection() #ottiene la selezione corrente in griglia
                                         #con nessun record selezionato tutti i record visibili in griglia
        print('selezione presa',len(selection))
        if not selection:
            self.batch_debug_write('Nessun record trovato')
            return
        incr_perc = self.batch_parameters.get('percentuale') or 2
        ritardo = self.batch_parameters.get('ritardo') or 3
        if not incr_perc:
            return
        incr_perc = Decimal(incr_perc/100)
        records = self.get_records(for_update=True) #dalla selezione corrente ottiene un iteratore in formato record
        maximum = len(self.get_selection())
        iteratore_prodotti = self.btc.thermo_wrapper(records,message=self.messaggio_termometro, maximum=maximum) 
        
        #il metodo thermo_wrapper ottiene un iteratore che scorrendo ogni elemento aggiorna il termometro 
        for record in iteratore_prodotti:
            oldrecord = dict(record)
            record['prezzo_unitario'] += record['prezzo_unitario']*incr_perc
            self.tblobj.update(record,oldrecord) #tblobj di un batch è la table dove è situata la risorsa
            if ritardo:
                sleep(ritardo)
        self.db.commit()


    def messaggio_termometro(self,record, curr, tot, **kwargs):
        return "Prodotto %s %i/%i" %(record['codice'],curr,tot)


    def table_script_parameters_pane(self,pane,extra_parameters=None,record_count=None,**kwargs):
        fb = pane.formbuilder(cols=1,border_spacing='3px')
        fb.numberTextBox(value='^.percentuale',lbl=r'Incr./Decr. %')
        fb.numberTextBox(value='^.ritardo',lbl='Ritardo')

   #def result_handler(self):
   #    return 'Batch concluso', dict(url='url del file da scaricare', document_name='nome del file')