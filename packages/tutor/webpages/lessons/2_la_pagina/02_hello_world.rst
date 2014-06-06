Hello World
-----------

In questa pagina viene presentato il primo esempio della sintassi di Genropy.

Per prima cosa viene definita una classe **GnrCustomWebPage** che eredita da
object. Come vedremo in seguito tale classe ha solo la funzione di un
raccoglitore di metodi che verranno in seguito mixinati dinamicamente
alla pagina in esecuzione.

In ogni pagina deve essere definito metodo **main** che viene invocato
per costruire il contenuto della pagina.
A tale metodo viene passato un oggetto root e, nel caso la pagina sia
stata chiamata con parametri supplementari, verranno passati anche tali parametri.

Sull'oggetto **root** viene poi chiamata la funzione **div** che provvede
ad aggiungere a **root** un nodo di tipo **div**. Il primo parametro della funzione,
in questo caso *Hello world*, corrisponde al parametro **innerHTML**. 
Possiamo anche aggiungere attributi come ad esempio **font_size**.

Come vedremo nella prossima pagina ogni  elemento **html** può essere aggiunto nello stesso modo.

