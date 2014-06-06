Model View Controller
=====================


In questo capitolo vedremo come si generano le pagine in Genropy e spiegheremo come è stato implementato in Genropy il
paradigma **Model View Controller** per gestire pagine molto complesse in modo semplice e manutenibile.

La pagina Genropy
-----------------

Ogni volta che una pagina viene richiesta al server, quest'ultimo provvede a restituire una pagina **HTML** molto 
semplice che contiene solo **javascript** e **css** necessari.

Alla ricezione della pagina **HTML** viene costruito un client javascript (**genro**) che richiede al server
la *ricetta* della pagina ovvero un **XML** che contiene tutti gli elementi necessari al client per costruire il **DOM**
(ovvero la View), i **dati iniziali** (Model)  e lo **logica** sul client. (Controller).

La *ricetta* viene analizzata e vengono costruiti tutti gli elementi necessari. A questo punto la pagina è attiva e inizierà a dialogare col
server per inviare informazioni o riceverne. 

Il tempo di vita di una pagina può essere molto lungo e quindi anche se il primo caricamento può essere meno veloce di
una pagina **HTML** il vantaggio di usare la stessa pagina per lungo tempo rende poi molto più veloce il lavoro successivo.

Source
------
Una pagina si basa su una struttura in memoria che contiene le informazioni necessarie per costruire il **DOM** e gestire i dati.
La struttura (**Source**) non è però immutabile e ogni cambiamento fatto in essa genera una ricostruzionedella parte interessata.
Per questa ragione le pagine non sono immutabili ma possono modificarsi in base a scelte dell'utente.

Datastore
---------
Oltre al **Source** il client **genro** contiene anche un **Datastore**. Si tratta di uno store gerarchico costituito da nodi
che hanno un valore e degli attributi. Per accedere ad un elemento si utilizza un path gerarchico.
Ad esempio *'miodato'* oppure *'miorecord.nome_utente'* oppure ancora *'persona.indirizzo.privato'*.
Oltre al valore in un nodo sono presenti attributi. Per accedere tramite path agli attributi si utilizza : *'path?nomeattributo'*.
Tornando agli esempi precedenti potremmo avere quindi *'miorecord.nome_utente?valore_precedente'*
