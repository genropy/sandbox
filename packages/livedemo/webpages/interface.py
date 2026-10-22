# -*- coding: utf-8 -*-


class GnrCustomWebPage(object):

    def main(self, root, **kwargs):
        fb = root.formbuilder(cols=1, border_spacing='6px')
        fb.textbox('^.name', lbl='!![en]Your name', width='16em',
                   connect_onkeyup='SET .name = $1.target.value;')
        fb.div('^.greeting', lbl='!![en]Greeting', font_size='1.5em', color='#1b7fa8')
        fb.dataFormula('.greeting', "name ? hello+', '+name+'!' : ''",
                       name='^.name', hello='!![en]Hello')
