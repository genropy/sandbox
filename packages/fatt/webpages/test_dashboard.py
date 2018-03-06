# -*- coding: UTF-8 -*-
#from gnr.core.gnrbag import Bag
from gnr.core.gnrdecorator import public_method
from gnr.core.gnrbag import DirectoryResolver

class GnrCustomWebPage(object):
    py_requires='gnrcomponents/dashboard_component/dashboard_component:DashboardGallery'

    def main(self,root,**kwargs):
        bc = root.borderContainer()
        bc.dashboardGallery(pkg='fatt',code='generale',region='center')

    def main_zzz(self,root,**kwargs):
        bc = root.borderContainer()
        top = bc.contentPane(region='top',height='100px')
        bottom = bc.contentPane(region='bottom',height='100px')
        bc.contentPane(region='left',width='100px')
        bc.contentPane(region='right',width='100px')

        top.dashboardItem(table='fatt.cliente',
                            itemName='report_acquisti',
                            testo='prova 1',color='red',font_size='15pt')
        bottom.dashboardItem(table='fatt.cliente',
                            itemName='report_acquisti',
                            testo='prova 2',color='green',font_size='20pt')
        bc.contentPane(region='center')
