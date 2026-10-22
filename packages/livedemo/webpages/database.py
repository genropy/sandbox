# -*- coding: utf-8 -*-


class GnrCustomWebPage(object):

    def main(self, root, **kwargs):
        fb = root.formbuilder(cols=1, border_spacing='6px')
        fb.textbox('^.code', lbl='!![en]Region code', width='6em', placeholder='LOM',
                   connect_onkeyup='SET .code = $1.target.value;')
        grid = root.quickGrid(value='^.regions', height='260px', margin_top='8px')
        grid.column('sigla', name='!![en]Code', width='5em')
        grid.column('nome', name='!![en]Name', width='18em')
        grid.column('zona', name='!![en]Area', width='10em')
        root.dataSelection('.regions', 'glbl.regione', columns='$sigla,$nome,$zona',
                           where="$sigla ILIKE COALESCE(:code,'') || '%%'", code='^.code',
                           recordResolver=False, _onStart=True)
