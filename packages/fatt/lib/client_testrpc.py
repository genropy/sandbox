from datetime import datetime
import xmlrpclib
s = xmlrpclib.ServerProxy('http://sandbox:sandbox@localhost:8081/fatt/test_xmlrpc')
z = s.testlist()

print z

print s.lista_fatture(dict(cliente='effelunga'))

