from gnr.web.gnrbaseclasses import BaseComponent
from gnr.web.gnrwebstruct import struct_method
from gnr.core.gnrdecorator import public_method

class LayoutBelli(BaseComponent):

    @struct_method
    def layoutbelli_superTabbone(self,parent,datapath=None,**kwargs):
        tc = parent.tabContainer(datapath=datapath,
                                selectedPage='^.selectedPage',
                                subscribe_tabboneReset="SET .selectedPage='alfa';",
                                **kwargs)
        self.makeTab(tc,title='Alfa',childname='alfa',
                                datapath='.alfa',
                                pageName='alfa')
        self.makeTab(tc,title='Beta',childname='beta',
                                datapath='.beta',
                                pageName='beta')
        self.makeTab(tc,title='Gamma',childname='gamma',
                                datapath='.gamma',
                                pageName='gamma')
        tc.contentPane(title='Altri',pageName='altri',
                        datapath='.altri',childname='altri').remote(self.altriTab)
        return tc


    def makeTab(self,tc,**kwargs):
        alfa = tc.contentPane(**kwargs)
        fb = alfa.formbuilder()
        fb.textbox(value='^.nome',lbl='Nome')
        fb.textbox(value='^.cognome',lbl='Cognome')

    @public_method
    def altriTab(self,pane):
        pane.superTabbone()


        
