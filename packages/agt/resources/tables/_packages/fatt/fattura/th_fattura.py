
from gnr.web.gnrbaseclasses import BaseComponent

class View(BaseComponent):
    
    def th_options(self):
        return dict(partitioned=True)
