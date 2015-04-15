# -*- coding: UTF-8 -*-

from gnr.core.gnrdecorator import public_method
from gnr.core.gnrbag import Bag

class GnrCustomWebPage(object):
    def main(self,root,**kwargs):
        root.attributes['overflow'] = 'hidden'
        bc = root.borderContainer(height='100%')
        header = bc.contentPane(region='top',background='silver',height='23px')
        header.div('Query tester',font_weight='bold',color='#666',text_align='center',
                  font_size='18px')
        center = bc.borderContainer(region='center')
        top = center.borderContainer(region='top',height='200px',datapath='query')
        fb = top.contentPane(region='center').div(margin='15px',margin_right='25px').formbuilder(cols=2,border_spacing='3px',width='100%')
        fb.textbox('^.table',lbl='Table',validate_notnull=True)
        fb.checkbox('^.distinct',label='Distinct')
        fb.simpleTextArea('^.columns',lbl='Columns',colspan=2)
        fb.simpleTextArea('^.where',lbl='Where',colspan=2)
        fb.textbox('^.order_by',lbl='Order by',colspan=2,width='100%')
        fb.textbox('^.group_by',lbl='Group by',colspan=2,width='100%')
        fb.textbox('^.limit',lbl='Limit',width='5em')
        fb.button('Run Query',fire='runquery')
        parsgrid = top.contentPane(region='right',width='325px').quickGrid('^.pars')
        parsgrid.tools('addrow,delrow')
        parsgrid.column('name',edit=True,width='12em',name='Name')
        parsgrid.column('dtype',edit=dict(tag='filteringSelect',values='T:Text,N:Number,D:Date'),width='7em',name='Type')
        parsgrid.column('value',edit=True,width='12em',name='Value')
        bc.dataRpc('result',self.getSelectionData,query='=query',
                   _if='_table',_table='=query.table',_fired='^runquery')
        
        tc = center.tabContainer(region='center',margin='2px')
        tc.contentPane(title='Result').quickGrid('^result.data')
        tc.contentPane(title='Sql').pre('^result.sql')
        bc.contentPane(region='bottom',height='30px').div('^result.error')


    @public_method
    def getSelectionData(self,query=None):
        q = None
        try:
            table = query.pop('table')
            pars = query.pop('pars') or Bag()
            parsdict = query.asDict(ascii=True)
            for p in pars.values():
                parsdict[p['name']] = self.catalog.fromText(p['value'],p['dtype'] or 'T')
            q = self.db.table(table).query(addPkeyColumn=False,**parsdict)
            data = Bag()
            result = Bag(dict(data=data,sql=q.sqltext))
            f = q.fetch()
            for i,r in enumerate(f):
                data['r_%i' %i] = Bag(r)
        except Exception, e:
            error=str(e)
            result = Bag(data=Bag(),sql=q.sqltext if q else error,error=error)
        return result
