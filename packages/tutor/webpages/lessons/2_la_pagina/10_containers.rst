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
figlio deve essere specificato un **title** e opzionalmente un **pageName**.
Il **tabContainer** deve avere una **height** e una **width** e ogni figlio occupa
il 100% dello spazio disponibile.

testTabContainer
----------------
Nell' esempio ad un **tabContainer** viene aggiunto un **contentPane** al cui interno è
posizionato un **div** il cui valore è al path **'^.showtime'**.
Un **dataFormula** ad ogni secondo ricalcola il valore formattando un oggetto **new Date()**
(si noti l'uso della macro **_F** per formattare un valore).
Viene poi aggiunto un **contentPane** con il title **Notes** nel quale è posta una **simpleTextArea** con opzione **editor=True**.
Questa opzione consente di avere un editor Html completo a disposizione.
Come terza pagina viene poi aggiunto un **tabContainer** che ha title **Calendar**.
A questo **tabContainer** vengono aggiunti 4 **contentPane** riempiti con i giorni dei prossimi 