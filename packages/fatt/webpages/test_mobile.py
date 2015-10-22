# -*- coding: UTF-8 -*-
from gnr.core.gnrdecorator import public_method
from docutils.core import publish_string
import StringIO
import tempfile

class GnrCustomWebPage(object):
    def main(self,root,**kwargs):
        root.dataController("""
            SET messagebox.caption = type+' -> '+evt.target.id;
            SET messagebox.detail = genro.mobile.touchEventString(evt);
            """,subscribe_hammer_input=True)
        root.div('sono piero',id='piero',height='50px',width='300px',border='2px solid silver',margin='20px')
        root.div('sono mario',id='mario',height='50px',width='300px',border='2px solid silver',margin='20px')
        root.div('sono antonio',id='antonio',height='50px',width='300px',border='2px solid silver',margin='20px')
        root.div('^messagebox.caption',min_height='50px',background='red',color='white',font_size='2em')
        root.div('^messagebox.detail',min_height='50px',background='yellow',font_size='.9em',padding='20px')
