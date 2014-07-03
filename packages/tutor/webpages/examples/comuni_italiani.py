# -*- coding: UTF-8 -*-
import datetime
from dateutil.rrule import rrule,DAILY
from dateutil.relativedelta import relativedelta as rd
from gnr.core.gnrdecorator import public_method,extract_kwargs
from gnr.core.gnrbag import Bag

class GnrCustomWebPage(object):
    
    def main(self,root,**kwargs):
        bc =root.borderContainer(height='100%',datapath='italia',
                                 margin='15px', border='1px solid silver')
                                 
        center=self.tableIndex(bc,title='Regioni',datapath='.regioni',
                           table='glbl.regione',columns='$sigla,$nome',
                           _onStart=True, grid_selected_sigla='.selected')
         
        center=self.tableIndex(center,title='Province',datapath='.province',
                           table='glbl.provincia',columns='$sigla,$nome',
                           where="$regione = :regione",
                           regione='^italia.regioni.selected',
                           grid_selected_sigla='.selected')
                           
        pane=self.tableIndex(center,title='Comuni',datapath='.comuni',
                           table='glbl.comune',columns='$denominazione',
                           where="$sigla_provincia = :provincia",
                           provincia='^italia.province.selected',
                           grid_selected_denominazione='.selected')
                           
        pane.htmliframe(width='100%',height='100%',
                        src='^.wikipedia',border=0)
        pane.dataFormula('.wikipedia',"'http://it.wikipedia.org/wiki/'+comune",
                     comune='^italia.comuni.selected',_if='comune',_else="'/'")
                     
    @extract_kwargs(grid=True)
    def tableIndex(self,bc,title=None,datapath=None,table=None,columns=None,
                        where=None,grid_kwargs=None,**kwargs):
                        
        pane=bc.borderContainer(region='left',width='180px',datapath=datapath,
                            splitter=True)
                            
        pane.contentPane(region='top').div(title,text_align='center',
                                           color='white',background_color='#444')
                                           
        pane.contentPane(region='center',overflow='auto').quickGrid(value='^.data',
                                             height='100%',width='100%',
                                             border_right='1px solid silver',
                                             autoSelect=True,**grid_kwargs)
                                             
        pane.dataRpc('.data',self.fillGrid,table=table,where=where,
                       columns=columns,**kwargs)
                       
        return bc.borderContainer(region='center') 
        
    @public_method
    def fillGrid(self, table=None, columns=None, where=None, **kwargs):
        table=self.db.table(table)
        result=Bag()
        selection=table.query(columns=columns,addPkeyColumn=False,
                           where=where,**kwargs).fetch()
        for k,record in enumerate(selection):
            result.setItem('r_%i' % k,Bag(record))
        return result
        
