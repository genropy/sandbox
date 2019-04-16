#!/usr/bin/env python
# encoding: utf-8
def config(root,application=None):
    root.branch("Fatturazione",pkg='fatt')
    root.branch("Amministrazione", tags="admin", pkg="adm")
    root.branch("Geo Italia", tags="admin", pkg="glbl")
    root.branch("Sistema", tags="sysadmin,_DEV_", pkg="sys")
    #root.branch("Lezioni", pkg="tutor", dir="lessons")
    #root.branch("Gui", pkg="tutor", dir="gui")
    if hasattr(application,'site') and application.site.remote_edit:
        root.branch(u"Docu Examples", pkg="tutor", dir="docu_examples")
