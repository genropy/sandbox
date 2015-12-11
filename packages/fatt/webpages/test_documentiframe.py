# -*- coding: UTF-8 -*-

# dataremote.py
# Created by Francesco Porcari on 2010-10-29.
# Copyright (c) 2010 Softwell. All rights reserved.

"""dataRemote"""


class GnrCustomWebPage(object):
    py_requires = "gnrcomponents/testhandler:TestHandlerFull"
    
    def test_1_basic(self, pane):
        """dataRemote basic example"""
        bc = pane.borderContainer(height='800px')
        fb = bc.contentPane(region='top').formbuilder()
        fb.dbSelect(value='^.fattura_id',lbl='Fatture',dbtable='fatt.fattura')
        fb.dateTextBox()
        bc.contentPane(region='center').documentFrame(resource='fatt.fattura:html_res/fattura_stampa',
                            emptyMessage='Rigenero il pdf',
                            iframe_id='iframeStampa',
                            pkey='^.fattura_id',missingContent='Notifica incompleta',
                            ultimo_aggiornamento='^.ultimo_aggiornamento',
                            _if='pkey',_delay=100)

    def test_2_ccc(self, pane):
        bc = pane.borderContainer(height='800px')
        fb = bc.contentPane(region='top').formbuilder()
        fb.textbox(value='^.src',lbl='src')
        bc.contentPane(region='center').iframe(height='100%',border=0,documentClasses=True,src='^.src')