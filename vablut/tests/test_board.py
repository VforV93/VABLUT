# -*- coding: utf-8 -*-
from vablut.board import *
import pytest

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

blacks = np.array([[0,0,0,0,1,0,0,0,0],
                   [0,0,0,0,1,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [1,0,0,0,0,1,0,0,0],
                   [1,1,0,0,0,0,1,0,0],
                   [0,0,0,0,0,1,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,1,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0]])
whites = np.array([[0,0,0,0,0,0,0,0,0],
                   [0,0,1,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,1,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,1,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,1,0,0,0],
                   [0,0,0,0,0,0,0,0,0]])
king  =  np.array([[0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,1,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0]])
pos3 = {PLAYER1:blacks, PLAYER2: (whites,king)}

blacks = np.array([[0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,1,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,1,0,0,0,0,0,0,0],
                   [0,1,0,0,0,0,1,1,0],
                   [0,1,0,0,0,1,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0]])
whites = np.array([[0,0,0,0,0,0,0,0,0],
                   [0,0,0,1,0,1,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,1,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,1,1,1,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0]])
king  =  np.array([[0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,1,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0]])
pos4 = {PLAYER1:blacks, PLAYER2: (whites,king)}

blacks = np.array([[0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,1,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,1,0,1,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0]])
whites = np.array([[0,0,0,0,0,0,0,0,0],
                   [0,1,0,0,0,0,0,0,0],
                   [0,0,0,0,1,0,0,0,0],
                   [0,0,0,0,1,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,1,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,1,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0]])
king  =  np.array([[0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,1,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0]])
pos5 = {PLAYER1:blacks, PLAYER2: (whites,king)}

blacks = np.array([[0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,1,0,0,0,0],
                   [0,1,0,0,0,0,0,0,0],
                   [1,0,0,0,0,0,0,0,1],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,1,0,0,0,1],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,1,0,1,1,0,0,0]])
whites = np.array([[0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,1,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,1,0,0,0],
                   [0,1,1,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0]])
king  =  np.array([[0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,1,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0]])
pos6 = {PLAYER1:blacks, PLAYER2: (whites,king)}

blacks = np.array([[0,0,0,0,0,0,0,0,0],
                   [0,0,0,1,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,1,0,0,0,0],
                   [0,0,0,0,0,1,0,0,1],
                   [0,0,0,0,1,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,1,0,0,0,0],
                   [0,0,0,0,1,0,0,0,0]])
