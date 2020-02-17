#!/usr/bin/python3
# -*- coding: utf-8 -*-

def config(root,application=None):
    agt = root.branch('Agenti')
    agt.thpage('Agenti',table='agt.agente')
