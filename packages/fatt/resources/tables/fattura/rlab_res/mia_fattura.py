#!/usr/bin/env python
# encoding: utf-8

from gnr.core.gnrrlab import RlabResource


class Main(RlabResource):

    maintable = 'fatt.fattura'
    row_table = 'fatt.fattura_riga'
    doc_header_height = 32
    doc_footer_height = 12
    grid_header_height = 5

    def main(self):
        self.canvas.drawString(100,100, 'PLACEHOLDER')

    def docHeader(self, header):
        pass

    def datiFattura(self, c):
        pass
 
    def datiCliente(self, c):
        pass

    def gridStruct(self,struct):
        pass

    def docFooter(self, footer, lastPage=None):
        pass