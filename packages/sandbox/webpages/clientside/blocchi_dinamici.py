# -*- coding: utf-8 -*-

from gnr.core.gnrdecorator import public_method
from gnr.core.gnrbag import Bag
from time import sleep

class GnrCustomWebPage(object):
    py_requires = "gnrcomponents/testhandler:TestHandlerBase"
    
    def test_01_remoteParametrico(self, pane):
        "Remote"
        bc = pane.borderContainer(height='300px')
        fb = bc.contentPane(region='top').formbuilder(cols=1)
        fb.dbSelect(value='^.regione',dbtable='glbl.regione',lbl='Regione')
        bc.contentPane(region='center').remote(
            self.blocchiProvincia,regione='^.regione'
        )
    
    @public_method
    def blocchiProvincia(self,pane,regione=None,**kwargs):
        if not regione:
            pane.div('Seleziona la regione!!!')
            return
        tab = pane.tabContainer(margin='2px')
            
        province = self.db.table('glbl.provincia').query(where='$regione=:reg',reg=regione).fetch()
        for pr in province:
            paneProv = tab.contentPane(title=pr['nome'])
            fb = paneProv.formbuilder(datapath=f'.{pr["sigla"]}')
            fb.textbox(value='^.annotazioni',lbl='Annotazioni a riguardo')


    def test_02_remoteLazy(self, pane):
        "Remote lazi"
        tc = pane.tabContainer(height='300px')
        tc.contentPane(title='Pagina 1').simpleTextArea(value='^.testolibero')
        tc.contentPane(title='Pagina lazy').remote(self.paginaLazy,_waitingMessage='Attendere prego')
    
    @public_method
    def paginaLazy(self,pane):
        sleep(3)
        pane.div('contenuto remoto pesantuccio')

    

    def test_03_costruzioneDinamica(self, pane):
        bc = pane.borderContainer(height='300px')
        fb = bc.contentPane(region='top').formbuilder(cols=1)
        fb.textBox(value='^.titoli_tabs',lbl='Titoli')
        miaradice = bc.contentPane(region='center')
        bc.dataController(
            """
            let tc = myroot._('tabContainer','contenitore');
            if(!titoli_tabs){
                return;
            }
            titoli_tabs.split(',').forEach(function(titolo){
                let pannelloInterno = tc._('ContentPane',{title:titolo,datapath:`.${titolo}`});
                pannelloInterno._('div',{innerHTML:titolo});
                pannelloInterno._('textbox',{value:'^.contenuto'});
            });
            """,
            myroot = miaradice,
            titoli_tabs='^.titoli_tabs'
        )

