# -*- coding: UTF-8 -*-


class GnrCustomWebPage(object):
    def main(self,root,**kwargs):
        fb = root.formbuilder(cols=1,border_spacing='3px',datapath='test')
        fb.textbox(value='^.foo',lbl='Test',
                                 connect_onkeypress="""
                                    var b = new gnr.GnrBag();
                                    var v;
                                    for(var k in $1){
                                        v = $1[k];
                                        if(typeof(v)=='function' || typeof(v)=='object'){
                                            continue;
                                        }
                                        b.setItem(k,$1[k]);
                                    }
                                    SET .output = b.getFormattedValue()
                                 """)
        fb.div('^.output',lbl='Output')
