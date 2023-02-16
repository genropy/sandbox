from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import oncalled

class ViewFromOfferta(BaseComponent):

    @oncalled
    def campi_extra(self,r,**kwargs):
        r.fieldcell('is_veneto')
