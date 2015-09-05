import xmlrpclib
s = xmlrpclib.ServerProxy('http://sandbox:sandbox@localhost:8081/fatt/testrpc')

print s.lista_fatture(dict(cliente='effelunga'))

