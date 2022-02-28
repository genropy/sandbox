# -*- coding: UTF-8 -*-

class GnrCustomWebPage(object):

    def main(self,root,pkey=None,template=None,**kwargs):
        root.templateChunk(table='fatt.prodotto',record_id='^mypkey',template=template,
                            height='600px',width='600px',border='1px solid silver',
                            editable=True)
        root.dataFormula('mypkey','pkey',pkey=pkey,_onStart=True)