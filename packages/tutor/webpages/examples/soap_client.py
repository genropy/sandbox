# -*- coding: UTF-8 -*-
from gnr.core.gnrbag import Bag,BagException
from gnr.core.gnrdecorator import public_method
from suds.client import Client

class GnrCustomWebPage(object):
    def main(self,root,**kwargs):
        #ricevo root e creo un framePane con identifcativo 'main' e gli assegno un percorso base nello store a 'main'.
        frame = root.framePane('main',datapath='main')
        
        #uso il metodo '.data' per assegnare il valore di url ad un default. L'indirizzo '.url' iniziando con '.' è relativo al datapath corrente ('main')
        frame.data('.url','http://www.webservicex.com/globalweather.asmx?WSDL')
        
        #Il framePane ha un top in cui creo una slotToolbar con questi slot: 2px,uncampo per l'url (urlfield), 10px, un bottone (runbutton)
        bar = frame.top.slotToolbar('2,urlfield,10,runbutton,*',height='20px')
        
        #avendo dichiarato che esiste una contenitore per campi (formbilder) e dico che al tasto 'Enter' verrà triggerata la locazione '.run'
        fb = bar.urlfield.formbuilder(cols=1,onEnter='FIRE .run;',border_spacing='3px') 
        
        #nel formbuilder metto un widget per caricare del testo, specificando una label ('Url') e dicendo che il valore inputato finirà al pathrelativo '.url'
        fb.textbox('^.url',lbl='Url',width='30em')
        
        #metto ora nella toolbar, allo slot 'runbutton' un bottone che, una volta premuto, triggererà un avento al path '.getWsdl'
        bar.runbutton.button('Run',fire='.getWsdl')
        
        #creo ora un oggetto di tipo dataRpc che eseguirà la chiamata al server. Il primo parametro è il path dove verrà messo il risultato della chiamata
        #il parametro fittizio _fired='^.getWsld'provocherà l'esecuzione dela chiamata ogni volta che al path .getWsdl avverrà un cambiamento di valore.
        #ricordo che un comando 'fire' pone al path il valore True ed immediatamente riporta a null il valore.
        #il parametro 'url' si riempirà del valore al path '.url' mentre il parametro _if impedirà ce venga fatta la chiamata in assenza di un url.
        #infine _lockScreen serve a bloccare lo schermo durante la call.
        bar.dataRpc('.result',self.getWsdl,_fired='^.getWsdl',url='=.url',_if='url',_lockScreen=True)
        
        #nella parte centrale della form viene messo un contenitore multiplo di tipo 'borderContainer'
        bc = frame.center.borderContainer()
        
        #nella parte di sinistra mettiamo un contentPane (contenitore). Ne dichiariamo la largezza e chiediamo che ci sia uno splitter per il ridimensionamento.
        treepane = bc.contentPane(region='left',width='250px',margin='2px',splitter=True)
        
        #nel contentPane mettiamo un albero che verrà costruito a partire dal contenuto che sarà reso disponibile dalla chiamata definita prima.
        #diciamo inoltre che al variare dell'albero selezionato vengono settati dei valori al path 'current_method' corrispondenti all'elemento selezionato.
        treepane.tree(storepath='.result.services',
                                selfsubscribe_onSelected="""
                                    var kw = $1.item.attr
                                    var selected=null
                                    if(kw.nodetype=='Method'){
                                        selected=new gnr.GnrBag();
                                        var parsdict = kw.parsdict;
                                        for(var k in parsdict){
                                            selected.setItem('pars.'+k,null,{dtype:parsdict[k]})
                                        }
                                        selected.setItem('methodpath',$1.path);
                                        selected.setItem('name', kw.caption);
                                    }
                                    SET .current_method = selected;
                                """,selectedLabelClass='selectedTreeNode',hideValues=True)
                                
        #per popolare la parte destra chiamiamo il metodo soapCallerPanel. Avremmo potuto continure qui di seguito
        #ma dividere il codice in blocchi aiuta a comprenderlo meglio...
        self.soapCallerPanel(bc.borderContainer(region='center'))

    def soapCallerPanel(self,bc):
        #provvediamo ora a mettere nella parte superiore del borderContainer ricevuto un altro framePane, mettiamo anche uno splitter e assegniamo un datapath
        frametop = bc.framePane('soapPars',region='top',height='300px',splitter=True,datapath='.current_method')
        
        #come visto precedentemente creiamo una toolbar in cui definiamo solo uno slot 'methodname'
        bar = frametop.top.slotBar('*,methodname,*',height='20px',background='#efefef')
        
        #diciamo che lo slot 'methodname si alimenterà dal path '^.name'. il Simbolo '^' segnala che ad ogni variazione il div dovrà aggiornarsi 
        bar.methodname.div('^.name',color='#666')
        
        #mettiamo anche una toolbar nel bottom con un bottone per invocare il metodo.
        footer = frametop.bottom.slotBar('*,runbtn,2',height='2px',background='#efefef')
        footer.runbtn.button('Call',fire='main.callSoapMethod')
        
        #nella parte centrale del frame piazziamo un multiValueEditor che è un widget complesso che consente di editare più valori di tipo diverso.
        frametop.multiValueEditor(value='^.pars',tools=False,margin='2px')
        
        #mettiamo un altro oggetto dataRpc che sarà invocato con un fire al path 'main.callSoapMethod' passando il methodo Soap da chiamare e i relativi parametri.
        bc.dataRpc('.current_method.result',self.callSoapMethod,url='=.url',pars='=.current_method.pars',
                            methodpath='=.current_method.methodpath',_fired='^main.callSoapMethod',_lockScreen=True)
        
        #infine creiamo lo spazio dove verrà mostrato il risultato come Bag formattata
        bc.contentPane(region='center').div('==_F(_result,{nested:true});"";',_result='^.current_method.result')

    @public_method
    def getWsdl(self,url=None):
        #questa chiamata rpc riceve un url, crea un client suds e prepara una Bag con la descrizione del Wsdl
        #da notare che una bag viene in modo automatico presentata nel client come un tree.
        client = Client(url)
        services = Bag()
        typeconverter= {'string':'T','boolean':'B','int':'L','duoble':'N','float':'N'}
        for service in client.wsdl.services:
            ports = Bag()
            services.setItem(service.name, ports,caption=service.name,nodetype='Service')
            for port in service.ports:
                methods = Bag()
                ports.setItem(port.name, methods,caption=port.name,nodetype='Port')
                for k,method in port.methods.items():
                    methods.setItem(method.name, None,
                          caption=method.name,
                          parsdict=dict([(parname, typeconverter[parobj.type[0]]) for parname,parobj in method.binding.input.param_defs(method)]),
                          nodetype='Method')
        return Bag(dict(services = services))

    @public_method
    def callSoapMethod(self,url=None,methodpath=None,pars=None):
        #questa chiamata riceve l'url del wsdl, il metodo da chiamare e i parametri.
        # esegue la richiesta soap e rende il risultato come Bag che verrà mosrata formattata.
        client = Client(url)
        service,port,method= methodpath.split('.')
        kw = pars.asDict(ascii=True) if pars else dict()
        result = getattr(client.service[port],method)(**kw)
        if result:
            result = result.replace('utf-16','utf-8') #bug in saxparser for utf-16
        try:
            result=Bag(result)
        except BagException:
            result=Bag(dict(result=result))
        return result




