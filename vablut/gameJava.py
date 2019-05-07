# -*- coding: utf-8 -*-
import socket
import json

import numpy as np
from vablut.engine.random import RandomEngine
from vablut.modules.Utils import utils
from vablut.board import Board, PLAYER1, PLAYER2, KING_VALUE, DRAW

HOST = "localhost"
WHITEPORT = 5800
BLACKPORT = 5801
NAME = "TABRUTT"

#deve poter accettare un parametro che definisce se sei nero o bianco, nel costruttore chiamato engine
class GameJavaHandler(object):    
    def __init__(self, engine, playerType, verbose=False):
        self.engine     = engine
        self.verbose    = verbose
        self.playerType = playerType

    def play(self):
#1       
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if(self.playerType.upper() == 'WHITE'): #l'idea è quella di estrarre una property dall'engine che mi dica chi è
            sock.connect((HOST, WHITEPORT))
        else:
            sock.connect((HOST, BLACKPORT))
#2
        x = json.dumps(NAME)
        utils.write_utf8(x, sock)
#3
        state = utils.read_utf8(sock)
        state_pos = self.from_json_to_pos(state)
        board = Board(state_pos, draw_dic={})
        while(True):
            print(board)
            if(self.playerType.upper() == 'WHITE'):
                state = utils.read_utf8(sock)
            else:
                state = utils.read_utf8(sock)

    @classmethod
    def from_json_to_pos(cls, gson_state):
        state   = json.loads(gson_state)
        pos     = np.asarray(state['board']).flatten()
        pos[pos=='EMPTY'] = 0
        pos[pos=='BLACK'] = int(PLAYER1)
        pos[pos=='WHITE'] = int(PLAYER2)
        pos[pos=='KING']  = int(KING_VALUE)
        pos = np.asarray(pos, dtype=int)
        return Board.from_pos_to_dic(pos) 
        
gh= GameJavaHandler(RandomEngine, 'white', True)
gh.play()

#cosa fare?
        #1-connettersi a localhost (andare a vedere le porte)
        #2-inviare nome es. "TABRUTT"
        #3-mettersi in lettura (che restituisce lo stato) con un while. Se whitewin, bw o draw esce da while, altrimenti
            #3.1-ricostruire lo stato
            #3.2-valutare il turno (capire a chi tocca)
            #3.3-agire di conseguenza chiamando i metodi dell'engine / se non tocca a me ripetere read bloccante (punto 3)