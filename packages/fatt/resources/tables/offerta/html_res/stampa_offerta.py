#!/usr/bin/env pythonw
# -*- coding: utf-8 -*-
#

from gnr.core.gnrdecorator import customizable
from gnr.web.gnrbaseclasses import TableScriptToHtml

#####DA FARE ---COPIATO DA UNA STAMPA QUALSIASI MASTER DETAIL


class Main(TableScriptToHtml):
    maintable = 'fatt.offerta'
    rows_table = 'fatt.offerta_riga'
    row_mode = 'attribute'
    page_width = 210
    page_height = 297
    doc_header_height = 60
    doc_footer_height = 35 
    grid_row_height=6.5
    grid_header_height = 5
    grid_footer_height = 9
    grid_style_cell = 'text-indent:1mm;border-bottom:0px dotted gray;border-top-width:0px;'
    height_factor = 0.21
    main_font_family = "Arial Narrow"
    currencyFormat = '#,###.00'

    def onRecordLoaded(self):
        customizerBag = self.record['@offerta_tipo.conf_print']
        vp = self.site.virtualPage(py_requires='gnrcomponents/master_detail/master_detail:MasterDetail AS md')
        vp.md.customizePrint(self,viewResource='th_offerta_riga:ViewFromOfferta',
                            customizerBag=customizerBag)
        righe = self.db.table(self.rows_table).query(where='$offerta_id=:f_id',f_id=self.record['id'],
                        order_by='$_row_count').selection().output('grid')
        self.setData(self.rows_path, righe)
        self.is_draft = self.record['__is_draft']
    

    def mainLayout(self,page):
        style = """
        text-align:left;
        line-height:4mm;
        font-size:12pt;
        """
        #8.5pt
        return page.layout(name='pageLayout',um='mm',top=0,
                           left=0,border_width=0,
                           lbl_height=4,lbl_class='caption',
                           style=style)

    def docHeader(self,header):
        style_dest = """
            text-align:left;
            line-height:4.2mm;
            font-size:10pt;"""
        
        anagrafica_id = self.getData('record.cliente_id')
        self.anag_record=self.db.table('fatt.cliente').record(pkey=anagrafica_id).output('bag')
        layout = header.layout(name='doc_header',um='mm',
                                   top=0,bottom=0,left=0,right=0,
                                   lbl_height=3,
                                   border_width=0)     
        r = layout.row()   
        self.docHeaderLeft(r.cell(width=100))
        self.docHeaderRight(r.cell().layout(name='righth',top=1,bottom=1,left=1,right=1,border_width=0,
                                            lbl_height=0,lbl_class='smallCaption',content_class='aligned_left',style=style_dest))

        r = layout.row()  
        self.docHeaderDati(r.cell())  
        return layout

    @customizable
    def docHeaderDati(self,cell):
        style_testata = """
            text-align:left;
            line-height:4mm;
            font-size:10pt;"""
        layout = cell.layout(name='center',top=1,bottom=1,left=1,right=1,border_width=0.3,
                                            lbl_height=3,lbl_class='smallCaption',content_class='aligned_left',style=style_testata)
        row=layout.row()
        cwidth = 56
        #documento = self.getData('record.@ordine_tipo')['descrizione']
        row.cell((self.field('protocollo')),lbl='Protocollo',width=cwidth)
        row.cell(self.pageCounter(), lbl='Pagina')
        row=layout.row()
        row.cell(self.anag_record['codice_fiscale'],lbl='Codice Fiscale',width=cwidth)
        row=layout.row()
        return layout


    def docHeaderLeft(self,layout):
        layout.row()
        #row.cell((self.field('numero') or 'BOZZA'),lbl='Fattura')
        #row.cell(self.field('data_documento'),lbl='Del')
        #row.cell(self.pageCounter(), lbl='Page',width=20)

    def docHeaderRight(self,layout):
        row=layout.row()
        titolo = self.anag_record['titolo'] or ''
        row.cell("""<div>%s</div>::HTML""" %titolo,
                       width=0,style='line-height:4mm;text-indent:5mm;font-size:10pt;')
        for key in ('indirizzo','cap','localita','provincia','nazione'):
            if not self.anag_record[key]:
                self.anag_record[key]=''
        row=layout.row()
        row.cell("""<div>%(ragione_sociale)s</div>
                    <div>%(indirizzo)s</div>
                    <div>%(cap)s  %(localita)s %(provincia)s</div>
                    <div>%(nazione)s</div>::HTML""" %self.anag_record,
                       width=0,style='line-height:5mm;text-indent:5mm;font-size:12pt;')
        layout.row()
        layout.row()
        layout.row()
        layout.row()
        layout.row()
        layout.row()

    def docFooter(self, footer,lastPage=None):
        style = """
            text-align:left;
            font-size:10pt;"""
        layout = footer.layout(name='footerL',um='mm',border_color='gray',
                                   lbl_class='smallCaption',
                                  top=0,bottom=0,left=0,right=0,
                                  lbl_height=3,border_width=0,
                                  content_class='aligned_right',style=style)
        r = layout.row()  
        if not lastPage:
            return
        self.docFooterLeft(r.cell().layout(name='riepiloghi',top=0,bottom=0,left=0,right=0,border_width=0,
                                            lbl_height=3,lbl_class='smallCaption',content_class='aligned_right'))
        self.docFooterRight(r.cell(width=30).layout(name='totali',top=0,bottom=0,left=0,right=0,border_width=0,
                                            lbl_height=0,lbl_class='smallCaption',content_class='aligned_left'))



    def docFooterLeft(self,layout):
        row=layout.row()
                      

    def docFooterRight(self,layout):
       #if self.ordine_in_valuta:
       #    row = layout.row(height=10)    
       #    row.cell(self.field('importo_documento_valuta',
       #                format=self.currencyFormat,currency=self.currency),lbl='Totale S.E.& O.',content_class='aligned_right',style='font-size:10pt;font-weight:bold')
       #    layout.row().cell()
       #    return
        row=layout.row()
        self.docTotali(row.cell().layout(name='totali_ordine',top=1,bottom=1,left=1,right=1,border_width=0.3,
                                            lbl_height=3,lbl_class='smallCaption',content_class='aligned_right'))
    def docTotali(self,layout):
        row=layout.row()        

    def docFooterIva(self,layout):
        pass

    def gridFooter(self, row):
        pass

    def gridLayout(self,body):
        # here you receive the body (the center of the page) and you can define the layout
        # that contains the grid
        return body.layout(name='rowsL',um='mm',top=1,bottom=1,left=1,right=1,
                            border_width=.3,lbl_class='caption',
                            style='text-align:left;font-size:10pt')

    def prepareRow(self,row):
        desc = self.rowData.get('descrizione')
        if not desc:
            desc = self.rowData.get('riga_documento_caption')
        self.rowData['descrizione'] = desc
        self.fillRow()

    def calcRowHeight(self):
        desc = self.rowData.get('descrizione')
        lines = 1
        if desc and '\n' in desc:
            lines = len(desc.split('\n'))
        return 5.5*lines

    def outputDocName(self, ext=''):
        n = self.getData('record.protocollo') or self.getData('record.id')
        return '%s.%s' % (n.replace('.','_').replace('/','_'),ext)
        

    def defineCustomStyles(self):
        """override this for custom styles"""
        if self.record['@ordine_tipo.style_custom']:
            self.body.style(self.record['@ordine_tipo.style_custom'])

        self.body.style("""
                        .pageLayout_layout div{
                            font-family:"%s";
                        }
                         """ %self.main_font_family)

        
                         
    def getPdfPath(self, *args, **kwargs):
        result='vol:%s' %self.record['filepath']
        return result
