Formbuilder
-----------

Uno dei compiti più fastidiosi nella creazione di form è il piazzamento di coppie etichetta/valore in un modo semplice e con un risultato estetico gradevole.

In Genropy si utilizza il **formbuilder** che costruisce una tabella html nella quale piazza in modo automatico gli oggetti che vengono passati.

Al **formbuider** è possibile passare i numero di colonne su cui effettuare il piazzamento e anche dei parameteri di default per gli oggetti piazzati.

Nel codice di esempio vediamo per prima cosa 3 formbuilder con lo stesso datapath e che differiscono solo per il numero di colonne.

Osservando il codice del metodo **small** vediamo che viene creato un **div** con un **datapath**, la larghezza richiesta, un margine e un'ombreggiatura.
Viene poi messo un div con margine di 10px per lasciare un poco di spazio e quindi viene messo il **formbuilder** al quale si passa il parametero cols, la larghezza e i valori di default per gli oggetti contenuti.
In questo caso **fld_width** significa che per ogni valore è assegnata una larghezza del 100% come default.
Vengono anche passati dei parameteri di default per le
labels e precisamente **lbl_font_size** e **lbl_font_weight**

Una volta definito il formbuilder, si procede attaccando ad esso i vari oggetti ai quali si passa anche l'attributo **lbl** per specificare la label.
Nel nostro esempio per il campo **state** mostriamo come sia localmente possibile alterare gli attributi.
In questo caso la larghezza del campo e il colore della label.


Viene poi presentato l'esempio **large** in cui si mostra l'uso di **colspan** e **rowspan** per gestire piazzamenti più complessi.