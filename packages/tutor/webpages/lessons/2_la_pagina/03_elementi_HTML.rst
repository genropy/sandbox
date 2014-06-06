Elementi HTML
-------------

In questa pagina viene mostrato come creare oggetti HTML vari.
Come regola generale si riceve un oggetto al quale si possono aggiungere **n** oggetti figli.

Esempio::

     def main(self,pane,**kwargs):
         pane.div('foo', color='red')
         pane.div('bar', color='lime')
         subpane = pane.div(color='pink',margin_left='5px')
         subpane.div('spam')
         subpane.div('eggs')
         
A **pane** aggiungiamo i div *foo* e *bar* e un div contenitore che chiamiamo **subpane**. In tale div aggiungeremo 2 div innestati.

Nel codice sotto riportato vengono costruiti con la stessa logica un contenitore di pallini variamente colorati e una tabella.

