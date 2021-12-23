from gnr.web.gnrwsgisite import GnrWsgiSite

site = GnrWsgiSite('sandboxpg')
tblcli = site.db.table('fatt.cliente')
tblcli.column('@fatture.@righe.#')

#count(*) tbl='fatt.fattura_riga',where='@fattura_id.cliente_id=#THIS.id'