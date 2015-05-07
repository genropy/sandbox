# -*- coding: UTF-8 -*-


class GnrCustomWebPage(object):
    def main(self,root,**kwargs):
        bc = root.borderContainer(datapath='main')
        top = bc.contentPane(region='top')
        fb = top.formbuilder(cols=1,border_spacing='3px')
        fb.textbox(value='^.libro',lbl='!!Book')
        fb.textbox(value='^.tipo_idea',lbl='!!Kind of idea')
        center = bc.contentPane(region='center')
        fb.div(self._T("Are you sure %s? Is a good idea to %s?") %(self.user,self.workdate),lbl='rrr')
        fb.div(self._T("Are you sure %(name)s? Is a good idea to %(data)s?") %dict(name=self.user,data=self.workdate),lbl='bbb')

        fb.filteringSelect(value='^.test',values='small:[!!Small],medium:[!!Medium],large:[!!Large]')