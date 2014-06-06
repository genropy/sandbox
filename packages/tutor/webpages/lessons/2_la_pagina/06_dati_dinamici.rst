Dati Dinamici
-------------

In questa pagina vedremo che è possibile cambiare i valori nel datastore.

Per prima cosa, in base alla regola del *Suddividere il codice* abbiamo
identificato che per ogni riga abbiamo dovuto mettere una *label* ed un valore, 
o meglio, il *path* ad un valore.
Abbiamo quindi creato il metodo **setRow** che riceve il *pane*, la *label* e il *path*.

Questo metodo crea un **div** e al suo interno posiziona 2 **span**.
Il primo con la *label* il secondo con il *path*.

Nello span con la label abbiamo anche messo un **onclick** che ci dovrà 
chiedere il nuovo valore e provvedere a metterlo nel datastore.

Esaminiamo il **javascript** di questo gestore di **onclick**::

   var curr_value=genro.getData('%(path)s');
   var new_value=prompt('%(label)s',curr_value);
   genro.setData('%(path)s',new_value)


Notiamo la chiamata **genro.getData(path)** che prende dal datastore il valore corrente al path voluto.
Viene poi eseguito un **prompt(label,valore)** che presenta un box dove viene chiesto il valore
con la label data e mettendo come default il valore attuale.

Il valore restituito viene quindi scritto nel datastore con **genro.setData(path,valore)**

Esaminando il codice si può notare che i *div* di **Fixed Data** hanno un path 
che inizia con **'='** mentre in quelli di **Variable Data** il path inizia con **'^'**.

Cliccando sulle label potremo cambiare i valori nel datastore ma solo quelli che
iniziano con **'^'** mutano al variare del valore mentre gli altri restano fissi.

**I path che iniziano con '=' si limitano a prelevare i valori dal datastore ma non ricevono i cambiamenti.
I path che iniziano con '^' si auto aggiornano al variare del valore*** 


