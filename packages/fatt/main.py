#!/usr/bin/env python
# encoding: utf-8

from gnr.app.gnrdbo import GnrDboTable, GnrDboPackage

class Package(GnrDboPackage):

    def config_attributes(self):
        return dict(comment='Package demo fatturazione',sqlschema='fatt',language='it',
                    name_short='Fatturazione', name_long='Fatturazione', name_full='Fatturazione')
                    
    def config_db(self, pkg):
        pass

    def custom_type_money(self):
        return dict(dtype='N',format='#,###.00')

    def custom_type_percent(self):
        return dict(dtype='N',format='##.00')

    def fooSum(self,par1=None,par2=None):
        """Uso da webpage:
             result = self.db.package('fatt').fooSum(3,5)
        """
        return par1+par2

class Table(GnrDboTable):
    
    def fooSum(self,par1=None,par2=None):
        """comune a tutte le tabelle del package:
            Uso da webpage o da table di package diverso:
             result = self.db.table('fatt.miatable').fooSum(3,5)
            Uso da table del package
              result = self.fooSum(3,5)
             """
        return par1+par2

class WebPage(object):
    def fooSum(self,par1=None,par2=None):
        """comune a tutte le webpage del package:
            Uso da webpage:
             result = self.fooSum(3,5)"""
        return par1+par2
