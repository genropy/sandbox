from datetime import datetime
from xmlrpclib import ServerProxy

s = ServerProxy('http://external:3xt3rn4l@localhost:8081/fatt/test_xmlrpc')
z = s.lista_fatture(dict(cliente='Effelunga',
                    importo=54031,a_partire_dal=datetime(2015,1,1)))

print z


