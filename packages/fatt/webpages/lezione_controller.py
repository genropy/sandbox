# -*- coding: utf-8 -*-

"""Lezione controller"""

from builtins import object
class GnrCustomWebPage(object):
    py_requires = "gnrcomponents/testhandler:TestHandlerBase"
    
    
    def test_1_compatta(self, pane):
        """Notazione compatta"""
        pane.checkbox('^.accetto','Accetto le condizioni')
        pane.checkbox('^.voglio_spam','Voglio spam')
        pane.button('Attiva il servizio', disabled='^.accetto?=!#v')




    def test_2_entrambi(self, pane):
        """Condizione basata su due campi con variabile d'appoggio """
        pane.checkbox('^.accetto','Accetto le condizioni')
        pane.checkbox('^.voglio_spam','Voglio spam')

        pane.button('Attiva il servizio', disabled='^.disabilita_attivazione')

        pane.dataFormula('.disabilita_attivazione', 
                        '(!accetto || !voglio_spam)',
                        accetto = '^.accetto',
                        voglio_spam = '^.voglio_spam',
                        _onStart=True)

        #pane.data('.disabilita_attivazione', True)

    def test_3_entrambi_ugualeuguale(self, pane):
        """Condizione basata su due campi senza variabile d'appoggio """
        pane.checkbox('^.accetto','Accetto le condizioni')
        pane.checkbox('^.voglio_spam','Voglio spam')
        pane.button('Attiva il servizio',
                    disabled='==(!cond || !spam)',
                    cond = '^.accetto',
                    spam = '^.voglio_spam')

    def test_4_stack(self, pane):
        bc = pane.borderContainer(height='400px')
        top = bc.contentPane(region='top', height='50px')
        top.checkbox('^.accetto','Accetto le condizioni')
        top.checkbox('^.voglio_spam','Voglio spam')
        top.button('Configura', action='SET .pagina_selezionata = "configurazione";')
        top.dataFormula(".pagina_selezionata",
                        '(cond && spam)?"libero":"bloccato"',
                        cond = '^.accetto',
                        spam = '^.voglio_spam',
                        _onStart=True)

        sc = bc.stackContainer(region='center', selectedPage='^.pagina_selezionata')

        sc.contentPane(background_color='red', pageName='bloccato').div('Accetta altrimenti nisba', 
                                                    color='white', 
                                                    font_size='48pt')
        sc.contentPane(background_color='green', pageName='libero').div('Benvenuto',
                                                    color='white', 
                                                    font_size='48pt')
        sc.contentPane(background_color='black', pageName='configurazione').div('Configura tutto',
                                                    color='white', 
                                                    font_size='48pt')
        


        