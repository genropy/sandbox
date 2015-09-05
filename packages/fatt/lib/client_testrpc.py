import xmlrpclib
s = xmlrpclib.ServerProxy('http://fporcaru:ghigo@localhost:8081/fatt/testrpc')

print s.lista_fatture(dict(cliente='effelunga'))

