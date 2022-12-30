# -*- coding: UTF-8 -*-
            
class GnrCustomWebPage(object):
    css_requires='christmas'

    def main(self,root,**kwargs):
        cp = root.contentPane(height='100%', _class='main_bc snowflakes')
        cp.img(src='/_storage/img/genropy-logo.png')
        cp.h1('wishes you Merry Christmas')
        for i in range(1,100):
            cp.div(id=f"snowflake_{i}", _class='snowflake', width=f'{i}px', height=f'{i}px')