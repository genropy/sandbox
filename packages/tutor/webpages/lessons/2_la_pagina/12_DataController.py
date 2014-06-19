# -*- coding: UTF-8 -*-

from random import randint as rn

class GnrCustomWebPage(object):
    
    def main(self,root,**kwargs):
        self.bytesConverter(root.div(margin='15px',datapath='bytesconverter'))
        self.eratostene(root.div(margin='15px',datapath='eratostene'))
        self.clickToDecrement(root.div(margin='15px',datapath='clickToDecrement'))
        self.autoDecrement(root.div(margin='15px',datapath='autoDecrement'))

    def bytesConverter(self,pane):
        pane.h1('Bytes Converter')
        box=pane.div(width='400px',border='1px solid gray')
        fb = box.formbuilder(cols=2)
        fb.numberTextBox('^.bytes',lbl='Bytes',width='60px')
        fb.div('^.conv',lbl='Conversion',width='70px',_class='fakeTextBox')
        fb.dataController("""
             var s = ['Bytes','KB','MB','GB','TB'];
             if (b == 0) return 'n/a';
             var i = parseInt(Math.floor(Math.log(b) / Math.log(1024)));
             SET .conv = (b / Math.pow(1024, i)).toFixed(1) + ' ' + s[[i]];""",
             b='^.bytes')

    def eratostene(self,pane):
        pane.h1('Eratostene')
        box=pane.div(width='700px',border='1px solid gray')
        fb = box.formbuilder(cols=1)
        fb.numberTextBox('^.nmax',lbl='Primes limit',width='40px',
                         validate_max=1000,
                         validate_max_error='Max value: 1000',
                         validate_min='1',
                         validate_min_error='Min value: 1',
                         validate_onReject="SET .result=''")
        fb.dataController(self.eratosteneJs(),nMax='^.nmax',
                          _if='nMax>0 && nMax<=1000',
                          _else="alert('The number must be in the interval 1:1000')")
        fb.div('^.result',lbl='Primes',width='500px',_class='fakeTextBox')
        
    def eratosteneJs(self):
        js="""var d = [], primes = [];
              for (var n2, x, n1 = 2; n1 < nMax; n1++) {
                if (d[n1]) {
                  for (n2 = 0; n2 < d[n1].length; n2++) {
                    x = d[n1][n2];
                    if (d[x + n1]) {d[x + n1].push(x); }
                    else { d[x + n1] = [x]; }
                  }
                  delete d[n1];} 
                else {
                  primes.push(n1);
                  if (n1 * n1 < nMax) { d[n1 * n1] = [n1]; }
                }
              }
              SET .result=primes.join(', ')"""
        return js

    def clickToDecrement(self,pane):
        pane.h1('Click to decrement value')
        box=pane.div(width='400px',border='1px solid gray')
        fb = box.formbuilder(cols=2,fld_width='80px')
        fb.numberTextBox('^.counter',lbl='Start value')
        fb.button('Decrement',action="FIRE .decrement")
        box.dataController("""if (counter>0){
                                 SET .counter = counter-1;;
                             } """, counter='=.counter',
                            _fired='^.decrement')
        
    def autoDecrement(self,pane):
        pane.h1('Enter a number (1 to 256)')
        box=pane.div(width='400px',border='1px solid gray')
        fb = box.formbuilder(cols=4,fld_width='80px')
        fb.numberTextBox('^.start',lbl='Enter a number (1 to 256)')
        fb.dataController("""SET .counter =start;
                             SET .timing =0.1;""", start='^.start')
        fb.data('.timing',0)
        fb.dataController("""if (counter>0){ SET .counter = counter-1;}
                                 else{ SET .timing = 0;}""", 
                             counter='=.counter', _timing='^.timing')
        pane.div(width='400px').div('^.counter',text_align='center',
                                     background='#666',color='white',
                                     font_size="==f+'px'",f='^.counter')
        
        
 
        
        
        
        
        


        
   
