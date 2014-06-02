# -*- coding: UTF-8 -*-

from gnr.core.gnrdecorator import public_method
from gnr.core.gnrbag import Bag

class GnrCustomWebPage(object):
    def main(self,root,**kwargs):
        bc = root.borderContainer(datapath='main')
        left = bc.framePane(region='left',width='50%',splitter=True,margin='2px',margin_right=0,border='1px solid #efefef')
        left.center.contentPane(overflow='hidden').codemirror(value='^.source',height='100%',
               config_mode='rst',config_lineNumbers=True,config_keyMap='softTab')
        
        editorbar = left.top.slotToolbar('5,editmenu,*',height='22px')
        editorbar.data('.editor.menuoptions',self.editor_menuoptions())
        editorbar.editmenu.dropDownButton('Edit').menu(storepath='.editor.menuoptions',
                                                      action='alert($1.code);',_class='smallMenu')

        right = bc.framePane(region='center',margin='2px',border='1px solid #efefef')
        renderingbar = right.top.slotToolbar('5,style_selector,*',height='22px')
        fb = renderingbar.style_selector.formbuilder(cols=1,border_spacing='0px')
        fb.filteringSelect(value='^.rendering.theme',lbl='Theme',
                            values='violet:Violet,gray:Gray,standard:Standard')
        iframe = right.center.contentPane(overflow='hidden').htmliframe(height='100%',width='100%',border=0)
        bc.dataController('iframe.domNode.contentWindow.document.body.innerHTML = rendering',
                            rendering='^.rendering.html',
                            iframe=iframe)
        bc.dataRpc('.rendering.html',self.convert_rst2html,source_rst='^.source',
                    theme='^.rendering.theme',
                    _delay=500)

    def editor_menuoptions(self):
        result = Bag()
        result.setItem('bold',None,caption='Bold',code='bold')
        result.setItem('italic',None,caption='Italic',code='italic')
        return result

    @public_method
    def convert_rst2html(self,source_rst=None,theme=None,**kwargs):
        return self.site.getService('rst2html')(source_rst,
                                    theme=theme,**kwargs)