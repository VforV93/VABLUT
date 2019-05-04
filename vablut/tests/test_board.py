# -*- coding: utf-8 -*-
from vablut.board import *

#several test position
blacks = np.array([[0,0,0,1,1,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,1,0,0,0,0],
                   [0,1,0,0,0,0,0,1,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,1,1,0],
                   [0,0,0,0,0,0,0,0,0]])
whites = np.array([[0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,1,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,1,0,0,0],
                   [0,0,0,0,0,0,0,1,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,1,0,0,0,0,0,0,1],
                   [0,0,0,0,0,0,0,0,0]])
king  =  np.array([[0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,1,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0]])
pos1 = {PLAYER1:blacks, PLAYER2: (whites,king)}

blacks = np.array([[0,0,0,0,0,0,0,0,0],
                   [0,0,0,1,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,1,0,0,0,0],
                   [0,0,0,1,0,1,0,0,1],
                   [0,0,0,0,1,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,1,0,0,0,0],
                   [0,0,0,0,1,0,0,0,0]])
whites = np.array([[0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,1,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,1,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,1,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,1,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0]])
king  =  np.array([[0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,1,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0]])
pos2 = {PLAYER1:blacks, PLAYER2: (whites,king)}

def test_properties():
    boardP1 = Board(pos1, PLAYER1)
    boardP2 = Board(pos1, PLAYER2)
    assert boardP1.end is None,"board.end should be None"
    assert boardP2.end is None,"board.end should be None"

    assert boardP1.stm == PLAYER1,"board.stm should be PLAYER1"
    assert boardP1.stm != PLAYER2,"board.stm should be PLAYER1"
    assert boardP2.stm == PLAYER2,"board.stm should be PLAYER2"
    assert boardP2.stm != PLAYER1,"board.stm should be PLAYER2"

    assert boardP1.other == PLAYER2,"board.other should be PLAYER2"
    assert boardP2.other == PLAYER1,"board.other should be PLAYER1"

    pos =np.array([[0,0,0,1,1,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,2,0,0,0,0,0,0],
                   [0,0,0,0,1,0,0,0,0],
                   [0,1,0,0,0,2,0,1,0],
                   [0,0,0,0,0,0,0,2,0],
                   [0,0,0,0,3,0,0,0,0],
                   [0,2,0,0,0,0,1,1,2],
                   [0,0,0,0,0,0,0,0,0]])

    assert (boardP1.pos==pos).all(),"boardP1 should have %s like pos"%(pos)
    assert (boardP2.pos==pos).all(),"boardP2 should have %s like pos"%(pos)


def test_checkend():
    board = Board(pos2, PLAYER1,COMPUTE,39)
    print(board)

test_checkend()
#print(board1)