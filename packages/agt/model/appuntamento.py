# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('appuntamento', pkey='id', 
                    name_long='Appuntamento', 
                    name_plural='Appuntamenti',caption_field='descrizione_appuntamento')
        self.sysFields(tbl)
        tbl.column('cliente_id',size='22', group='_', name_long='Cliente'
                    ).relation('fatt.cliente.id', 
                                relation_name='appuntamenti', 
                                mode='foreignkey', 
                                onDelete='raise')  
        tbl.column('descrizione',name_long='Descrizione')
        tbl.column('dtstart', 'DHZ', 
                    name_long='!![en]Begin',
                    icalendar='DTSTART')
        tbl.column('dtend', 'DHZ', 
                    name_long='!![en]End',
                    icalendar='DTEND')
        tbl.column('geocoder', name_long='!![en]Geocode', 
                    name_short='!![en]Geo',icalendar='GEO')
        tbl.column('geodesc', name_long='!![en]Location', 
                    name_short='!![en]Location')

        tbl.formulaColumn('descrizione_appuntamento',"@cliente_id.ragione_sociale || '-' || $descrizione") 
        

