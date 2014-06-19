dataController
--------------

A differenza del **dataFormula**, un **dataController** non restituisce un valore ma esegue un
blocco di codice Javascript.

GET SET FIRE
------------

Per rendere più facile la scrittura del codice in Genropy sono implementate 
delle MACRO Javascript che consentono un comodo accesso al datastore.

**GET** serve a leggere all'interno di un blocco di Javascript il valore al path richiesto.
Ad esempio: ::
 
 var x = GET .miodato;
 var z = GET .dato.cliente.nome;
 
**SET** consente di scrivere ad un path un valore. Esempio: ::
 
 SET .miodato = 34;
 SET .dato.nuovo = GET .dato.vecchio + 333;
 
**FIRE** si comporta come una **SET** ma invece di lasciare il valore al path,
immediatamente dopo lo porta a **null**. La ragione è che se si scrive ad un path
del datastore un valore uguale al precedente, questo **NON** fa scattare la notifica
di cambiamento e quindi i path attivi non vengono richiamati.
Con la MACRO **FIRE** invece si crea un **impulso** che subito viene riposrato
a null e di conseguenza un nuovo **FIRE** farà riscattare gli elementi collegati.
Scrivendo **FIRE .foo** viene scritto **true**. Si può anche scrivere **FIRE.foo= xx** 
dove **xx** è un valore desiderato. Di norma se non si è interessati al valore
(ovvero nel caso di FIREsenza valore specificato), è consuetudine sottoscrivere
col parametro **_fired**.
Se invece, pur firato, si desidera il valore, di norma si colleca ad un parametro 
dal nome più significativo.

Lo scope degli script Javascript
--------------------------------

Tutti gli script javascript richiamati in Genropy e quindi per ora abbiamo visto **action=**
del **Button**, **dataFormula** e **dataController**, vengono eseguiti nello **scope** del 
nodo di struttura che li definisce. Per questo motivo, nelle MACRO i path
relativi sono conteggiati a partire dal datapath corrente del nodo che li definisce.


Esempi nella pagina
-------------------

Al solito la pagina contiene vari esempi che andremo a commentare.

bytesConverter
--------------

Al accettazione del valore al path '^.bytes', scatta il **dataController** che va a settare 
al path '.conv' il risultato.


eratostene
----------

Nell'esempio eratostene introduciamo per la prima volta le validazioni. La 
**validate_min** e **validate_max** con i loro rispettivi messaggi di errore
**validate_min** e **validate_max**. Si noti inoltre il 
parametro **validate_onReject** che consente di avere una **callback** quando il
valore è rifiutato in modo da poter eseguiore del codice di cleanup.
Apuro scopo didattico viene anche usata una **_if** per impedire l'esecuzione 
del **dataController** in caso di valore non valido.
Data la presenza della validazione sul widget questo non dovrebbe accadere.
Se tuttavia con il **dataInspector** si provasse a forzare un valore non ammesso,
questo controllo interverrebbe.

Notiamo l'utilizzo di **script** come elemento HTML per aggiungere codice javascript
alla pagina. In questo caso definiamo una funzione **eratostene(nMax)** che andremo
poi ad invocare nel dataController.

clickToDecrement
----------------
In questo esempio viene messo un valore al path '.counter'. Il bottone 'Decrement'
esegue un **FIRE** su un path '.decrement' sottoscritto tramite path attivo 
da un **dataController** che provvede a settare al path '.counter' il valore letto 
e quindi decremetato.

autoDecrement
-------------

Questo esempio si propone di mostrare il parametro speciale **_timing** 
che serve  a richiamare continuativamente un **dataController** con un intervallo di
tempo desiderato.
Notiamo che con l'istruzione **data** inizializziamo il valore del **timing** a 0.
Non appena digitiamo un valore nel campo (path a  '^.start') scatta un dataController
che copia il valore nel path **'.counter'** e provvede a mettere in **'.timing'** il valore '0.1'
che corrisponde ad un decimo di secondo.
Appena viene posto un valore il timing inizia ad azionare il **dataController** 
ogni decimo di secondo. Il dataController decrementa il counter e se 
arriva a zero disattiva il timer ponendo '.timing' a 0.

Si noti che per rendere più evidente il count down il font-size del counter
viene pilotato dal valore del counter stesso.






















 
