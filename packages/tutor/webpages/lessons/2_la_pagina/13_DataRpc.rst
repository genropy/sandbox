dataRpc
-------

Un **dataRpc** è simile ad un **dataFormula** con la differenza che l'elaborazione è svolta in **python** sul server.

Vediamo direttamente alcuni esempi d'uso.


serverDatetime
--------------

In questo primo esempio il bottone genera un **fire** sul path *'get_datetime'*
che è sottoscritto dal parametro fittizio **_fired** del **dataRpc**.
Nei **dataRpc** i parametri che iniziano con '_' non vengono inviati al server.
il **dataRpc** chiama quindi il metodo di pagina **getNow** che deve, per motivi
di sicurezza, essere decorato con il decoratore @public_method.
Il server rende il datetime corrispondente che il **dataRpc** provvedea 
mettere nel path '.now'. Questo path è sottoscritto da un **dataContrller** che 
al variare del valore attiva un **alert**.


QuickGrid
---------

Nei prossimi 2 esempi useremo per la prima volta il widget **QuickGrid** senza peraltro 
entrare in dettaglio sul suo funzionamento. Tale widget consente di visualizzare come tabella
una zona dello store creata da una Bag. Nel suo utilizzo  minimale la **quickGrid** è in grado di 
desumere la formattazione e le intestazioni dal contenuto della Bag.

cpuTimes
--------

In questo esempio viene creata una **quickGrid** che ha come **value** *'^.data'*.
Viene poi definita una **dataRpc** che è attivata allo start e poi ogni 5 secondi.
Tale **dataRpc** chiama il metodo del server **getCpuTimes**.
Tale metodo crea una Bag vuota e poi chiama un metodo di **psutils** che rende 
per ogni core del sistema le informazioni richieste.
Per ogni core viene creata una **Bag** con i valori della riga e tale riga viene 
quindi inserita nel risultato ad un path come **r_0**, **r_1** ecc..
La Bag con le righe viene quindi restituita al client dove la **QuickGrid**, al variare
del valore sottoscritto, provvede a ridisegnarsi.

*Si noti che cliccando sugli headers è possibile riordinare i valori.* 

processList
-----------

L'ultimo esempio è decisamente più ambizioso e complesso.

Per prima cosa viene preparata una stringa con i nomi delle possibili colonne. Poi in un
formbuider vengono richiesti alcuni parametri e al variare di questi viene chiamato il 
metodo della pagina **getProcessList**.
Questo riceve nei parametri le colonne che l'utente desideara vedere e filtra i processi
in base al nome, allo user e, se richiesto alla percenrtuale di Cpu e di memoria.
La Bag che risulta viene quindi visualizzata nella **quickGrid**







