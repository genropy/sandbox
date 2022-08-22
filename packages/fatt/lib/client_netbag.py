
from gnr.core.gnrbag import NetBag

fatture = NetBag('http://external:3xt3rn4l@localhost:8081/fatt/test_netbag','lista_fatture',cliente='Berlucchi',limit=3,output='v')
print(fatture['#0.protocollo'])
#fatture = fatture()
#print('fatture\n',fatture)