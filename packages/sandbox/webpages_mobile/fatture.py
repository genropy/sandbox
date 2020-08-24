# -*- coding: UTF-8 -*-
import datetime
from gnr.core.gnrdecorator import public_method

class GnrCustomWebPage(object):
    css_requires='mobile'


    def main(self,root,**kwargs):
        container = root.div(_class='mobile_button_container',
                action="")
        container.a('Recenti',_class='mobile_button',
                href='fatture')
        container.a('Maggior incassi',_class='mobile_button',href='fatture')
        container.a('Indietro',_class='mobile_button',href='index',background='red')