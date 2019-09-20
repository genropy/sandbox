# -*- coding: UTF-8 -*-
from gnr.core.gnrdecorator import public_method
import sh
class GnrCustomWebPage(object):
    def main(self,root,**kwargs):
        box = root.div(datapath='test')
        fb = box.formbuilder(border_spacing='3px',cols=2)
        fb.textbox(value='^.command',lbl='Command',width='40em')
        box.dataRpc('.result',self.doCommand,
                    command='^.command',_if='command')
        box.pre('^.result')

    @public_method
    def doCommand(self,command=None,parameters=None):
        try:
            cmdlist = command.split(' ')
            command = cmdlist.pop(0)
            cmd = getattr(sh,command)
            return cmd(*cmdlist) if cmdlist else cmd()
        except Exception as e:
            return str(e)