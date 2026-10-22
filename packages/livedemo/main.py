#!/usr/bin/env python
# encoding: utf-8
from gnr.app.gnrdbo import GnrDboTable, GnrDboPackage


class Package(GnrDboPackage):
    def config_attributes(self):
        return dict(comment='live examples embedded by genropy.org',
                    sqlschema='livedemo', language='en',
                    name_short='Live', name_long='Live examples',
                    name_full='Live examples')

    def config_db(self, pkg):
        pass


class Table(GnrDboTable):
    pass


class WebPage(object):
    """Shared plumbing of every example page of this package.

    genropy.org shows the source of each example next to the running page, so
    the example file must hold the example and nothing else: the chrome-free
    wrapper and the height message to the embedding page live here.

    No auth_default here and no auth_main on the pages: with no page tags
    _checkAuth returns AUTH_OK, so the pages are public and read-only.
    """
    package_css_requires = 'livedemo'

    def mainWrapper(self, rootwdg, **kwargs):
        pane = rootwdg.div(_class='livedemo_page', nodeId='livedemo_root', datapath='demo')
        self.main(pane, **kwargs)
        pane.dataController("""
            var el = genro.nodeById('livedemo_root').domNode;
            var post = function(){
                genro.dom.windowMessage('parent',
                    {topic:'livedemo_height', height:el.scrollHeight});
            };
            new ResizeObserver(post).observe(el);
            post();
            """, _onStart=True, _delay=200)
