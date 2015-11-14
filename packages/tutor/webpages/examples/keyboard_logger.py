# -*- coding: UTF-8 -*-

class GnrCustomWebPage(object):
    def main(self,root,**kwargs):
        root.css('.event_type_keydown',"color:red;font-weight:bolder;")
        root.css('.event_type_keypress',"color:green; font-weight:bolder;")
        root.css('.past_event',"opacity:0.5;font-weight:normal; font-style:italic;")

        bc = root.borderContainer(datapath='logger')
        fb = bc.contentPane(region='top',border_bottom='1px solid silver').formbuilder(cols=2)
        fb.input(value='^.curval',lbl='Test input',
                 connect_onkeydown='genro.publish("log_event",{evt:$1});',
                 connect_onkeypress='genro.publish("log_event",{evt:$1});')
        fb.button('Clear',action='SET .logdata = null;SET .curval=null;')
        bc.dataController("""
                if(!data){
                    data = new gnr.GnrBag();
                }else{
                    data = data.deepCopy();
                    if(data.len()>1){
                        data.setItem('#1?_customClasses',data.getItem('#1?_customClasses')+' past_event');
                    }
                }
                var row = new gnr.GnrBag();
                columns.forEach(function(c){ console.log(c,evt[c]);row.setItem(c,evt[c]) });
                data.setItem('#id',row,{_customClasses:'event_type_'+evt.type},{_position:'<'});
                if(data.len()>10){data.popNode('#11');}
                SET .logdata = data;
                evt.target.value = null;
            """,data='=.logdata',subscribe_log_event=True,
                columns=['type','charCode','keyIdentifier','keyChar','shiftKey','altKey','ctrlKey','metaKey']
                )
        center = bc.contentPane(region='center',margin='2px')
        center.quickGrid(value='^.logdata')

