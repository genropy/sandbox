# -*- coding: UTF-8 -*-
            
class GnrCustomWebPage(object):
    def main(self,root,**kwargs):
        root.data('codetest','print "Test"')
        fb = root.formbuilder(cols=1,border_spacing='3px')
        fb.checkbox(value='^readOnly',lbl='readOnly')
        root.codemirror(value='^codetest',margin='10px',width='600px',height='300px',
               border='1px solid silver',config_mode='python',config_lineNumbers=True,
               readOnly='^readOnly',
               nodeId='testEditor')  

        root.simpleTextArea(value='^codetest')