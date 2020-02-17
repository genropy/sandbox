# encoding: utf-8


class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('agente',pkey='id',name_long='Agente',name_plural='Agenti', caption_field='etichetta')
        self.sysFields(tbl)
        tbl.column('cognome',name_long='Cognome', validate_notnull=True)
        tbl.column('nome',name_long='Nome', validate_notnull=True)
        tbl.column('email',name_long='Email', validate_notnull=True)
        tbl.column('codice', size=':15', name_long='Codice', validate_notnull=True)
        tbl.column('partita_iva', size=':12', name_long='Partita IVA',name_short='P.IVA',unique=True, validate_notnull=True)
        tbl.column('provvigione_base', dtype='percent',name_long='!![it]Provvigione base', validate_notnull=True)
        tbl.column('user_id',name_long='User Id').relation('adm.user.id',one_one=True)
        tbl.column('regioni', name_long='Regioni')
        tbl.formulaColumn('cognome_nome', "$cognome||' '||$nome", name_long='Cognome Nome')
        tbl.formulaColumn('etichetta', "$codice||'-'||$cognome_nome")

    def defaultValues(self):
        return dict(provvigione_base=self.db.application.getPreference('provvigione_default',pkg='agt'))

    def partitionioning_pkeys(self):
        if not self.db.currentEnv.get('agente_id'):
            where=None
        else:
            where='$id=:env_agente_id'
        return [r['pkey'] for r in self.query(where=where).fetch()]
    