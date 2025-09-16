# -*- coding: UTF-8 -*-
from gnr.core.gnrdecorator import public_method
import requests


class GnrCustomWebPage(object):
    py_requires="gnrcomponents/testhandler:TestHandlerFull"

    def test_01_somma(self,pane,**kwargs):
        fb = pane.formlet(cols=3)
        fb.numberTextBox(value='^.a',lbl='A')        
        fb.numberTextBox(value='^.b',lbl='B')
        fb.div('^.result')
        fb.button('Invio').dataRpc('.result',
            self.eseguiTestEndpoint,
            metodo='somma',
            a='=.a',
            b='=.b'
        )
    
    def test_02_moltiplica(self,pane,**kwargs):
        fb = pane.formlet(cols=3)
        fb.numberTextBox(value='^.a',lbl='A')        
        fb.numberTextBox(value='^.b',lbl='B')
        fb.div('^.result')
        fb.button('Invio').dataRpc('.result',
            self.eseguiTestEndpoint,
            metodo='moltiplica',
            a='=.a',
            b='=.b'
        )
    def test_03_elenco_clienti(self,pane,**kwargs):
        fb = pane.formlet(cols=2)
        fb.dbSelect(value='^.provincia',lbl='Provincia',table='glbl.provincia')  
        fb.div()
        fb.checkbox('^.useAuth',lbl='Usa auth')      
        fb.button('Invio').dataRpc('.result',
            self.eseguiTestEndpoint,
            metodo='elenco_clienti',
            provincia='=.provincia',
            useAuth='=.useAuth'
        )
        fb.quickGrid('^.result',height='300px',colspan=2)

    def test_04_dati(self,pane,**kwargs):
        bc = pane.borderContainer(height='500px')
        grid = bc.contentPane(region='left',width='50%').quickGrid(value='^.ordine')
        grid.tools('delrow,addrow',title='!![en]Articoli')
        grid.column('codice', width='8em', name='!![en]Codice', edit=True)
        grid.column('quantita', width='6em', dtype='L', name='!![en]Quantità', edit=True)

        bc.contentPane(region='top').flexbox().button('Invio').dataRpc('.result',
            self.eseguiTestEndpoint,
            metodo='controlla_ordine',
            ordine='=.ordine',
        )
        bc.contentPane(region='center').quickGrid('^.result')

    @public_method
    def eseguiTestEndpoint(self,metodo=None,useAuth=False,**kwargs):
        """Esegue una POST verso l'endpoint esterno inviando i parametri.
        Parametri:
        - metodo: nome del metodo remoto da invocare (es. 'somma')
        - **kwargs: parametri da inoltrare al metodo remoto
        Ritorna il contenuto della risposta (JSON se possibile, altrimenti testo).
        """
        url = 'http://127.0.0.1:8083/fatt/endpoint'
        if useAuth:
            url = self.dev.authenticatedUrl(url,user='ext',password='provaext')
        result = self.site.callGnrRpcUrl(url,metodo,**kwargs)
        print(result)
        return result