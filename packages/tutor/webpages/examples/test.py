# -*- coding: UTF-8 -*-


class GnrCustomWebPage(object):
    def main(self,root,**kwargs):
        bc = root.borderContainer(datapath='main')
        top = bc.contentPane(region='top')
        fb = top.formbuilder(cols=1,border_spacing='3px')
        fb.textbox(value='^.libro',lbl='Libro')
        fb.textbox(value='^.tipo_idea',lbl='Tipo idea')
        center = bc.contentPane(region='center')
        contenuto = self._T("Sei sicuro che %s sia furbo in data %s?") %(self.user,self.workdate)
        center.div(contenuto)
