#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method,extract_kwargs
from gnr.web.gnrwebstruct import struct_method

class ButtonSetComponent(BaseComponent):
    @extract_kwargs(condition=True,btn=True)
    @struct_method
    def bt_buttonSet(self,pane,resultpath=None,storeCallback=None,**kwargs):
        buttonSetRoot = pane.div(connect_onclick="""
            var targetNode = $1.target.sourceNode;
            var pkey = targetNode.attr.pkey;
            var resultValue;
            if(targetNode.attr.isFinalValue){
                resultValue = targetNode.attr.pkey;
            }
            this.setRelativeData(this.attr.resultpath,resultValue);
            targetNode.setRelativeData('.selected_pkey',pkey);
            """
        ,resultpath=resultpath)
        buttonSetRoot.remote(self.bt_buildRemoteButtonSet,storeCallback=storeCallback,lazy=False,**kwargs)

    @public_method
    def bt_buildRemoteButtonSet(self,pane,storeCallback=None,parent_pkey=None,**kwargs):
        storeCallback = self.getPublicMethod('rpc',storeCallback)
        data = storeCallback(selected_pkey=parent_pkey)
        if not data:
            return
        container = pane.div(position='relative',border='1px solid #666',background='white',
                        z_index=1,datapath='.children',
                        shadow='5px 5px 4px #666',rounded=6,**kwargs)
        buttons = container.div(position='absolute',top='5px',bottom='5px',left='5px',right=0,overflow='auto')

        for n in data:
            buttons.div(n.value,pkey=n.attr['pkey'],_class=n.attr['_class'],
                                is_selected='==_current_selected==this.attr.pkey',
                                _current_selected='^.selected_pkey',isFinalValue=n.attr.get('isFinalValue'))
        children = container.div(position='relative', top='30px',left='30px')
        children.remote(self.bt_buildRemoteButtonSet,storeCallback=storeCallback,lazy=True,
                           parent_pkey='^.selected_pkey',_if='parent_pkey',
                           _else="SET .children=null;",**kwargs)


        