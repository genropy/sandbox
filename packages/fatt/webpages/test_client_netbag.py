
# -*- coding: UTF-8 -*-

"""ClientPage tester"""
from gnr.core.gnrbag import NetBag
from gnr.core.gnrdecorator import public_method


class GnrCustomWebPage(object):
    py_requires = "gnrcomponents/testhandler:TestHandlerFull"

    def test_1_lista_fatture(self, pane):
        frame = pane.framePane(height='400px')
        frame.top.slotToolbar('*,run,10').run.slotButton('Run',action='FIRE .run;')
        bc = frame.center.borderContainer()
        top = bc.contentPane(region='top')
        fb = top.formbuilder(cols=2,border_spacing='3px')
        fb.textbox(value='^.cliente',lbl='Cliente',width='20em')
        fb.numberTextBox(value='^.importo',lbl='Importo',width='6em')
        fb.checkboxtext(value='^.columns',lbl='Columns',colspan=2,
                        cols=1,popup=True,
                        values=','.join(['$%s' %k for k in self.db.table('fatt.fattura').model.columns.keys()]),
                        width='40em')
        center = bc.contentPane(region='center')
        center.quickGrid('^.result')
        frame.dataRpc('.result',self.netBagCallListaFatture,cliente='=.cliente',importo='=.importo',
                        columns='=.columns',_fired='^.run')

    def test_2_lista_fatture_more_params(self, pane):
        frame = pane.framePane(height='400px')
        frame.top.slotToolbar('*,run,10').run.slotButton('Run',action='FIRE .run;')
        bc = frame.center.borderContainer()
        top = bc.borderContainer(region='top',height='150px')
        fb = top.contentPane(region='left').formbuilder(cols=1,border_spacing='3px')
        fb.textbox(value='^.cliente',lbl='Cliente',width='20em')
        fb.numberTextBox(value='^.importo',lbl='Importo',width='6em')
        fb.checkboxtext(value='^.columns',lbl='Columns',colspan=2,
                        cols=2,
                        values=','.join(['$%s' %k for k in self.db.table('fatt.fattura').model.columns.keys()]),
                        width='40em')
        right = top.borderContainer(region='center',margin='2px')
        right.contentPane(region='top').div('Parametri supplementari',padding='3px',background='#707070',color='white',text_align='center',rounded_top=4)
        right.contentPane(region='center').multiValueEditor(value='^.querykwargs',grid_tools_position='BR',
                                                        grid_border='1px solid #efefef',margin='2px')
        center = bc.contentPane(region='center',margin='1px',border='1px solid #efefef')
        center.quickGrid('^.result')
        frame.dataRpc('.result',self.netBagCallListaFatture,cliente='=.cliente',importo='=.importo',
                        columns='=.columns',querykwargs='=.querykwargs',_fired='^.run')


    @public_method
    def netBagCallListaFatture(self,cliente=None,importo=None,columns=None,querykwargs=None,**kwargs):
        querykwargs = querykwargs.asDict(ascii=True)
        return  NetBag('http://external:3xt3rn4l@localhost:8081/fatt/test_netbag','lista_fatture',cliente=cliente,importo=importo,
                            columns=columns,
                            output='v',**querykwargs)



