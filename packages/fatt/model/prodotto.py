#!/usr/bin/env python
# encoding: utf-8

class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('prodotto', pkey='id', name_long='!![it]Prodotto', name_plural='!![it]Prodotti',caption_field='descrizione')
        self.sysFields(tbl)
        tbl.column('codice' ,size=':10',name_long='!![it]Codice')
        tbl.column('descrizione' ,size=':50',name_long='!![it]Descrizione')
        tbl.column('prodotto_tipo_id',size='22' ,group='_',name_long='!![it]Tipo Prodotto',name_short='Tipo').relation('prodotto_tipo.id',relation_name='prodotti',mode='foreignkey',onDelete='raise')
        tbl.column('prezzo_unitario',dtype='money',name_long='!![it]Prezzo unitario',name_short='P.U')
        tbl.column('tipo_iva_codice',size=':5' ,
                    group='_',name_long='!![it]Tipo iva',
                    defaultFrom='@prodotto_tipo_id.tipo_iva'
                    ).relation('tipo_iva.codice',relation_name='prodotti',mode='foreignkey',onDelete='raise')
        tbl.column('foto_url' ,dtype='P',name_long='!![it]Foto',name_short='Foto')
        tbl.column('caratteristiche',dtype='X',name_long='!![it]Caratteristiche',subfields='prodotto_tipo_id')
    
        tbl.joinColumn('totale_oggi_id').relation('fatt.prodotto_data_totale.id',
                                                         cnd='@totale_oggi_id.data=:env_workdate AND @totale_oggi_id.prodotto_id=$id'
                                                         )
        tbl.aliasColumn('totale_oggi','@totale_oggi_id.totale',dtype='N',name_long='Totale oggi')
