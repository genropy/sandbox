# -*- coding: UTF-8 -*-

from gnr.core.gnrdecorator import public_method
from docutils.core import publish_string
class GnrCustomWebPage(object):
    
    
    def main(self,root,**kwargs):
        bc = root.borderContainer(datapath='main')
        left = bc.contentPane(region='left',width='50%',splitter=True,overflow='hidden')
        left.codemirror(value='^.source',height='100%',
               border='1px solid silver',config_mode='rst',config_lineNumbers=True) 
        iframe = bc.contentPane(region='center').htmliframe(height='100%',width='100%',border=0)
        bc.dataController('iframe.domNode.contentWindow.document.body.innerHTML = rendering',rendering='^.rendering',iframe=iframe)
        bc.dataRpc('.rendering',self.convert_rst2html,_onCalling="""kwargs.source_rst=' \n'+skwargs.source_rst;""",
                    source_rst='^.source',
                    _delay=500)





    @public_method
    def convert_rst2html(self,source_rst=None,**kwargs):
        stylesheet_path=self.site.getStaticPath('rsrc:common','rstcss','gnrcss.css')
        settings_overrides = {'embed_stylesheet': 'yes','stylesheet_path':stylesheet_path}
        return publish_string(source_rst, writer_name='html',
              settings_overrides=settings_overrides)