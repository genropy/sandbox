#!/usr/bin/env python
# encoding: utf-8
def config(root,application=None):
    root.branch("Fatturazione",pkg='fatt')
    root.branch("Amministrazione", tags="admin", pkg="adm")
    root.branch("Geo Italia", tags="admin", pkg="glbl")
    root.branch("Business intelligence", tags="admin", pkg="biz")
    root.branch("Sistema", tags="sysadmin,_DEV_", pkg="sys")
    #root.branch("Lezioni", pkg="tutor", dir="lessons")
    #root.branch("Gui", pkg="tutor", dir="gui")
