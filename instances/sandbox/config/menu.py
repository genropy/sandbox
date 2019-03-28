#!/usr/bin/env python
# encoding: utf-8
def config(root,application=None):
    root.branch("Fatturazione",pkg='fatt')
    root.branch("Amministrazione", tags="admin", pkg="adm")
    root.branch("Geo Italia", tags="admin", pkg="glbl")
    root.branch("Sistema", tags="sysadmin,_DEV_", pkg="sys")

    root.branch("Tutor",pkg='fatt')

