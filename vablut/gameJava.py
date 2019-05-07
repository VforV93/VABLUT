# -*- coding: utf-8 -*-

import socket
import json
from vablut.engine.random import RandomEngine

HOST = "localhost"
WHITEPORT = 5800
BLACKPORT = 5801

#deve poter accettare un parametro che definisce se sei nero o bianco, nel costruttore chiamato engine
class GameJavaHandler(object):
    def __init__(self, engine, playerType, verbose=False):
        self.engine = engine
        self.verbose = verbose
 #1       
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if(playerType.upper() == 'WHITE'): #l'idea è quella di estrarre una property dall'engine che mi dica chi è
            sock.connect((HOST, WHITEPORT))
        else:
            sock.connect((HOST, BLACKPORT))
#2
        x = "TABRUTT"
        #print(json.dumps(x))
        u = x.encode('utf-8')
        #temp = json.dumps(toSend)
        #temp = toSend.toByte
        #sock.sendall(json.dumps(x).encode('utf-8'))
        sock.send(len(u).to_bytes(2, byteorder='big'))
        sock.send(u)
        
#3
        #data=sock.read(1024)
        #print(data)
        
gh= GameJavaHandler(RandomEngine, 'white', True)
        
#cosa fare?
        #1-connettersi a localhost (andare a vedere le porte)
        #2-inviare nome es. "TABRUTT"
        #3-mettersi in lettura (che restituisce lo stato) con un while. Se whitewin, bw o draw esce da while, altrimenti
            #3.1-ricostruire lo stato
            #3.2-valutare il turno (capire a chi tocca)
            #3.3-agire di conseguenza chiamando i metodi dell'engine / se non tocca a me ripetere read bloccante (punto 3)