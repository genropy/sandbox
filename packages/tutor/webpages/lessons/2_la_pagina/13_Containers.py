# -*- coding: UTF-8 -*-
import datetime
from dateutil.rrule import rrule,DAILY
from dateutil.relativedelta import relativedelta as rd
class GnrCustomWebPage(object):
    
    def main(self,root,**kwargs):
        self.testTc(root.div(datapath='testTc',margin='10px'))
        self.testBc(root.div(datapath='testBc',margin='10px'))
        
        
    def testTc(self,pane):
        tc=pane.tabContainer(height='300px',width='550px')
        c=tc.contentPane(title='Clock',datapath='.clock',padding='5px')
        c.div('^.showtime',font_size='130px',text_align='center',
              margin_top='50px',color='#2A7ACC')
        c.dataFormula('.showtime',"_F(new Date(),'hh:mm:ss','H')",
                               _timing=1)
        notes = tc.contentPane('^.text',title='Notes',datapath='.notes',
                               padding='5px')
        notes.simpleTextArea(height='100%',width='100%',editor=True)
        innertc=tc.tabContainer(title='Calendar',margin='4px',
                                datapath='.calendar',height='100%')
        for week in range(4):
            self.makeWeek(innertc,week)

    def makeWeek(self,pane,week=None):
        tw=pane.contentPane(title='Week %i' % week,
                                   datapath='.week_%i' % week)
        statuslist='F:Free,H:Home,W:Work,T:Travel'
        dtstart=datetime.date.today()
        dtstart=dtstart+rd(dtstart,weeks=week)
        tb=tw.table(margin='5px').tbody()
        h=tb.tr(datapath='week_%i')
        h.td()
        days=[d.strftime('%d/%m/%y') for d in rrule(DAILY, count=7, dtstart=dtstart)]
        for d in days:
            h.td(d,align='center')
        for h in range (8,18):
            r=tb.tr()
            r.td('%i:00'%h,align='right')
            for d in days:
                r.td().filteringSelect('^.%s.%i' %(d,h),width='5em',values=statuslist)
    
    
    def testBc(self,pane):

        bc=pane.borderContainer(height='300px',width='550px',
                                border='1px solid silver',rounded=8)
                                
        top=bc.contentPane(region='top',height='20px',background_color='silver')
        pages='small:Small,medium:Medium,large:Large'
        top.filteringSelect('^.page',values=pages,width='10em')
        
        fb=bc.contentPane(region='left',width='150px',
                            border_right='1px solid silver',
                            splitter=True).formbuilder(cols=1)
        fb.checkBox('^.italic',label='Italic')
        fb.checkBox('^.bold',label='Bold')
        fb.checkBox('^.underline',label='Underline')
        fb.checkBox('^.small_caps',label='Small Caps')
        fb.dataController(""" var style='font-weight:'+(bold?'bold':'normal');
                                  style+=';font-style:'+(italic?'italic':'normal');
                                  style+=';text-decoration:'+(underline?'underline':'none');
                                  style+=';font-variant:'+(small_caps?'small-caps':'normal')+';';
                                  SET .style = style;
                          """,italic='^.italic',bold='^.bold',
                             underline='^.underline', small_caps='^.small_caps')
        center=bc.stackContainer(region='center',margin='3px',selectedPage='^.page')
        for k,p in enumerate(pages.split(',')):
            pageName,title=p.split(':')
            c=center.contentPane(pageName=pageName,style='^.style')
            c.div(title,padding='20px',font_size='%ipx' % (20*(k+1)))

        bottom=bc.borderContainer(region='bottom',height='22px',
                                  background_color='silver')
        b_left=bottom.contentPane(region='left',width='60px').button('Clear',action='alert("Clearing...")')
        b_right=bottom.contentPane(region='right',width='60px').button('Submit',action='alert("Submitting...")')
        c_center=bottom.contentPane(region='center')
        c_center.div('Genropy',text_align='center',font_size='20px')
       
        
        
                    
                  
                    
        
       
        
        
        


        
   
