# -*- coding: UTF-8 -*-
import datetime
from gnr.core.gnrdecorator import public_method

class GnrCustomWebPage(object):
    auth_main='user'
    css_requires='mobile'


    def main(self,root,**kwargs):
        container = root.div(_class='mobile_button_container')
        container.a('Fatture',
                    _class='mobile_button',href='fatture')
        container.a('Clienti',
        _class='mobile_button',href='clienti')
        container.a('Prodotti',
                    _class='mobile_button',href='prodotti')
        container.lightbutton('Esci',_class='mobile_button',
                            action='genro.logout();',
                            background='red')