#!/usr/bin/python3
# -*- coding: utf-8 -*-
class Menu(object):
    def config(self,root,**kwargs):
        agt = root.branch('Agenti')
        agt.thpage('Agenti',table='agt.agente')
        agt.thpage('Appuntamenti',table='agt.appuntamento')
