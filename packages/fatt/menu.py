# encoding: utf-8
from gnr.core.gnrdecorator import metadata
class Menu(object):
    def config(self,root):
        fatturazione = root.branch(u"Fatturazione")
        fatturazione.thpage(u"Clienti", table="fatt.cliente")
        fatturazione.thpage(u"Tipi Prodotto", table="fatt.prodotto_tipo")
        fatturazione.thpage(u"Prodotti", table="fatt.prodotto")
        fatturazione.thpage(u"Fatture", table="fatt.fattura")
        fatturazione.thpage(u"Righe vendita", table="fatt.fattura_riga")
        fatturazione.tableBranch('Ultime fatture',table='fatt.fattura',
                                query_limit=5,
                                query_order_by='$protocollo desc',
                                cacheTime=5)
        fatturazione.tableBranch('Ultime fatture brutte',table='fatt.fattura',
                                query_limit=5,
                                query_order_by='$protocollo desc',
                                cacheTime=5,variant='piero')
        fatturazione.tableBranch('Ultime per tipo',table='fatt.fattura',
                                branchMethod='menuPerTipoCliente',
                                cacheTime=5)

        fatturazione.tableBranch('Prodotti a caso',table='fatt.prodotto',
                                webpage='fatt/scheda_prodotto',query_limit=5,
                                webpage_template='catalogo',cacheTime=5)

        fatturazione.packageBranch('Gestione utenti',pkg='adm',
                                branchMethod='userSubmenu',
                                    branch_parametro=3)

                                    
        fatturazione.lookups(u"Tabelle Ausiliarie", lookup_manager="fatt")

 
    @metadata(group_code='AGT')
    def config_agenti(self,root):
        fatturazione = root.branch(u"Fatturazione")
        fatturazione.thpage(u"Agentose fatture", table="fatt.fattura")


    def quickMenu(self,mostraGlbl=None):
        root.thpage(u"Prodotti", table="fatt.prodotto")
        root.thpage(u"Province", table="glbl.provincia")
