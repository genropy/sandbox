# -*- coding: UTF-8 -*-
#--------------------------------------------------------------------------
# Copyright (c) : 2004 - 2007 Softwell sas - Milano 
# Written by    : Giovanni Porcari, Michele Bertoldi
#                 Saverio Porcari, Francesco Porcari
#--------------------------------------------------------------------------
#This library is free software; you can redistribute it and/or
#modify it under the terms of the GNU Lesser General Public
#License as published by the Free Software Foundation; either
#version 2.1 of the License, or (at your option) any later version.

#This library is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#Lesser General Public License for more details.

#You should have received a copy of the GNU Lesser General Public
#License along with this library; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

from gnr.core.gnrdecorator import public_method
try:
    from gnrpkg.biz.dashboard import BaseDashboardItem
except:
    BaseDashboardItem = False

caption = 'Client edit records'
description = 'Client edit records'

class Main(BaseDashboardItem):
    #py_requires='public:Public,th/th:TableHandler'

    def content(self,pane,**kwargs):
        pane.button('Test rpc',fire='pippo')
        #pane.dataRpc(None,'_tblscript.fatt.cliente.dashboard/edit_clienti.Main.miaRpc',_fired='^pippo')
        pane.dataRpc(None,self.miaRpc,_fired='^pippo')

        #pane.stackTableHandler(table='fatt.cliente',view_store__onBuilt=True)

    def configuration(self,pane,**kwargs):
        fb = pane.formbuilder()
        fb.textbox(value='^.color',lbl='Color')
        fb.textbox(value='^.size',lbl='Size')

    @public_method
    def miaRpc(self,**kwargs):
        print 'workdate',self.workdate
        print x

    