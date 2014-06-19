Data Formula
------------

Un **dataFormula** è un elemento attivo della pagina che puo ricevere vari
parametri sia come costanti che come riferimenti (*path attivi* e *passivi*) 
al datastore.

Parametri: ::

 pane.dataFormula(path, formula, parametri)
 
Al variare del valore di uno dei parametri la formula viene ricalcolata e il risultato
scritto nel datastore al path desiderato.

In questa pagina daremo vari esempi dell'uso di un **dataFormula**.

Si noti che nel **main** vengono chiamati 3 metodi differenti cui viene passato un **div**
con datapath. Il vantaggio è che in ogni esempio i dati sono relativi e non esiste 
il rischio di sovrapporre i nomi. 

Aprendo il **dataInspector** si potrà osservare il posizionamento nel datastore
dei vari valori.

triangleArea
------------

In un **formbuilder** vengono richiesti **Base** e **Height** che sono assegnati 
a **'^.base'** e **'^.height'**. Viene poi costruito un **div** che riceve il suo valore 
dal path **'^.area'** e al quale viene passato **_class='fakeTextBox'** per avere 
un disegno simile al **numberTextBox** senza consentire l'input. Si noti **claaa** + un nome
riservato in python e peranto si usa **_class**.

Viene poi costruito il **dataFormula** che riceve nei parameteri **b** e **h** 
il contenuto di **'^.base'** e **'^.height'**. La formula è calcolata e 
il valore savato in '.area'.

**Si noti che il path per il risultato della formula non inizia per '^' o per '='
perchè non è un valore dal datastore ma proprio un 'path'.**

Si noti anche l'uso di **default_value** per assegnare un valore iniziale.

colorMaker
-----------

Nel **div** passato dal **main** con datapath **'colormaker'** viene costruito 
un formbuilder con 4 colonne. Si noti l'attributo **lblpos ='T'** per avere le etichette in prima riga.

Nelle prime 3 celle verranno inseriti 3 **self.colorRgb**, uno per il **background_color** del quadrato di test, 
uno per il **color** e uno per **shadow_color**.

**self.colorRgb** è un metodo che costruisce un formbuilder innestato che a sua volta
contiene 3 **self.colorSlider**, uno *Red*, uno per *Green* e uno per *Blue*. 

Ogni **self.colorRgb** contiene un **dataFormula** che a partire da red,green e blue va a settare al
path reltivo **'.rgb'** la stringa corrispondente al valore rgb.

**self.colorSlider** è un **verticalSlider** che consente di selezionare un 
valore tra 0 e 255. Si noti anche il default_value è un numero casuale tra 0 e 255.


Si noti che i peth nel datastore sono su due livelli :

 - bkg
 
   - rgb
   - red
   - green
   - blue
    
 - color
   
   - rgb
   - red
   - green
   - blue
   
 - shadow
   
   - rgb
   - red
   - green
   - blue
   
Grazie ai path relativi è possibile riusare i metodi di costruzione e il codice è molto
più compatto e manutenibile.

personalBalance
---------------

In questo esempio vediamo nel **dataFormula** che calcola 'home_total' l'utilizzo di un parametro 'contenitore'.
In questo caso il valore che viene ricevuto non è un numero ma una **Bag** che contiene, come un dizionario python, più valori.
La Bag ha una metodo **sum** che viene usato in questo caso per calcolare la somma. Si noti che mettendo il path attivo ad un contenitore, 
la formula scatta quando un valore qualunque al suo interno cambia.

Le **Bag** rappresentano una struttura usatissima in Genropy sia in Python che in Javascript. Nel capitolo sulle Bag vedremo in dettaglio tutto quanto è necessario conoscere sulle bag.

_if e _else
-----------

Notiamo infine che in funzione del saldo un dataFormula provvede a mettere il valore in verde o rosso o blue.
Per farlo utilizza i parameteri **_if** e **_else** che offrono la possibilità di porre una condizione iniziale e di 
avere una modalità di calcolo per il caso di **else**.

