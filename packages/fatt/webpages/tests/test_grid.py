# -*- coding: utf-8 -*-

# includedview_bagstore.py
# Created by Francesco Porcari on 2011-03-23.
# Copyright (c) 2011 Softwell. All rights reserved.

from gnr.core.gnrdecorator import public_method
from gnr.core.gnrbag import Bag

class GnrCustomWebPage(object):
    py_requires="""gnrcomponents/testhandler:TestHandlerFull,
                    th/th:TableHandler,gnrcomponents/framegrid:FrameGrid"""

    def test_0_tablehandler_virtual(self,pane):
        """Comuni con ricerca estesa e store virtuale"""
        pane.plainTableHandler(table='glbl.comune',virtualStore=True,
                                extendedQuery=True,height='600px')


    def test_1_tablehandler_static(self,pane):
        """Comuni della provincia di Milano"""
        pane.plainTableHandler(table='glbl.comune',
                                #condition='$sigla_provincia=:sig',
                                #condition_sig='MI',
                                view_store_onStart=True,
                                height='600px')

    def test_2_tablehandler_static(self,pane):
        """Edit clienti"""
        pane.inlineTableHandler(table='fatt.cliente',
                                view_store_onStart=True,
                                autoSave=True,
                                viewResource='ViewEditable',
                                height='600px')

    def test_3_baggrid(self,pane):
        pane.bagGrid(storepath='.storedischi',
                    datapath='.grigliadischi',
                    struct=self.struttura_dischi,
                    height='600px',width='500px')
    
    def struttura_dischi(self,struct):
        r=struct.view().rows()
        r.cell('titolo',name='Titolo',width='20em',edit=True)
        r.cell('n_tracce',name='N.Tracce',dtype='L',width='5em',
                edit=True,totalize=True)
        r.cell('genere',name='Genere',edit=dict(tag='combobox',
                    values='rock,classical,pop,folk'),width='10em')


    def test_4_baggrid_province(self,pane):
        province = self.db.table('glbl.provincia').query().fetch()
        b = Bag()
        for p in province:
            b[p['sigla']] = Bag(dict(p))
        pane.data('.provincegrid.store',b)
        pane.bagGrid(storepath='.store',
                    datapath='.provincegrid',
                    struct=self.struttura_prov,
                    height='600px',width='500px')
    
    def struttura_prov(self,struct):
        r=struct.view().rows()
        r.cell('sigla',name='Sigla',width='4em',edit=True)
        r.cell('regione',name='Regione',width='5em',edit=True)
 