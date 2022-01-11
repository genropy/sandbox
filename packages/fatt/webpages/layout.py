# -*- coding: UTF-8 -*-
class GnrCustomWebPage(object):

    def main(self,root,**kwargs):

        py_requires = """gnrcomponents/testhandler:TestHandlerFull,th/th:TableHandler"""
 

        root.data('dim.top.height','50%')
        root.data('dim.top.left.width','30%')
        root.data('dim.top.left.top.height','50%')
        root.data('dim.top.center.top.height','80%')
        root.data('dim.top.center.top.left.width','60%')
        

        # design Form
        p=root.borderContainer(width='500px',height='300px', regions='reg.main_bc')
        top = p.borderContainer(region='top',
                                height='^dim.top.height',
                                splitter=True,
                                regions='reg.top_bc')
        center=p.contentPane(region='center').div('center',width='100%',height='100%',background='#ddd')

        t_left=top.borderContainer(region='left',
                                    width='^dim.top.left.width',
                                    datapath='.record',splitter=True,
                                    regions='reg.leftbc')
        t_center=top.borderContainer(region='center', regions='reg.topcenter_bc')

        t_l_top=t_left.contentPane(region='top',
                                    height='^dim.top.left.top.height',
                                    splitter=True).div('tlt',width='100%',height='100%',background='#ddd')
        t_l_center=t_left.contentPane(region='center').div('tlc',width='100%',height='100%',background='#ddd')        

        t_c_top=t_center.borderContainer(region='top',
                                        height='^dim.top.center.top.height', 
                                        regions='reg.topcentertop_bc', splitter=True)
        t_c_center=t_center.contentPane(region='center').div('tcc',width='100%',height='100%',background='#ddd')

        t_c_t_left=t_c_top.contentPane(region='left',
                                        width='^dim.top.center.top.left.width',splitter=True).div('tctl',width='100%',height='100%',background='#ddd')
        t_c_t_center=t_c_top.contentPane(region='center').div('tctc',width='100%',height='100%',background='#ddd')
