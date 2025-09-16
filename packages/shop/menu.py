# encoding: utf-8
# encoding: utf-8
class Menu(object):
    def config(self,root,**kwargs):
        fatturazione = root.branch(u"Shop", tags="")
        fatturazione.thpage(u"Shop", table="shop.shop", tags="",multidb='master')

class ApplicationMenu(object):
    def config(self,root,**kwargs):
        root.packageBranch(u"Shop management", tags="", pkg="shop",multidb='master')
        root.packageBranch(u"Fatturazione", tags="", pkg="fatt",multidb='slave')
        root.packageBranch(u"Geo Italia", tags="admin", pkg="glbl",multidb='master')
        root.packageBranch(u"Amministrazione", tags="admin", pkg="adm")
        root.packageBranch(u"Sistema", tags="sysadmin,_DEV_", pkg="sys",multidb='master')