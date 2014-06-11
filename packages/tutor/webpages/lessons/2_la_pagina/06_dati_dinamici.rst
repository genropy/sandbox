Path Attivo e Passivo
---------------------

In questa pagina vedremo che gli elementi possono essere collegati al datastore in due modalità: 
 - prefissati da '=' - (*path passivo*)
 - prefissati da '^' - (*path attivo*)
 
Nel caso siano prefissati da '=' allora il valore è letto dal datastore ma 
successivi cambiamenti non vengono notificati.

Nel caso invece il path inizi con '^' qualunque cambiamento del dato provoca
un aggiornamento.

Esaminiamo ora il codice dell'esempio. 
Per prima cosa notiamo che in questo caso lo store viene precaricato con un solo elemento **data** al quale viene passato un dizionario. 



Abbiamo ripreso l'esempio precedente ma questa
volta utiliziamo un elemento **input** che è collegato
al datastore con un *path attivo*.

Per semplificare la leggibilità e compattezza del codice abbiamo introdotto il metodo **labelDiv**
che rappresenta un primo esempio di componentizzazione. 
Tale metodo riceve un *pane* ed una *label* e resituisce un **div** con dentro uno **span** contenente la **label**.

L'esempio si compone di due blocchi: nel primo con degli elementi di **input** collegati al datastore con **path attivo**, si da modo di editare i valori nel datastore.
Nel secondo blocco invece sono presenti dei div collegati al datastore in modo differente.
L'elemento *name* (rosso) è collegato con un **path attivo** mentre il secondo, *location* (verde) è
collegato con un **path passivo**

Se editiamo i valori notiamo che solo quelli collegati con **path attivo** vengono aggiornati. 

**Puoi usare il dataInspector per vedere e modificare i dati**