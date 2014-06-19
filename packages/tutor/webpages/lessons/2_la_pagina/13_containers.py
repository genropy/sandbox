# -*- coding: UTF-8 -*-
"""The first example of Genropy page"""

class GnrCustomWebPage(object):
    
    def main(self,root,**kwargs):
        self.testTabContainer(root.div(margin='10px',height='150px', width='500px',datapath='testTabContainer'))
        self.testBorderContainer(root.div(margin='10px',height='250px', width='500px',datapath='testBorderContainer'))
        self.testStackContainer(root.div(margin='10px',height='250px', width='500px',datapath='testStackContainer'))
        
    def testTabContainer(self,pane):
        tc=pane.tabContainer(height='100%')
        tc.contentPane(title='Alfa',padding='20px').div('Alfa',font_size='30px')
        tc.contentPane(title='Bravo',padding='20px').div('Bravo',font_size='30px')
        tc.contentPane(title='Charlie',padding='20px').div('Charlie',font_size='30px')
        
    def testBorderContainer(self,pane):
        bc=pane.borderContainer(height='100%',border='1px solid silver')
        bc.contentPane(region='left',width='100px',splitter=True,
                       border_right='1px solid silver').div('Left',font_size='12px')
        bc.contentPane(region='right',width='100px',
                       border_left='1px solid silver').div('Right',font_size='12px')
        bc.contentPane(region='top',height='40px',
                       border_bottom='1px solid silver').div('Top',font_size='12px')
        bc.contentPane(region='bottom',height='40px',
                       border_top='1px solid silver').div('Bottom',font_size='12px')
        self.testTabContainer(bc.contentPane(region='center'))
    
    def testStackContainer(self,pane):
        bc=pane.borderContainer(height='100%',border='1px solid silver')
        
        sc=bc.StackContainer(region='center',selected='^.selected')
        sc.contentPane(padding='20px').div('1',font_size='60px')
        sc.contentPane(padding='20px').div('2',font_size='60px')
        sc.contentPane(padding='20px').div('3',font_size='60px')
        sc.contentPane(padding='20px').div('4',font_size='60px')
        sc.data('.selected',1)
        fb=bc.contentPane(region='bottom',height='27px',
                              border_top='1px solid silver').formbuilder(cols=3)
        fb.button('<---',action="SET .selected= p-1",p='^.selected',
                                       disabled='== (p <= 0)')
        fb.div('^.selected',width='2em',_class='fakeTextBox',text_align='center')
        fb.button('--->',action="SET .selected= p+1",p='^.selected',
                                       disabled='== (p >= 3)')

