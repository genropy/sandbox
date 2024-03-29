# -*- coding: UTF-8 -*-
from genericpath import exists
import requests
from zipfile import ZipFile
from gnr.core.gnrdecorator import public_method,extract_kwargs
from gnr.core.gnrbag import Bag,NetBag

class GnrCustomWebPage(object):
    def source_viewer_open(self):
        return False
        
    def main(self,root,**kwargs):
        root.div('LOCAL HANDBOOKS',background='#1e3055',
                    font_size='1.5rem',text_align='center',color='white',padding='10px', border_top='solid 2px white')
        root.div("""Da questa sezione è possibile scaricare i manuali aggiornati di Genropy. Gli esempi saranno interattivi, e sarà quindi possibile modificarli in tempo reale. 
                    <br>Ricordati di avviare la tua istanza con il parametro "remote_edit":""",
                    padding='40px 40px 10px 40px', font_size='14px')
        root.div('gnrwsgiserve sandboxpg --remote_edit', font_style='italic', padding='10px 40px', font_size='14px')
        root.br()
        tbl = root.div(margin='40px').table(datapath='main',font_size='1.2rem',color='#666',border_spacing='10px').tbody()
        local_handbooks = self.site.storageNode(self.localHandbooksPath())
        for row in self.interactiveHandbooks().digest('#a'):
            r = tbl.tr(datapath='.%s' %row['name'])
            r.td(row['title'],text_align='right')
            localfolder = local_handbooks.child(row['name'])
            r.data('.downloaded',localfolder.exists)
            download_url = row['download_url']
            r.td().lightbutton('^.downloaded?=#v?"Update":"Download"' ,
                    padding='5px',background='rgba(234, 203, 110, 1)',rounded=6,
                    download_url=download_url,width='10em',text_align='center'
                    ).dataRpc('.downloaded',self.downloadInteractiveHandbook, download_url=download_url, _lockScreen=True)
            r.td().lightbutton('Apri manuale',action="genro.openWindow(indexurl)",hidden='^.downloaded?=!#v',
                    width='10em',text_align='center',padding='5px',background='rgba(234, 203, 110, 1)',rounded=6,
                    indexurl=localfolder.child('index.html').url())

        root.div("""Una volta effettuato l'update, assicurati di aver svuotato la cache per visualizzare la versione aggiornata della documentazione""",
                    padding='40px 40px 10px 40px', font_size='14px')
    
    def localHandbooksPath(self):
        return 'documentation:local_handbooks'

    def docsUrl(self):
        return 'https://dev.genropy.org/gnet/handbooks'
    
    @public_method
    def interactiveHandbooks(self,project_code=None,package_identifier=None,
                                    table_identifier=None,pagename=None,**kwargs):
        result = NetBag(self.docsUrl(),'get_interactive_handbooks')()
        return result

    @public_method
    def downloadInteractiveHandbook(self, download_url=None,**kwargs):
        filezip = download_url.split('/')[-1]
        r = requests.get(download_url, stream=True)
        if r.ok:
            with self.site.storageNode(self.localHandbooksPath(),filezip).open('wb') as f:
                for chunk in r.iter_content(1024):
                    f.write(chunk)
            with self.site.storageNode(self.localHandbooksPath(),filezip).local_path() as path:
                myzip =  ZipFile(path, 'r')
                folderpath = path.replace('.zip','')
                myzip.extractall(folderpath)
                examples_sn = self.site.storageNode(folderpath,'_static','_webpages')
                if examples_sn.exists:
                    self.site.storageNode(folderpath,'_static','_webpages').move(dest='site:webpages/docu_examples')
        return True