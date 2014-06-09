Widget
------

Per scrivere interfacce complesse Genropy offre, in aggiunta agli elementi HTML, una larga collezione di widget che sarà in dettagli esaminata nel capitolo ad essi dedicato.

Per ora mostrima solo brevemente alcuni di essi senza addentrarci nell'esame dei parametri che possono essere passati.

Si noti come muovendo lo slider cambi l'arrotondamento del contenitore della form perchè l'attributo **rounded** invece di essere una costante, è rappresentato dal path '^.rounded' 
che è anche sottoscritto dallo **slider**. 

Come ulteriore esempio di dinamicità si può notare che il formbuilder ha l'attibuto **lbl_color** al path '^.lblcolor'.
Sullo stesso path è collocato il widget **comboBox**. Selezionando in esso un valore corretto, si vedrà mutare il colore delle label dei campi.
Trattandosi di  **comboBox**, oltre ai valori da menù, sarà possibile scrivere qualunque valore in aggiunta a quelli previsti.

Il Button **Submit** mostra il valore dei dati come Xml.