#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class Bottoniera(BaseComponent):
    def bottonieraProdotti(self,pane,datapath=None):
        bc = pane.borderContainer(datapath=datapath)
        dati_prodotto = self.datiProdotti()
        bc.css('.box_bottoni',"""margin:10px; padding:10px; border-radius:6px;""")

        bc.css('.bottone',"""border:1px solid green; padding:10px; display:inline-block;""")
        self.pannelloTop(bc.contentPane(region='top',
                       height='120px'),dati_prodotto=dati_prodotto)
        self.pannelloCenter(bc.contentPane(region='center'))

    def pannelloCenter(self,pane):
        pane.remote(self.costruisciProdotti,prodotto_id='^.prodotto_id')

    @public_method
    def costruisciProdotti(self,pane,prodotto_id=None):
        if not prodotto_id:
            pane.div('Seleziona un tipo prodotto')
            return
        prodotti_tbl = self.db.table('fatt.prodotto')
        prodotti = prodotti_tbl.query(where="@prodotto_tipo_id.hierarchical_pkey LIKE :prodotto_id",
                            prodotto_id='%s%%' %prodotto_id).fetch()
        box = pane.div(_class='box_bottoni',background='^.background',color='^.color')
        for p in prodotti:
            box.div("%(codice)s-%(descrizione)s" %p,_class='bottone',margin='==margine+"px"',margine='^.margine')
       
    def pannelloTop(self,pane,dati_prodotto=None):
        fb = pane.formbuilder(cols=1,border_spacing='3px')
        fb.filteringSelect(value='^.background',values='red,silver,green,yellow',lbl='background')
        fb.filteringSelect(value='^.color',values='red,silver,green,yellow',lbl='color')

        fb.horizontalSlider('^.margine',lbl='',minimum=0,maximum=59,
                               width='160px',intermediateChanges=True)
        
        box = pane.div(_class='box_bottoni')
        for pkey,nome in dati_prodotto['root'].digest('#a.pkey,#a.caption'):
            box.div(nome,_class='bottone',
                    connect_onclick="SET .prodotto_id = this.attr.prodotto_id;",
                    prodotto_id=pkey)
        
    def pannelloAlbero(self,pane,dati_prodotto=None):
        pane.data('.store',dati_prodotto)
        pane.tree(storepath='.store',
                     labelAttribute='caption',
                     hideValues=True,
                     connect_ondblclick="alert('hello')")
        
    def datiProdotti(self):
        tbl_tipi_prodotto = self.db.table('fatt.prodotto_tipo')
        return tbl_tipi_prodotto.getHierarchicalData()