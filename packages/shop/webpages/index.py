# -*- coding: utf-8 -*-
            
import urllib.parse
def make_maps_url(address: str) -> str:
    # converte l'indirizzo in formato URL-safe
    return "https://www.google.com/maps?q=" + urllib.parse.quote(address)

class GnrCustomWebPage(object):
    py_requires = 'plainindex'
    

    def fi_get_owner_name(self):
        return '^gnr.app_preference.adm.instance_data.owner_name'


    def windowTitle(self):
        return self.dbstore or self.getPreference('instance_data.owner_name',pkg='adm')
        

    def index_dashboard(self,pane):
        box = pane.div(position='absolute',top=0,bottom=0,right=0,left=0,overflow='hidden')
        if not self.dbstore:
            src = self.getResourceUri(self.index_url,add_mtime=self.isDeveloper())
            box.htmliframe(height='100%', width='100%', src=src, border='0px',shield=True)   
            return
        

        with open(self.getResource('splashscreen_template.html',pkg='shop'), 'r', encoding='utf-8') as f:
            template = f.read()
            keys = ["shop_name", "logo_path", "tagline", "address", "maps_url"]

            # 1) escapa tutte le graffe letterali
            safe = template.replace('{', '{{').replace('}', '}}')

            # 2) ripristina i placeholder noti
            for k in keys:
                safe = safe.replace('{{'+k+'}}', '{'+k+'}')
            shop_preference = self.getPreference('',pkg='shop')
            address = shop_preference['tagline'] or ''
            html = safe.format(
                shop_name=shop_preference['shop_name'],
                logo_path=shop_preference['logo_path'],
                tagline=shop_preference['tagline'],
                address=address,
                maps_url=make_maps_url(address)
            )
        box.htmliframe(height='100%',width='100%',srcdoc=html,shield=True)