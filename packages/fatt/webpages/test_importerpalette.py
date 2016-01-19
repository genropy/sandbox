# -*- coding: UTF-8 -*-

# dataremote.py
# Created by Francesco Porcari on 2010-10-29.
# Copyright (c) 2010 Softwell. All rights reserved.

"""dataRemote"""

from gnr.core.gnrdecorator import public_method

class GnrCustomWebPage(object):
    py_requires = "gnrcomponents/testhandler:TestHandlerFull"
    
    def test_1_basic(self, pane):
        """dataRemote basic example"""
        bc = pane.borderContainer(height='800px')
        fb = bc.contentPane(region='top').formbuilder()
        fb.paletteImporter(paletteCode='testimporter',
                            dockButton_iconClass='iconbox inbox',
                            title='!!Table from csv/xls',
                            importButton_label='Import test',
                            importButton_action="""
                                    genro.publish('importa_file',{filepath:imported_file_path,parametrone:parametrone})
                                """,
                            importButton_ask=dict(title='Parametrone',fields=[dict(name='parametrone',lbl='Name')]),
                            matchColumns='*')
        fb.dataRpc('dummy',self.importaFileTest,subscribe_importa_file=True,
            _onResult="""
                console.log('uuu',result);
                genro.publish('testimporter_onResult',result);
            """,_onError="""
                genro.publish('testimporter_onResult',{error:error});
            """)

    @public_method
    def importaFileTest(self,filepath=None,parametrone=None):
        print 'filepath',filepath,'parametrone',parametrone
        if parametrone=='mario':
            return dict(error='nome non ammesso')
        else:
            return dict(message='tutto bene',closeImporter=True)

