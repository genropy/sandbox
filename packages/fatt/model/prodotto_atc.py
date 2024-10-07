#!/usr/bin/env python
# encoding: utf-8
from gnr.app.gnrdbo import AttachmentTable

class Table(AttachmentTable):
    def onTableConfig(self,tbl):
        tbl.column('filepath', ext_ltx_documentRegister=dict(maintable_pkey='maintable_id',
                                            preprocess={'pdf':'ocr'},
                                            name='Allegato {description}',language='italian'))
#
   # def onTableConfig(self,tbl):
   #     tbl.column('text_content', tsvector='$text_language')