Containers
----------

Per creare pagine complesse sono disponibili dei **widget** di tipo **container**.

I principali sono:

  - contentPane
  - tabContainer
  - borderContainer
  - stackContainer


Il **contentPane** è l'unico che può contenere element HTML o widget. Può anche contenere un altro
**container** ma in tal caso deve essere **figlio unico**.

Il **tabContainer** serve a mettere nello stesso spazio più 
contenuti organizzati in pagine attivate da **'tab'**. Al **tabContainer** è possibile 
aggiungere dei **contentPane** oppure dei **container**. Quando si aggiunge un
figlio deve essere specificato un **title**.
Il **tabContainer** deve avere una **height** e una **width** e ogni figlio occupa
il 100% dello spazio disponibile.

Il **borderContainer** permette di suddividere lo spazio interno in 5 region:

 - top
 - bottom
 - left
 - right
 - center
 
Il **center** prende tutto lo spazio libero mentre per le region **left** e **right** è possibile dare una **width**.
Per **bottom** e **top** è possibile specificare ***height**.
A tutte le region tranne **center** è possibile assegnare **Splitter=True** per richiedere uno splitter.
Ogni **region** può essere o un **contentPane** oppure un container.

Lo **stackContainer** è simile al **tabContainer** ma non mostra delle etichette per
selezionare la pagina voluta. Invece ha un attributo **selected** che assume il valore della 
pagina selezionata e cambiando questo valore viene cambiata la pagina corrente.