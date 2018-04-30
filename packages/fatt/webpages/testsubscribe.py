# -*- coding: UTF-8 -*-
from gnr.core.gnrdecorator import public_method
            
class GnrCustomWebPage(object):
    def main(self,root,**kwargs):
        bc = root.borderContainer(datapath='main')
        top = bc.contentPane(region='top')
        top.formbuilder().numberTextBox(value='^.numero',lbl='Numero')
        top.button('Su',action='PUBLISH attivati = {numero:numero,direzione:direzione};',
                numero='=.numero',direzione='su')
        top.button('Giù',action='PUBLISH attivati = {numero:numero,direzione:direzione};',
                numero='=.numero',direzione='giu')
        top.button('Destra',action='PUBLISH attivati = {numero:numero,direzione:direzione};',
                numero='=.numero',direzione='destra')
        top.button('Sinistra',action='PUBLISH attivati = {numero:numero,direzione:direzione};',
                numero='=.numero',direzione='sinistra')
        center = bc.contentPane(region='center')
        for j in range(100):
            subscribe = """if(this.attr.numero%$1.numero===0){
                if($1.direzione=='su'){
                    this.domNode.style.top = (parseInt(this.domNode.style.top || 0)-1)+'px'
                }
                if($1.direzione=='giu'){
                    this.domNode.style.top = (parseInt(this.domNode.style.top || 0)+1)+'px'
                }
            }"""
            center.div(height='15px',width='15px',
                        display='inline-block',
                        numero=j,position='relative',
                        border='1px solid red',margin='2px',
                        subscribe_attivati=subscribe)