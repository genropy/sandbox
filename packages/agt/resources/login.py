
from gnr.web.gnrwebpage import BaseComponent
import datetime

class LoginComponent(BaseComponent):
    def onAuthenticating_agt(self, avatar, rootenv=None):
        agente = self.db.table('agt.agente'
                ).query(where='$user_id=:user_id', 
                user_id=avatar.user_id).fetch()
        if agente:
            rootenv['agente_id'] = agente[0]['id']
            rootenv['login_time'] = datetime.datetime.now()