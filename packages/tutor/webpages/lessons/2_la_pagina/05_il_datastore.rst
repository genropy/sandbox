Datastore
---------

Le pagine di Genropy utilizzano un datastore locale che contiene tutti i dati necessari.

In questo primo esempio vediamo che nel metodo **main** chiamiamo **setClientData**.
Questo metodo utilizza il tag speciale  **data** che provvede a settare 
nello **store del client** al *path* indicato il 
*valore* desiderato

Il metodo **showClientData** utilizza la sintassi *'=path_dato_voluto'* per indicare
che il contenuto dello span è all'indirizzo che segue il simbolo **'='**

Nella prossima pagina vedremo altri aspetti dell'uso del datastore.

Nelle toolbar sopra il codice python c'è un icona che apre il **data Inspector**, 
una palette che mostra il contenuto dello store.
Selezionando un elemento dell'albero è possibile editare il valore e gli 
attributi del nodo e i cambiamenti saranno visibili nella pagina.

Ad esempio selezionando nell **data Inspector** il path *client.name* vedremo in *value* 'John Brown'.
Se con un doppio click editiamo il nome mettendo ad esempio 'Mary Jones' il nuovo valore sarà visibile nella pagina.

**Per qualunque ragione un valore nel datastore cambi, ogni cambiamento sarà propagato
agli elementi che sottoscrivono con un path attivo quell'elemento.**