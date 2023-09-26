#!/usr/bin/env python
# encoding: utf-8

class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('prodotto', pkey='id', name_long='!![it]Prodotto', name_plural='!![it]Prodotti',caption_field='descrizione')
        self.sysFields(tbl)

        tbl.column('codice', size=':10', name_long='!![it]Codice', validate_call="return !value.includes(' ')", 
                        validate_call_error='Non utilizzare spazi nel campo Codice')
        tbl.column('descrizione' ,size=':50', name_long='!![it]Descrizione')
        tbl.column('prodotto_marca', size='22', group='_', name_long='!![it]Marca Prodotto', name_short='Marca').relation(
                        'prodotto_marca.id',relation_name='prodotti',mode='foreignkey', onDelete='setnull')
        tbl.column('prodotto_tipo_id', size='22', group='_', name_long='!![it]Tipo Prodotto', name_short='Tipo').relation(
                        'prodotto_tipo.id',relation_name='prodotti',mode='foreignkey', onDelete='raise')
        tbl.column('prezzo_unitario', dtype='money', name_long='!![it]Prezzo unitario', name_short='P.U')
        tbl.column('foto_url', dtype='P', name_long='!![it]Foto',name_short='Foto')
        tbl.column('caratteristiche', dtype='X', name_long='!![it]Caratteristiche', subfields='prodotto_tipo_id')
        tbl.column('note', name_long='!![it]Note')
        tbl.column('materiale_consumo', dtype='B', name_long='Materiale di consumo', name_short='Consumabile')

        tbl.formulaColumn('giacenza_curr_dep', select=dict(table='mag_light.giacenza_prodotto_deposito', 
                                columns='$quantita_disponibile', where='$prodotto_id=#THIS.id AND $deposito_codice=:env_current_deposito_codice'),
                                name_long='Giacenza deposito', dtype='L')
        tbl.formulaColumn('giac_attesa_curr_dep', select=dict(table='mag_light.giacenza_prodotto_deposito', 
                                columns='$quantita_attesa', where='$prodotto_id=#THIS.id AND $deposito_codice=:env_current_deposito_codice'),
                                name_long='Giacenza attesa deposito', dtype='L')
        
    def onDuplicating_many(self, record, copy_number=None, copy_label=None):
        record['descrizione'] = '{descrizione} / {label}'.format(descrizione=record['descrizione'], label=copy_label)

    def formulaColumn_giacenze(self):
        depositi = self.db.table('mag_light.deposito').query().fetch()
        tbl_totali = self.db.table('mag_light.giacenza_prodotto_deposito')
        result = []
        for deposito in depositi:
            dep = deposito['codice']
            for colname,col in tbl_totali.columns.items():
                colattr = col.attributes
                if colname.startswith('quantita'):
                    newcol = dict(name='{colname}_{dep}'.format(colname=colname, dep=dep),
                                    dtype=colattr['dtype'], 
                                    select=dict(columns='${colname}'.format(colname=colname),
                                            where="($prodotto_id=#THIS.id AND $deposito_codice='%s')" % deposito['codice'],
                                            table='mag_light.giacenza_prodotto_deposito'),
                                    name_long='{name_long} {dep}'.format(name_long=colattr['name_long'], dep=dep))
                    result.append(newcol)
                
        return result