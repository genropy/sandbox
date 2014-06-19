# -*- coding: UTF-8 -*-
"""Rss Feeds"""

class GnrCustomWebPage(object):
    documentation = 'auto'

    def main(self,root,**kwargs):
        root.addToDocumentation(title='Piero',filepath='mario/piero.html')
        root.addToDocumentation(title='Prova',filepath='/advices/prova.html')
        root.addToDocumentation(title='Mario',filepath='site:sitedoc/mario.html')

        root.div('Rss Feeds')