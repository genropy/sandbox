# -*- coding: UTF-8 -*-
import datetime
from dateutil.rrule import rrule,DAILY
from dateutil.relativedelta import relativedelta as rd
from gnr.core.gnrdecorator import public_method
from gnr.core.gnrbag import Bag

class GnrCustomWebPage(object):
    
    def main(self,root,**kwargs):
        bc =root.borderContainer(height='100%',datapath='italia',
                                 margin='15px', border='1px solid silver')
        left=bc.contentPane(region='left',width='200px',datapath='.regioni',
                            splitter=True)
        left.h1('Regioni')
        left.quickGrid(value='^.data',height='100%',width='auto',
                       border_right='1px solid silver',
                       selected_sigla='.selected',autoSelect=True)
        left.dataRpc('.data',self.fillGrid,table='glbl.regione',
                     columns='$sigla,$nome',_onStart=True)
        center_bc=bc.borderContainer(region='center')

        left=center_bc.contentPane(region='left',width='150px',datapath='.province',
                                   splitter=True)
        left.h1('Province')
        left.quickGrid(value='^.data',height='100%',width='auto',
                       border_right='1px solid silver',
                       selected_nome='.selected',autoSelect=True)
        left.dataRpc('.data',self.fillGrid,table='glbl.provincia',
                     columns='$sigla,$nome',where="$regione = :regione",
                     regione='^italia.regioni.selected')
        
        
    def comuni(self,tc):
        bc =tc.borderContainer(datapath='comuni')
        top=bc.contentPane(region='top',height='26px',border_bottom='1px solid silver')
        fb=top.formbuilder(cols=1)
        fb.dbSelect(value='^.pr',dbtable='glbl.provincia',lbl='Provincia')
        left=bc.contentPane(region='left',width='150px',
                            border_right='1px solid grey',splitter=True)
        left.quickGrid(value='^.data',
                        selected_denominazione='.selected_comune',width='auto')
        left.dataRpc('.data',self.getComuni, provincia='^.pr')
        
        center=bc.borderContainer(region='center')
        pane=center.contentPane(region='center')
        pane.htmliframe(width='100%',height='100%',
                        src='^.wikipedia',border=0,
                        visible='^.selected_comune')
        pane.dataFormula('.wikipedia',"'http://it.wikipedia.org/wiki/'+comune",
                     comune='^.selected_comune',_if='comune',_else="'/'")
        
    @public_method
    def fillGrid(self, table=None, columns=None, where=None, **kwargs):
        print 'table ',table, where,kwargs
        table=self.db.table(table)
        result=Bag()
        selection=table.query(columns=columns,addPkeyColumn=False,
                           where=where,**kwargs).fetch()
        for k,record in enumerate(selection):
            result.setItem('r_%i' % k,Bag(record))
        return result
        
