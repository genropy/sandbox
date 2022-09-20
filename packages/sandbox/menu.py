# encoding: utf-8
class Menu(object):
    def config(self,root,**kwargs):
        root.packageBranch(u"Fatturazione", tags="", pkg="fatt")
        root.packageBranch(u"Test", tags="", pkg="test")
        root.packageBranch(u"Geo Italia", tags="admin", pkg="glbl")
        root.packageBranch(u"Amministrazione", tags="admin", pkg="adm")
        root.packageBranch(u"Sistema", tags="sysadmin,_DEV_", pkg="sys")