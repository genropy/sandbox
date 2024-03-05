#!/usr/bin/env python
# encoding: utf-8

class Menu(object):
    def config(self,root,**kwargs):
        root.packageBranch("Fatturazione", pkg='fatt')
        root.packageBranch("Test", pkg='test')
        root.packageBranch("Gestione utenti", pkg='adm', tags='admin')
        root.packageBranch("Sistema", pkg='sys', tags='admin')