whites = np.array([[0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,1,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,1,0,0,0,0,0,0,0],
                   [0,0,0,1,0,0,1,0,0],
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
pos7 = {PLAYER1:blacks, PLAYER2: (whites,king)}

blacks = np.array([[0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,1,0,1,0,1,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0]])
whites = np.array([[0,0,0,0,0,0,0,0,0],
                   [0,1,0,0,0,0,0,0,0],
                   [0,0,0,0,1,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,1,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,1,0,0],
                   [0,0,0,0,0,0,0,0,0]])
king  =  np.array([[0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0]])
pos8 = {PLAYER1:blacks, PLAYER2: (whites,king)}

blacks = np.array([[0,0,0,0,0,0,0,1,0],
                   [1,0,0,0,1,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [1,0,0,0,0,0,0,0,0],
                   [1,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,1,0,1,0,0,0,0]])
whites = np.array([[0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,1,0,1,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,1,0,0,0,0],
                   [0,0,0,0,1,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0]])
king  =  np.array([[0,0,0,0,0,0,1,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0]])
pos9 = {PLAYER1:blacks, PLAYER2: (whites,king)}

blacks = np.array([[0,0,0,0,0,0,0,1,0],
                   [1,0,0,0,1,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [1,0,0,0,0,0,0,0,0],
                   [1,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,1,0,1,0,0,0,0]])
whites = np.array([[0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,1,0,1,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,1,0,0,0,0],
                   [0,0,0,0,1,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0]])
king  =  np.array([[0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [1,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0]])
pos10 = {PLAYER1:blacks, PLAYER2: (whites,king)}

blacks = np.array([[0,0,0,0,0,0,0,1,0],
                   [1,0,0,0,1,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [1,0,0,0,0,0,0,0,0],
                   [1,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,1,0,1,0,0,0,0]])
whites = np.array([[0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,1,0,1,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,1,0,0,0,0],
                   [0,0,0,0,1,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0]])
king  =  np.array([[0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,1,0,0,0,0,0,0,0]])
pos11 = {PLAYER1:blacks, PLAYER2: (whites,king)}


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

    pos = np.array([[0,0,0,1,1,0,0,0,0],
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
    board1_1 = Board(pos1, PLAYER1, COMPUTE, 41)
    board1_2 = Board(pos1, PLAYER2, COMPUTE, 58)
    board1_3 = Board(pos1, PLAYER2, COMPUTE, 70)
    assert board1_1.end is None,"\n%s \n the end should be None"%(board1_1)
    assert board1_2.end is None,"\n%s \n the end should be None"%(board1_2)
    assert board1_3.end is None,"\n%s \n the end should be None"%(board1_3)
    
    board2_1 = Board(pos2, PLAYER2, COMPUTE, 31)
    board2_2 = Board(pos2, PLAYER2, COMPUTE, 39)
    board2_3 = Board(pos2, PLAYER2, COMPUTE, 41)
    board2_4 = Board(pos2, PLAYER2, COMPUTE, 49)
    assert board2_1.end is PLAYER1,"\n%s \n the end should be %s(PLAYER1)"%(board2_1,PLAYER1)
    assert board2_2.end is PLAYER1,"\n%s \n the end should be %s(PLAYER1)"%(board2_2,PLAYER1)
    assert board2_3.end is PLAYER1,"\n%s \n the end should be %s(PLAYER1)"%(board2_3,PLAYER1)
    assert board2_4.end is PLAYER1,"\n%s \n the end should be %s(PLAYER1)"%(board2_4,PLAYER1)

    board3_1 = Board(pos3, PLAYER2, COMPUTE, 32)
    board3_2 = Board(pos3, PLAYER2, COMPUTE, 42)
    board3_3 = Board(pos3, PLAYER2, COMPUTE, 50)
    board3_4 = Board(pos3, PLAYER1, COMPUTE, 41)
    board3_5 = Board(pos3, PLAYER1, COMPUTE, 12)
    board3_6 = Board(pos3, PLAYER2, COMPUTE, 37)
    assert board3_1.end is PLAYER1,"\n%s \n the end should be %s(PLAYER1)"%(board3_1,PLAYER1)
    assert board3_2.end is PLAYER1,"\n%s \n the end should be %s(PLAYER1)"%(board3_2,PLAYER1)
    assert board3_3.end is PLAYER1,"\n%s \n the end should be %s(PLAYER1)"%(board3_3,PLAYER1)
    assert board3_4.end is None,"\n%s \n the end should be None"%(board3_4)
    assert board3_5.end is None,"\n%s \n the end should be None"%(board3_5)
    assert board3_6.end is None,"\n%s \n the end should be None"%(board3_6)

    board4_1 = Board(pos4, PLAYER1, COMPUTE, 32)
    board4_2 = Board(pos4, PLAYER2, COMPUTE, 42)
    board4_3 = Board(pos4, PLAYER2, COMPUTE, 50)
    board4_4 = Board(pos4, PLAYER1, COMPUTE, 41)
    board4_5 = Board(pos4, PLAYER1, COMPUTE, 46)
    assert board4_1.end is None,"\n%s \n the end should be None"%(board4_1)
    assert board4_2.end is None,"\n%s \n the end should be None"%(board4_2)
    assert board4_3.end is None,"\n%s \n the end should be None"%(board4_3)
    assert board4_4.end is None,"\n%s \n the end should be None"%(board4_4)
    assert board4_5.end is None,"\n%s \n the end should be None"%(board4_5)
    
    draw_dic = {}
    board5_1 = Board(pos5, PLAYER2, COMPUTE, 55)
    board5_2 = Board(pos5, PLAYER2, COMPUTE, 57)
    board5_3 = Board(pos5, PLAYER1, COMPUTE, 47)
    board5_4 = Board(pos5, PLAYER1, COMPUTE, 65, draw_dic)
    assert board5_1.end is PLAYER1,"\n%s \n the end should be %s(PLAYER1)"%(board5_1,PLAYER1)
    assert board5_2.end is PLAYER1,"\n%s \n the end should be %s(PLAYER1)"%(board5_2,PLAYER1)
    assert board5_3.end is None,"\n%s \n the end should be None"%(board5_3)
    assert board5_4.end is None,"\n%s \n the end should be None"%(board5_4)
    board5_4again = Board(pos5, PLAYER1, COMPUTE, 65, draw_dic)
    assert board5_4again.end is DRAW,"\n%s \n the end should be DRAW"%(board5_4again)

    board6_1 = Board(pos6, PLAYER2, COMPUTE, 19)
    board6_2 = Board(pos6, PLAYER2, COMPUTE, 27)
    board6_3 = Board(pos6, PLAYER1, COMPUTE, 28)
    board6_4 = Board(pos6, PLAYER2, COMPUTE, 49)
    board6_5 = Board(pos6, PLAYER1, COMPUTE, 46)
    assert board6_1.end is PLAYER1,"\n%s \n the end should be %s(PLAYER1)"%(board6_1,PLAYER1)
    assert board6_2.end is None,"\n%s \n the end should be None"%(board6_2)
    assert board6_3.end is None,"\n%s \n the end should be None"%(board6_3)
    assert board6_4.end is None,"\n%s \n the end should be None"%(board6_4)
    assert board6_5.end is None,"\n%s \n the end should be None"%(board6_5)
    draw_dic = {}
    board7_1 = Board(pos7, PLAYER2, COMPUTE, 31, draw_dic)
    board7_2 = Board(pos7, PLAYER2, COMPUTE, 41)
    board7_3 = Board(pos7, PLAYER1, COMPUTE, 39)
    board7_4 = Board(pos7, PLAYER1, COMPUTE, 49)
    assert board7_1.end is None,"\n%s \n the end should be None"%(board7_1)
    assert board7_2.end is None,"\n%s \n the end should be None"%(board7_2)
    assert board7_3.end is None,"\n%s \n the end should be None"%(board7_3)
    assert board7_4.end is None,"\n%s \n the end should be None"%(board7_4)
    board7_1again = Board(pos7, PLAYER2, COMPUTE, 41, draw_dic)
    assert board7_1again.end is DRAW,"\n%s \n the end should be DRAW"%(board7_1again)

    board8_1 = Board(pos8, PLAYER2, COMPUTE, 32)
    board8_2 = Board(pos8, PLAYER2, COMPUTE, 34)
    assert board8_1.end is PLAYER1,"\n%s \n the end should be %s(PLAYER1)"%(board8_1,PLAYER1)
    assert board8_2.end is PLAYER1,"\n%s \n the end should be %s(PLAYER1)"%(board8_2,PLAYER1)

    board9 = Board(pos9, PLAYER1, COMPUTE, 6)
    board10 = Board(pos10, PLAYER1, COMPUTE, 18)
    board11 = Board(pos11, PLAYER1, COMPUTE, 73)
    assert board9.end is PLAYER2,"\n%s \n the end should be %s(PLAYER2)"%(board9,PLAYER2)
    assert board10.end is PLAYER2,"\n%s \n the end should be %s(PLAYER2)"%(board10,PLAYER2)
    assert board11.end is PLAYER2,"\n%s \n the end should be %s(PLAYER2)"%(board11,PLAYER2)

def test_orthogonalsegment():
    board1 = Board(pos1, PLAYER1, COMPUTE, 41)
    board3 = Board(pos3, PLAYER1, COMPUTE, 41)
    board6 = Board(pos6, PLAYER2, COMPUTE, 27)
    #b1: moving B FROM 31 TO 29, FROM 37 TO 39, FROM 43 TO 70
    #b1: invalid moving FROM 69 TO 57, FROM 3 TO 78
    r1_1 = np.asarray([0,0,1])
    r1_2 = np.asarray([1,0,0])
    r1_3 = np.asarray([1,2,0,1])
    assert (board1.orthogonal_segment(board1.pos, 31, 29)==r1_1).all(),"the orthogonal segment FROM %s TO %s should be %s and not %s"%(31,29,r1_1,board1.orthogonal_segment(board1.pos, 31, 29))
    assert (board1.orthogonal_segment(board1.pos, 37, 39)==r1_2).all(),"the orthogonal segment FROM %s TO %s should be %s and not %s"%(37,39,r1_2,board1.orthogonal_segment(board1.pos, 37, 39))
    assert (board1.orthogonal_segment(board1.pos, 43, 70)==r1_3).all(),"the orthogonal segment FROM %s TO %s should be %s and not %s"%(47,70,r1_3,board1.orthogonal_segment(board1.pos, 47, 70))
    with pytest.raises(ValueError):
        assert board1.orthogonal_segment(board1.pos, 69, 57)
        assert board1.orthogonal_segment(board1.pos, 3, 78)

    #b3: moving FROM 42 TO 38, FROM 65 TO 20
    #b3: invalid moving FROM 69 TO 57
    r3_1 = np.asarray([0,0,0,3,1])
    r3_2 = np.asarray([0,0,0,0,0,1])
    assert (board3.orthogonal_segment(board3.pos, 42, 38)==r3_1).all(),"the orthogonal segment FROM %s TO %s should be %s and not %s"%(42,38,r3_1,board3.orthogonal_segment(board3.pos, 42, 38))
    assert (board3.orthogonal_segment(board3.pos, 65, 20)==r3_2).all(),"the orthogonal segment FROM %s TO %s should be %s and not %s"%(65,20,r3_2,board3.orthogonal_segment(board3.pos, 65, 20))
    with pytest.raises(ValueError):
        assert board3.orthogonal_segment(board1.pos, 69, 57)

    #b6: moving FROM 46 TO 51, FROM 74 TO 20
    #b6: invalid moving FROM 77 TO 17
    r6_1 = np.asarray([2,2,0,1,0,0])
    r6_2 = np.asarray([0,0,0,2,0,0,1])
    assert (board6.orthogonal_segment(board6.pos, 46, 51)==r6_1).all(),"the orthogonal segment FROM %s TO %s should be %s and not %s"%(46,51,r6_1,board6.orthogonal_segment(board6.pos, 46, 51))
    assert (board6.orthogonal_segment(board6.pos, 74, 20)==r6_2).all(),"the orthogonal segment FROM %s TO %s should be %s and not %s"%(74,20,r6_2,board6.orthogonal_segment(board6.pos, 74, 20))
    with pytest.raises(ValueError):
        assert board6.orthogonal_segment(board6.pos, 77, 17)

def test_frompostodic():
    check_pos = pos5[PLAYER1] + 2*pos5[PLAYER2][0] + 3*pos5[PLAYER2][1]
    board5 = Board(pos5, PLAYER1, COMPUTE, 47)
    c_pos_dic = Board.from_pos_to_dic(check_pos)

    assert (board5._pos[PLAYER1].flatten()==c_pos_dic[PLAYER1].flatten()).all()
    assert (board5._pos[PLAYER2][0].flatten()==c_pos_dic[PLAYER2][0].flatten()).all()
    assert (board5._pos[PLAYER2][1].flatten()==c_pos_dic[PLAYER2][1].flatten()).all()
   
    board7 = Board(pos7, PLAYER2, COMPUTE, 41)
    assert not (board7._pos[PLAYER1].flatten()==c_pos_dic[PLAYER1].flatten()).all()
    assert not (board7._pos[PLAYER2][0].flatten()==c_pos_dic[PLAYER2][0].flatten()).all()

def test_posupdate():
    board5 = Board(pos5, PLAYER1, COMPUTE, 47)
    pos5_up_b  =  np.array([[0,0,0,1,1,1,0,0,0],
                            [0,2,0,0,1,0,0,0,0],
                            [0,0,0,0,2,0,0,0,0],
                            [1,0,0,0,2,0,0,0,1],
                            [1,1,0,0,1,0,0,1,1],
                            [1,0,2,0,0,0,0,0,1],
                            [0,1,3,1,0,0,0,0,0],
                            [0,0,2,0,1,0,0,0,0],
                            [0,0,0,1,1,1,0,0,0]])
    pos5_up_w  =  np.array([[0,0,0,2,2,2,0,0,0],
                            [0,2,0,0,2,0,0,0,0],
                            [0,0,0,0,2,0,0,0,0],
                            [2,0,0,0,2,0,0,0,2],
                            [2,2,0,0,2,0,0,2,2],
                            [2,0,2,0,0,0,0,0,2],
                            [0,1,3,1,0,0,0,0,0],
                            [0,0,2,0,2,0,0,0,0],
                            [0,0,0,2,2,2,0,0,0]])
    assert (board5.pos_update(board5.pos, 57).flatten() == pos5_up_b.flatten()).all(),"the updated pos should be \n%s instead of \n%s"%(pos5_up_b,board5.pos_update(board5.pos, 57).reshape((ROW,COL)))
    assert (board5.pos_update(board5.pos, 31).flatten() == pos5_up_w.flatten()).all(),"the updated pos should be \n%s instead of \n%s"%(pos5_up_w,board5.pos_update(board5.pos, 31).reshape((ROW,COL)))
    
    board7 = Board(pos7, PLAYER2, COMPUTE, 41)
    pos7_up_w  =  np.array([[0,0,0,2,2,2,0,0,0],
                            [0,0,0,1,2,2,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [2,2,0,0,1,0,0,0,2],
                            [2,2,0,2,2,1,2,2,2],
                            [2,0,0,0,1,0,0,0,2],
                            [0,0,0,0,0,0,0,0,0],
                            [0,2,0,0,2,0,0,0,0],
                            [0,0,0,2,2,2,0,0,0]])
    pos7_up_b  =  np.array([[0,0,0,1,1,1,0,0,0],
                            [0,0,0,1,1,2,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [1,2,0,0,1,0,0,0,1],
                            [1,1,0,2,1,1,2,1,1],
                            [1,0,0,0,1,0,0,0,1],
                            [0,0,0,0,0,0,0,0,0],
                            [0,2,0,0,1,0,0,0,0],
                            [0,0,0,0,1,0,0,0,0]])
    assert (board7.pos_update(board7.pos, 42).flatten() == pos7_up_w.flatten()).all(),"the updated pos should be \n%s instead of \n%s"%(pos7_up_w,board7.pos_update(board7.pos, 42).reshape((ROW,COL)))
    assert (board7.pos_update(board7.pos, 67).flatten() == pos7_up_b.flatten()).all(),"the updated pos should be \n%s instead of \n%s"%(pos7_up_b,board7.pos_update(board7.pos, 67).reshape((ROW,COL)))
    assert (board7.pos_update(board7.pos, 76).flatten() == pos7_up_b.flatten()).all(),"the updated pos should be \n%s instead of \n%s"%(pos7_up_b,board7.pos_update(board7.pos, 76).reshape((ROW,COL)))

    board9 = Board(pos9, PLAYER1, COMPUTE, 6)
    pos9_up_b  =  np.array([[0,0,0,1,1,1,3,1,0],
                            [1,0,0,0,1,2,0,2,0],
                            [0,0,0,0,0,0,0,0,0],
                            [1,0,0,0,0,0,0,0,1],
                            [1,0,0,0,1,0,0,1,1],
                            [0,0,0,0,2,0,0,0,1],
                            [0,0,0,0,2,0,0,0,0],
                            [0,0,0,0,1,0,0,0,0],
                            [0,0,1,1,1,1,0,0,0]])
    pos9_up_w  =  np.array([[0,0,0,2,2,2,3,1,0],
                            [1,0,0,0,2,2,0,2,0],
                            [0,0,0,0,0,0,0,0,0],
                            [2,0,0,0,0,0,0,0,2],
                            [2,2,0,0,2,0,0,2,2],
                            [2,0,0,0,2,0,0,0,2],
                            [0,0,0,0,2,0,0,0,0],
                            [0,0,0,0,2,0,0,0,0],
                            [0,0,1,2,2,2,0,0,0]])
    pos9_up_k  =  np.array([[0,0,0,3,3,3,3,1,0],
                            [1,0,0,0,3,2,0,2,0],
                            [0,0,0,0,0,0,0,0,0],
                            [3,0,0,0,0,0,0,0,3],
                            [3,3,0,0,3,0,0,3,3],
                            [3,0,0,0,2,0,0,0,3],
                            [0,0,0,0,2,0,0,0,0],
                            [0,0,0,0,3,0,0,0,0],
                            [0,0,1,3,3,3,0,0,0]])
    assert (board9.pos_update(board9.pos, 36).flatten() == pos9_up_b.flatten()).all(),"the updated pos should be \n%s instead of \n%s"%(pos9_up_b,board9.pos_update(board9.pos, 36).reshape((ROW,COL)))
    assert (board9.pos_update(board9.pos, 14).flatten() == pos9_up_w.flatten()).all(),"the updated pos should be \n%s instead of \n%s"%(pos9_up_w,board9.pos_update(board9.pos, 14).reshape((ROW,COL)))
    assert (board9.pos_update(board9.pos, 6).flatten() == pos9_up_k.flatten()).all(),"the updated pos should be \n%s instead of \n%s"%(pos9_up_k,board9.pos_update(board9.pos, 6).reshape((ROW,COL)))

def test_posupdatecapturing():
    board5 = Board(pos5, PLAYER1, COMPUTE, 47)
    pos5_up_b  =  np.array([[0,0,0,1,0,1,0,0,0],
                            [0,2,0,0,1,0,0,0,0],
                            [0,0,0,0,2,0,0,0,0],
                            [1,0,0,0,2,0,0,0,1],
                            [0,1,0,0,1,0,0,1,0],
                            [1,0,2,0,0,0,0,0,1],
                            [0,1,3,1,0,0,0,0,0],
                            [0,0,2,0,1,0,0,0,0],
                            [0,0,0,1,0,1,0,0,0]])
    pos5_up_w  =  np.array([[0,0,0,2,0,2,0,0,0],
                            [0,2,0,0,2,0,0,0,0],
                            [0,0,0,0,2,0,0,0,0],
                            [2,0,0,0,2,0,0,0,2],
                            [0,2,0,0,2,0,0,2,0],
                            [2,0,2,0,0,0,0,0,2],
                            [0,1,3,1,0,0,0,0,0],
                            [0,0,2,0,2,0,0,0,0],
                            [0,0,0,2,0,2,0,0,0]])
    assert (board5.pos_update_capturing(board5.pos, 57).flatten() == pos5_up_b.flatten()).all(),"the updated pos should be \n%s instead of \n%s"%(pos5_up_b,board5.pos_update_capturing(board5.pos, 57).reshape((ROW,COL)))
    assert (board5.pos_update_capturing(board5.pos, 31).flatten() == pos5_up_w.flatten()).all(),"the updated pos should be \n%s instead of \n%s"%(pos5_up_w,board5.pos_update_capturing(board5.pos, 31).reshape((ROW,COL)))
    
    board7 = Board(pos7, PLAYER2, COMPUTE, 41)
    pos7_up_w  =  np.array([[0,0,0,2,0,2,0,0,0],
                            [0,0,0,1,2,2,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [2,2,0,0,1,0,0,0,2],
                            [0,2,0,2,2,1,2,2,1],
                            [2,0,0,0,1,0,0,0,2],
                            [0,0,0,0,0,0,0,0,0],
                            [0,2,0,0,2,0,0,0,0],
                            [0,0,0,2,1,2,0,0,0]])
    pos7_up_b  =  np.array([[0,0,0,1,0,1,0,0,0],
                            [0,0,0,1,1,2,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [1,2,0,0,1,0,0,0,1],
                            [0,1,0,2,1,1,2,1,1],
                            [1,0,0,0,1,0,0,0,1],
                            [0,0,0,0,0,0,0,0,0],
                            [0,2,0,0,1,0,0,0,0],
                            [0,0,0,1,1,1,0,0,0]])
    assert (board7.pos_update_capturing(board7.pos, 42).flatten() == pos7_up_w.flatten()).all(),"the updated pos should be \n%s instead of \n%s"%(pos7_up_w,board7.pos_update_capturing(board7.pos, 42).reshape((ROW,COL)))
    assert (board7.pos_update_capturing(board7.pos, 67).flatten() == pos7_up_b.flatten()).all(),"the updated pos should be \n%s instead of \n%s"%(pos7_up_b,board7.pos_update_capturing(board7.pos, 67).reshape((ROW,COL)))
    assert (board7.pos_update_capturing(board7.pos, 76).flatten() == pos7_up_b.flatten()).all(),"the updated pos should be \n%s instead of \n%s"%(pos7_up_b,board7.pos_update_capturing(board7.pos, 76).reshape((ROW,COL)))
    
    board9 = Board(pos9, PLAYER1, COMPUTE, 6)
    pos9_up_b  =  np.array([[0,0,0,1,0,1,3,1,0],
                            [1,0,0,0,1,2,0,2,0],
                            [0,0,0,0,0,0,0,0,0],
                            [1,0,0,0,0,0,0,0,1],
                            [1,1,0,0,1,0,0,1,0],
                            [1,0,0,0,2,0,0,0,1],
                            [0,0,0,0,2,0,0,0,0],
                            [0,0,0,0,1,0,0,0,0],
                            [0,0,1,1,1,1,0,0,0]])#36
    pos9_up_w  =  np.array([[0,0,0,2,0,2,3,1,0],
                            [1,0,0,0,2,2,0,2,0],
                            [0,0,0,0,0,0,0,0,0],
                            [2,0,0,0,0,0,0,0,2],
                            [1,2,0,0,2,0,0,2,0],
                            [2,0,0,0,2,0,0,0,2],
                            [0,0,0,0,2,0,0,0,0],
                            [0,0,0,0,2,0,0,0,0],
                            [0,0,1,2,1,2,0,0,0]])#14
    pos9_up_k  =  np.array([[0,0,0,3,0,3,3,1,0],
                            [1,0,0,0,3,2,0,2,0],
                            [0,0,0,0,0,0,0,0,0],
                            [3,0,0,0,0,0,0,0,3],
                            [1,3,0,0,3,0,0,3,0],
                            [3,0,0,0,2,0,0,0,3],
                            [0,0,0,0,2,0,0,0,0],
                            [0,0,0,0,3,0,0,0,0],
                            [0,0,1,3,1,3,0,0,0]])#6
    assert (board9.pos_update_capturing(board9.pos, 36).flatten() == pos9_up_b.flatten()).all(),"the updated pos should be \n%s instead of \n%s"%(pos9_up_b,board9.pos_update_capturing(board9.pos, 36).reshape((ROW,COL)))
    assert (board9.pos_update_capturing(board9.pos, 14).flatten() == pos9_up_w.flatten()).all(),"the updated pos should be \n%s instead of \n%s"%(pos9_up_w,board9.pos_update_capturing(board9.pos, 14).reshape((ROW,COL)))
    assert (board9.pos_update_capturing(board9.pos, 6).flatten() == pos9_up_k.flatten()).all(),"the updated pos should be \n%s instead of \n%s"%(pos9_up_k,board9.pos_update_capturing(board9.pos, 6).reshape((ROW,COL)))


#boardP1 = Board(pos1, PLAYER1)
#test_posupdate()
#print(boardP1.capture_segments(boardP1, PLAYER1))
