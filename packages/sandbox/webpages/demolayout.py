# -*- coding: UTF-8 -*-
from gnr.core.gnrdecorator import public_method
            
class GnrCustomWebPage(object):
    py_requires='mieilayout:LayoutBelli'
    def main(self,root,**kwargs):
        bc = root.borderContainer(datapath='main')
        top = bc.contentPane(region='top',height='100px',splitter=True,
                            background='pink')
        fb = top.formbuilder()
        fb.div('^gnr.page_id',lbl='Sono la pagina',_class='selectable')
        fb.filteringSelect(value='^.one.selectedPage',lbl='Selettore 1',
                            values='alfa,beta,gamma')
        fb.textbox(value='^.valore',lbl='Valore remoto')
        fb.textbox(value='^.pid',lbl='Pagina')
        fb.dataRpc(None,self.testRpc,valore='^.valore',pid='^.pid')
        fb.textbox(value='^.messaggio',lbl='Messaggio')

        bottom = bc.contentPane(region='bottom',background='silver',
                        ).div('Ciao sono il bottom',font_size='30px')
        #self.superTabbone(bc,region='center',margin='2px')
        #self.superTabbone(bc,region='right',margin='2px',width='50%')    
        tc1 = bc.superTabbone(region='left',datapath='.one',
                        margin='2px',width='50%')
        tc1.beta.attributes.update(background='lime')
        fb = tc1.beta.formbuilder()
        fb.textbox(value='^.messaggio',lbl='Messaggio')
        tc2 = bc.superTabbone(region='center',margin='2px',datapath='.two')

    @public_method
    def testRpc(self,valore=None,pid=None):
        for x in ('one','two'):
            self.setInClientData('main.%s.selectedPage' %x,valore,page_id=pid)
    