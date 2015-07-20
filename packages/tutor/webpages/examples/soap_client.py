# -*- coding: UTF-8 -*-
from gnr.core.gnrbag import Bag
from gnr.core.gnrdecorator import public_method
from suds.client import Client

class GnrCustomWebPage(object):
    def main(self,root,**kwargs):
        frame = root.framePane('main',datapath='main')
        frame.data('.url','http://www.webservicex.com/globalweather.asmx?WSDL')
        bar = frame.top.slotToolbar('2,urlfield,10,runbutton,*',height='20px')
        fb = bar.urlfield.formbuilder(cols=1,onEnter='FIRE .run;',border_spacing='3px') 
        fb.textbox('^.url',lbl='Url',width='30em')
        bar.runbutton.button('Run',fire='.getWsdl')
        bar.dataRpc('.result',self.getWsdl,_fired='^.getWsdl',url='=.url',_if='url')
        bc = frame.center.borderContainer()
        treepane = bc.contentPane(region='left',width='250px',margin='2px',splitter=True)
        treepane.tree(storepath='.result.services',
                                selfsubscribe_onSelected="""
                                    var currdata = new gnr.GnrBag();
                                    SET .current_method = null;
                                    if($1.item.attr.nodetype=='Method'){
                                        var parsdict = $1.item.attr.parsdict;
                                        for(var k in parsdict){
                                            currdata.setItem(k,null,{dtype:parsdict[k]})
                                        }
                                        var kw = $1.item.attr;
                                        SET .current_method.methodpath = $1.path;
                                        SET .current_method.name = kw.caption;
                                        SET .current_method.pars = currdata;
                                    }
                                """,selectedLabelClass='selectedTreeNode',hideValues=True)
        self.soapCallerPanel(bc.borderContainer(region='center'))

    def soapCallerPanel(self,bc):
        frametop = bc.framePane('soapPars',region='top',height='300px',splitter=True,datapath='.current_method')
         
        bar = frametop.top.slotBar('*,methodname,*',height='20px',background='#efefef')
        bar.methodname.div('^.name',color='#666')
        footer = frametop.bottom.slotBar('*,runbtn,2',height='2px',background='#efefef')
        footer.runbtn.button('Call',fire='main.callSoapMethod')
        frametop.multiValueEditor(value='^.pars',tools=False,margin='2px')
        bc.dataRpc('.current_method.result',self.callSoapMethod,url='=.url',pars='=.current_method.pars',
                            methodpath='=.current_method.methodpath',_fired='^main.callSoapMethod')

        bc.contentPane(region='center').div('==_F(_result,{nested:true});"";',_result='^.current_method.result')

    @public_method
    def getWsdl(self,url=None):
        client = Client(url)
        services = Bag()
        result = Bag()
        typeconverter= {'string':'T','boolean':'B','int':'L','duoble':'N'}
        for service in client.wsdl.services:
            ports = Bag()
            services.setItem(service.name, ports,caption=service.name,nodetype='Service')
            for port in service.ports:
                methods = Bag()
                ports.setItem(port.name, methods,caption=port.name,nodetype='Port')
                for k,method in port.methods.items():
                    params = []
                    parsdict = dict()
                    for parname,parobj in method.binding.input.param_defs(method):
                        params.append("<b>%s:</b><i>%s</i>" %(parname,parobj.type[0]))
                        parsdict[parname] = typeconverter[parobj.type[0]]
                    methods.setItem(method.name, None,caption=method.name,params=' - '.join(params),parsdict=parsdict,nodetype='Method')
        result['services'] = services
        return result

    @public_method
    def callSoapMethod(self,url=None,methodpath=None,pars=None):
        client = Client(url)
        service,port,method= methodpath.split('.')
        kw = pars.asDict(ascii=True) if pars else dict()
        result = getattr(client.service[port],method)(**kw)
        if result:
            result = result.replace('utf-16','utf-8') #bug in saxparser for utf-16
        return Bag(result)




