from gnr.core.gnrbag import Bag, DirectoryResolver
from gnr.core.gnrdecorator import public_method
from gnr.app.gnrconfig import getGenroRoot
import os
PATH = getGenroRoot()

class GnrCustomWebPage(object):
    
    def main(self,root,**kwargs):
        bc=root.borderContainer(datapath='diskviewer')
        left=bc.contentPane(region='top',height='50%',padding='4px',
                            splitter=True)
        left.data('.root.genropy',DirectoryResolver(PATH)())
        left.tree(storepath='.root',hideValues=True, 
                  selectedLabelClass='selectedTreeNode',
                  selected_abs_path='.abs_path',
                  labelAttribute='nodecaption',autoCollapse=True)
        left.dataRpc('.content',self.getContent, filepath='^.abs_path')
        bc.contentPane(region='center').pre(value='^.content',font_size='.8em')
        
    @public_method    
    def getContent(self,filepath=None,**kwargs):
        filepath=os.path.join(PATH,filepath)
        with open(filepath,'r') as f:
            data=f.read()
        return data