# -*- coding: UTF-8 -*-
from gnr.core.gnrdecorator import public_method
from docutils.core import publish_string
import StringIO
import tempfile

class GnrCustomWebPage(object):
    def main(self,root,**kwargs):
        root.div().codemirror(value='^rstdoc',config_mode='rst',
                            config_lineNumbers=True)

        root.div('^htmldoc',border='1px solid green',margin='10px',min_height='30px')
        root.dataRpc('htmldoc',self.rst2html,
                    rstdoc='^rstdoc',_delay=500)

    @public_method
    def rst2html(self,rstdoc=None,**kwargs):
        return publish_string(rstdoc, writer_name='html')
