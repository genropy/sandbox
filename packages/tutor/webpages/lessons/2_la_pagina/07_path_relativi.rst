Path Relativi
-------------

Abbiamo visto che è possibile leggere e scrivere nel
datastore usando il path del valore cercato.

Per consentire di gestire ageolmente strutture nidificate è anche possibile utilizzare il cancetto di path relativo. Per usare un path relativo è necessario definire in un certo nodo un **datapath** assoluto 
e questo farà si che negli elementi annidati sia possibile usare un datapath relativo ovvero che inizia con **'.'**.

Facciamo un esempio::

 se nel nostro datastore abbiamo:
 
   province
     MI
       Milano
     TO
       Torino
       
       
allora avremo ::

 pane=root.div(datapath='province')
 pane.div('^.MI') # mostra Milano
 pane.div('^.TO') # mostra Torino
 
 
I datapath possono essere plurilivello e quindi un datapath può a sua volta essere relativo.

ad esempio ::

  se nel nostro datastore abbiamo:
  
   dati_geografici
     province
       MI
         Milano
       TO
         Torino
     regioni
       LOM
         Lombardia
       PIE
         Piemonte
         
         
         
         
Potremo scrivere::

 geografici=root.div(datapath='dati_geografici')
 
 province=geografici.div(datapath='.province')
 province.div('^.MI') # mostra Milano
 province.div('^.TO') # mostra Torino
 
 regioni=geografici.div(datapath='.regioni')
 province.div('^.LOM') # mostra Lombardia
 province.div('^.PIE') # mostra Piemonte
 
 
Nel caso della nostra pagina abbiamo un datapath **clients**
nel quale vengono aggiunti 3 clienti con datapath relativo '.c_1', '.c_2' e '.c_3'
A questo punto le chiamate successive, operndo su path relativi sono 'rilocabili' e quindi
riescono a gestire un indirizzamento relativo al blocco corrente.




         