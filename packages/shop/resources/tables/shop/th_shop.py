#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method
from gnrpkg.multidb.utility import getSyncTables
from gnr.core.gnrbag import Bag


class Page(BaseComponent):
    py_requires= "th/th_dynamic:DynamicTableHandler"

    @public_method
    def checksync_extstore(self,selection=None,**kwargs):
        tbl = selection.tablename
        with self.db.tempEnv(storename=self.db.rootstore):
            master_f = self.db.table(tbl).query().fetchAsDict('pkey')
        def cb(row):
            res = {}
            if row['pkey'] not in master_f:
                res['_customClasses'] = 'missingInMaster'
                res['missing_in_master'] = True
            return res
        selection.apply(cb)


class View(BaseComponent):
    py_requires = 'startupdata_manager/startupdata_manager:StartupDataManager'

    def th_hiddencolumns(self):
        return '$dbstore'
    
    def th_struct(self, struct):
        r = struct.view().rows()
        r.cell('apri_tab', name="Apri", calculated=True, width='3em',
               cellClasses='cellbutton',
               format_buttonclass='icnBaseLens buttonIcon',
               format_isbutton=True, format_onclick="""var row = this.widget.rowByIndex($1.rowIndex);
                                                           genro.childBrowserTab('/'+row['dbstore']+'/');""")
        #r.fieldcell('dbstore')
        r.fieldcell('denominazione')
        r.fieldcell('partita_iva')
        r.fieldcell('active_dbstore')

    def th_order(self):
        return 'denominazione'

    def th_query(self):
        return dict(column='denominazione', op='contains', val='')


class Form(BaseComponent):
    css_requires='erpy_studio'
    py_requires = """prefhandler/prefhandler:AppPrefHandler,th/th_dynamic:DynamicTableHandler,
                    multidb_components:MultidbCheckUtils"""

    def th_form(self, form):
        bc = form.center.borderContainer()
        top = bc.borderContainer(region='top',height='110px', datapath='.record')
        fb = top.contentPane(region='center').formbuilder(cols=2, border_spacing='4px')
        fb.field('denominazione')
        fb.field('partita_iva')
        fb.div('^.dbstore',hidden='^.dbstore?=!#v')
        fb.button('Crea',hidden='^.dbstore',disabled='^#FORM.controller.status?=#v!="ok"').dataRpc(self.creaDbShop,
                                                     pkey='=#FORM.record.id',
                                                     _lockScreen=True,
                                                    _ask=dict(title='Crea dbstore',
                                                              fields=[dict(name='dbstore', lbl='Dbstore', 
                                                                validate_case='l',
                                                                validate_regex='![^A-Za-z0-9_]', 
                                                                validate_notnull=True,
                                                                validate_regex_error='Caratteri non ammessi')]),
                                                            _onResult="this.form.reload()")
       #fb.button('import dbtemplate',hidden='^.imported_instance',
       #                 ask=dict(title=u'Importa dati da', hidden='^#FORM.record.dbtemplate',
       #                                        fields=[dict(name='dbtemplate', lbl='A partire da',
       #                                                     tag='filteringselect',
       #                                                     storepath='dbtemplates', storeid='filepath',
       #                                                     storecaption='caption')]),
       #          action='FIRE #FORM.import_data=dbtemplate')

       #fb.dataRpc(None, self.importaDatiDaTemplate, dbtemplate='^#FORM.import_data', pkey='=#FORM.pkey',
       #           _onResult='this.form.reload()', _lockScreen=True)
        tc = bc.tabContainer(region='center', margin='2px',selectedPage='^#FORM.selectedPage')
        tc.contentPane(title='Dati anagrafici')
        tc.checkSyncDataTab(title='Controllo dati',hidden='^#FORM.record.dbstore?=!#v')
    
    def gestioneUtenzeEsterne(self,pane):
        th = pane.dialogTableHandler(table='adm.user',condition='$dbstore=:dbs',
                                dialog_height='400px',formInIframe='/adm/user_page',
                                dialog_width='650px',condition_dbs='^#FORM.record.dbstore')
        bar = th.view.top.bar.replaceSlots('addrow','creautente')

        bar.creautente.slotButton(u'Crea utente shop',
                        iconClass='iconbox add_row',
                        email='=#FORM.record.@cliente_id.@anagrafica_id.email',
                        action='PUBLISH creaUtenteContabilita = {"user":user,"password":password,"email":email};',
                        ask=dict(title="Dati utenza",
                                fields=[dict(name='user',
                                             lbl='User',validate_notnull=True),
                                        dict(name='password',type='password',
                                            lbl='Password',validate_notnull=True),
                                        dict(name='email',lbl='Email')]),
                                hidden='^.user_id')
       #pane.dataRpc(None,self.db.table('erpy_studio.contabilita').creaUtenteContabilita,subscribe_creaUtenteContabilita=True,
       #            record_id='=#FORM.record.id',_if='record_id')
    
    

   #@public_method
   #def importaDatiDaTemplate(self, pkey=None, dbtemplate=None):
   #    self.mixinComponent('startupdata_manager/startupdata_manager:StartupDataManager')
   #    dbstore = self.db.table('erpy_studio.contabilita').readColumns(
   #        pkey=pkey, columns='$dbstore')
   #    with self.db.tempEnv(storename=dbstore):
   #        self.sd_loadDbTemplate(dbtemplate)
   #        self.db.table('adm.counter').initializeTableSequences(self.db.table('erpy_coge.conto'))
   #    with self.db.table('erpy_studio.contabilita').recordToUpdate(pkey) as rec:
   #        rec['dbtemplate'] = os.path.basename(dbtemplate).split('.')[0]
   #        self.db.commit()

    @public_method
    def creaDbShop(self,pkey=None,dbstore=None):
        tblobj = self.db.table('shop.shop')
        with tblobj.recordToUpdate(pkey) as rec:
            rec['dbstore'] = dbstore
        tblobj.multidb_activateDbstore(rec)
        self.db.commit()

    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
