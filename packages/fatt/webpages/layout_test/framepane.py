# -*- coding: UTF-8 -*-
from gnr.core.gnrdecorator import public_method
            
class GnrCustomWebPage(object):
    py_requires='mieilayout:LayoutBelli'
    def main(self,pane,**kwargs):
        frame = pane.framePane(margin='4px',rounded=10,
                            border='1px solid silver',
                            datapath='myframe')
        toolbar = frame.top.slotToolbar('2,mytitle,selettore,*,stackButtons,*,salva,20,cancella,2',
                            closable=True)
        toolbar.mytitle.div('Mio frame')
        toolbar.selettore.filteringSelect(value='^.currentStack',
                    values='ciao,miao,bao')
        toolbar.salva.button('Salva',action='alert("Salvo")')
        toolbar.cancella.button('Cancella',action='alert("cancella")')

        frame.bottom.div('piero',background='red',color='white')
        sc = frame.center.stackContainer(selectedPage='^.currentStack')
        sc.contentPane(title='Ciao',pageName='ciao',).div('ciao')
        sc.contentPane(title='Miao',pageName='miao').div('miao')
        sc.contentPane(title='Bao',pageName='bao').superTabbone(datapath='bao')