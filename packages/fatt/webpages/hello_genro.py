# -*- coding: UTF-8 -*-
#from gnr.core.gnrbag import Bag
from gnr.core.gnrdecorator import public_method
from gnr.core.gnrbag import DirectoryResolver

class GnrCustomWebPage(object):
    def main(self,root,**kwargs):
        root.div('Ciao Silvano io sono la pagina %s' %id(self))
        root.button('Saluti al server',action='FIRE test')
        root.div('^risultato',color='green')
        root.dataRpc('risultato',self.salutiAlServer,_fired='^test')
        dirresolver = DirectoryResolver(self.site.getStaticPath('vol:dropbox'))
        root.data('dir.root',dirresolver())
        root.tree(storepath='dir')

        root.button('Fai foto da telecamera',action='FIRE camera_id=camera_id;',
                    ask=dict(title='Nome Camera',fields=[dict(name='camera_id',lbl='Camera ID')]))

        root.iframe(src='^risultato_foto')
        root.dataRpc('risultato_foto',self.faiFoto,camera_id='^camera_id')

    @public_method
    def faiFoto(self,camera_id=None):
        return self.site.getService('photo_ip').takePicture(camera_id=camera_id)


    @public_method
    def salutiAlServer(self):
        return 'Ciao dal bello io sono invece la pagina %s' %id(self)