# -*- coding: UTF-8 -*-
from gnr.core.gnrdecorator import public_method
from gnr.core.gnrbag import Bag

class GnrCustomWebPage(object):
    py_requires="""buttonset:ButtonSetComponent"""

    def main(self,root,**kwargs):
        root.attributes.update(overflow='hidden')
        self.localStyles(root)
        bc = root.borderContainer(datapath='main')
        self.visoreProdotto(bc.contentPane(region='top',border='1px solid silver',rounded=6,
                            margin='10px'))
        center = bc.contentPane(region='center')
        center.buttonSet(resultpath='.prodotto_id',margin='10px',width='600px',height='300px',
                        storeCallback=self.storeBottoni)

    def visoreProdotto(self,pane):
        pane.dataRecord('.record_prodotto','mag_light.prodotto',pkey='^.prodotto_id',_if='pkey',_else='null')
        fb = pane.formbuilder(cols=2,border_spacing='3px',datapath='.record_prodotto')
        fb.div('^.id',lbl='Id')
        fb.div('^.codice',lbl='Codice')
        fb.div('^.descrizione',lbl='Descrizione')
        fb.div('^.prezzo_unitario',lbl='Prezzo unitario')

    @public_method
    def storeBottoni(self, selected_pkey=None,**kwargs):
        tbl_prodotto_tipo = self.db.table('mag_light.prodotto_tipo')
        where = """(CASE WHEN :selected_pkey IS NULL 
                         THEN $parent_id IS NULL
                         ELSE $parent_id = :selected_pkey 
                    END) AND ($child_count>0 OR @prodotti.id IS NOT NULL)
        """
        template = "%(descrizione)s"
        f = tbl_prodotto_tipo.query(where=where,selected_pkey=selected_pkey).fetch()
        _class = 'bottone bottone_tipo_prodotto'
        isFinalValue = False
        if not f:
            f = self.db.table('mag_light.prodotto').query(where='$prodotto_tipo_id=:selected_pkey',selected_pkey=selected_pkey).fetch()
            template = "Codice:%(codice)s<br/>%(descrizione)s<br/>P.U.:%(prezzo_unitario)2f"
            _class = 'bottone bottone_prodotto'
            isFinalValue = True
        result = Bag()
        for i,r in enumerate(f):
            result.setItem('r_%s' %i,template %r,pkey=r['pkey'],isFinalValue=isFinalValue,_class=_class)
        return result

        
    def localStyles(self,pane):
        pane.css('.bottone',"""display:inline-block; cursor:pointer;
                            padding:5px;border-radius:6px;
                            margin-right:5px;margin-bottom:3px;width:120px;text-align:center;
                            font-size:11pt;overflow:hidden;
                            white-space:nowrap;""")
        pane.css(".bottone[is_selected='true']","box-shadow:2px 2px 2px #666 inset;")
        pane.css('.bottone.bottone_tipo_prodotto',"""background:lightgreen; color:#444;height:20px;""")
        pane.css('.bottone.bottone_prodotto',"""background:lightblue; color:#444;height:50px;font-size:9pt;""")

    def source_viewer_open(self):
        return 'close'
