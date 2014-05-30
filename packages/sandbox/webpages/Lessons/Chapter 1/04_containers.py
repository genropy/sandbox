# -*- coding: UTF-8 -*-
            
class GnrCustomWebPage(object):
    py_requires = 'source_viewer'
    js_requires='codemirror/lib/codemirror,codemirror/mode/python/python.js,skulpt.min.js,skulpt-stdlib'
    css_requires='codemirror/lib/codemirror.css'
    def main(self,root,**kwargs):
        root.div(margin='10px',width='600px',height='700px',
               border='1px solid silver',onCreated="""
               function(obj,attr){
                   this.externalWidget=CodeMirror(obj,{mode:'python',
                                 lineNumbers:true})
               }
               """)    
