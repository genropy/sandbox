# encoding: utf-8
class Menu(object):
    def config(self,root,**kwargs):
        root.packageBranch(u"Amministrazione", tags="admin", pkg="adm")
        root.packageBranch(u"Sistema", tags="sysadmin,_DEV_", pkg="sys")
        root.thpage('Shop',table='shop.shop',aux_instance='multishop')