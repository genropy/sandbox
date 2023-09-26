def main(db):

     prodotti_tipo = db.table('fatt.prodotto_tipo').query().fetch()
     print('Migrazione tipi prodotto da fatt a mag_light')
     for pdttipo in prodotti_tipo:
         db.table('mag_light.prodotto_tipo').insert(pdttipo)
     
     print('Migrazione prodotti da fatt a mag_light')
     prodotti = db.table('fatt.prodotto').query().fetch()
     for pdt in prodotti:
          db.table('mag_light.prodotto').insert(pdt)

     print('Migrazione allegati prodotto da fatt a mag_light')
     prodotti_atc = db.table('fatt.prodotto_atc').query().fetch()
     for pdtatc in prodotti_atc:
          db.table('mag_light.prodotto_atc').insert(pdtatc)

     db.commit()