Path Relativi
=============

Abbiamo visto che è possibile leggere e scrivere nel
datastore usando il path del valore cercato.
Per consentire di gestire ageolmente strutture nidificate è anche possibile
utilizzare il cancetto di path relativo. 
Per usare un path relativo è necessario definire in un certo nodo 
un **datapath** assoluto e questo farà si che negli elementi annidati
sia possibile usare un datapath **relativo** ovvero che inizia con **'.'**.

Se ad esempio nel datastore abbiamo:

 - province
 
   - MI : Milano
   - TO : Torino
  
Potremo nel codice scrivere: ::
 
 pane=root.div(datapath='province')
 pane.div('^.MI')
 pane.div('^.TO')
 
I datapath possono essere multilivello e quindi un datapath può a sua volta
essere relativo. Se ad esempio nel datastore abbiamo:

 - dati_geografici
 
  - province
  
    - MI : Milano
    - TO : Torino
   
  - regioni
  
    - LOM : Lombardia
    - PIE : Piemonte
  
Potremo scrivere nel codice: ::

 dg = root.div(datapath='dati_geografici')
 
 pane=dg.div(datapath='.province')
 pane.div('^.MI') 
 pane.div('^.TO') 
 
 pane=dg.div(datapath='.regioni')
 pane.div('^.LOM')
 pane.div('^.PIE')
 
  

Codice pagina
=============

Esaminando il codice della pagina vediamo che viene fornita una
lista di dizionari con i dati di alcuni clienti.

Viene per prima cosa creato un **div** con l'attributo **datapath='clients'**.
Questo elemento rappresenta l' **origine dei path relativi**. Ogni qualvolta usiamo dei path relativi
dobbiamo essere certi che siano contenuti anche indirettamente in un elemento con **datapath assoluto**.

Per ogni elemento della lista si chiama poi un metodo **clientRow** passando l'indice e i dati del cliente.

Client row prepara quindi un identificatore del cliente basato sul suo indice (c0,c1,c2...) e costruisce un div
con **datapath** uguale all'identificativo reso **relativo** anteponendo il simbolo '.'.
I datapath saranno quindi **'.c1', '.c2'** ecc..

Viene poi chiamato **setClientData** passando questo **div** e **setClientData** provvede a
mettere i dati desiderati sempre con path relativi come '.name' e '.location'.

Viene quindi messo un div con l'identificativo e un div per il contenuto. Quest'ultimo viene passato ai metodi
editClientData e showClientData che , sempre usando path relativi potranno completare la riga.


**Puoi usare il dataInspector per vedere e modificare i dati**


         