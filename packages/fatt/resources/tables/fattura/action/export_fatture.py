from gnr.web.batch.btcexport import BaseResourceExport

caption = 'Export fatture'
description = 'Export fatture'

class Main(BaseResourceExport):
    export_mode='csv'
    localized_data = True
    locale ='EN_AU'
    csv_rowseparator='\n\n'
    csv_colseparator='--'
