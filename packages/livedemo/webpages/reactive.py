# -*- coding: utf-8 -*-


class GnrCustomWebPage(object):

    def main(self, root, **kwargs):
        fb = root.formbuilder(cols=3, fld_width='7em', border_spacing='6px')
        fb.numberTextBox('^.quantity', lbl='!![en]Quantity', default_value=2)
        fb.numberTextBox('^.price', lbl='!![en]Unit price', default_value=10, format='#,###.00')
        fb.numberTextBox('^.total', lbl='!![en]Total', format='#,###.00', readOnly=True)
        fb.dataFormula('.total', 'quantity*price', quantity='^.quantity', price='^.price',
                       _onStart=True)
