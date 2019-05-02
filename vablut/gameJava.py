# -*- coding: utf-8 -*-

#deve poter accettare un parametro che definisce se sei nero o bianco, nel costruttore chiamato engine
class GameJavaHandler(object):
    def __init__(self, engine, verbose=False):
        self.engine = engine
        self.verbose = verbose
#cosa fare?
        #1-connettersi a localhost (andare a vedere le porte)
        #2-inviare nome es. "TABRUTT"
        #3-mettersi in lettura (che restituisce lo stato) con un while. Se whitewin, bw o draw esce da while, altrimenti
            #3.1-ricostruire lo stato
            #3.2-valutare il turno (capire a chi tocca)
            #3.3-agire di conseguenza chiamando i metodi dell'engine / se non tocca a me ripetere read bloccante (punto 3)