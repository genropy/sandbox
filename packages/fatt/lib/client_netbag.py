
from gnr.core.gnrbag import NetBag

fatture = NetBag('http://external:3xt3rn4l@localhost:8081/fatt/test_netbag','lista_fatture',cliente='Berlucchi')
print fatture.keys()