# -*- coding: utf-8 -*-
import numpy as np
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
    board5_5 = Board(pos5, PLAYER1, COMPUTE, 56)
    assert board5_1.end is PLAYER1,"\n%s \n the end should be %s(PLAYER1)"%(board5_1,PLAYER1)
    assert board5_2.end is PLAYER1,"\n%s \n the end should be %s(PLAYER1)"%(board5_2,PLAYER1)
    assert board5_3.end is None,"\n%s \n the end should be None"%(board5_3)
    assert board5_4.end is None,"\n%s \n the end should be None"%(board5_4)
    board5_4again = Board(pos5, PLAYER1, COMPUTE, 65, draw_dic)
    assert board5_4again.end is DRAW,"\n%s \n the end should be DRAW"%(board5_4again)
    assert board5_5.end is None,"\n%s \n the end should be None"%(board5_5)
    
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

def test_coordinatesinttostring():
    assert Board.coordinates_int_to_string((19,25)) == ('B3','H3'),"the coordinate: %s should correspond to %s instead of %s"%('(19,25)',"('B3','H3')",Board.coordinates_int_to_string((19,25)))
    assert Board.coordinates_int_to_string((31,58)) == ('E4','E7'),"the coordinate: %s should correspond to %s instead of %s"%('(31,58)',"('E4','E7')",Board.coordinates_int_to_string((31,58)))
    assert Board.coordinates_int_to_string((78,15)) == ('G9','G2'),"the coordinate: %s should correspond to %s instead of %s"%('(78,15)',"('G9','G2')",Board.coordinates_int_to_string((78,15)))
    assert Board.coordinates_int_to_string((8,0))   == ('I1','A1'),"the coordinate: %s should correspond to %s instead of %s"%('(8,0)',"('I1','A1')",Board.coordinates_int_to_string((8,0)))
    assert Board.coordinates_int_to_string((54,13)) == ('A7','E2'),"the coordinate: %s should correspond to %s instead of %s"%('(54,13)',"('A7','E2')",Board.coordinates_int_to_string((54,13)))

def test_coordinatesstringtoint():
    assert Board.coordinates_string_to_int(('B3','H3')) == (19,25),"the coordinate: %s should correspond to %s instead of %s"%("('B3','H3')",'(19,25)',Board.coordinates_string_to_int(('B3','H3')))
    assert Board.coordinates_string_to_int(('E5','A9')) == (40,72),"the coordinate: %s should correspond to %s instead of %s"%("('E5','A9')",'(40,72)',Board.coordinates_string_to_int(('E5','A9')))
    assert Board.coordinates_string_to_int(('G2','G6')) == (15,51),"the coordinate: %s should correspond to %s instead of %s"%("('G2','G6')",'(15,51)',Board.coordinates_string_to_int(('G2','G6')))
    assert Board.coordinates_string_to_int(('E6','A6')) == (49,45),"the coordinate: %s should correspond to %s instead of %s"%("('E6','A6')",'(49,45)',Board.coordinates_string_to_int(('E6','A6')))
    assert Board.coordinates_string_to_int(('F9','I9')) == (77,80),"the coordinate: %s should correspond to %s instead of %s"%("('F9','I9')",'(77,80)',Board.coordinates_string_to_int(('F9','I9')))

def test_getallmoves():
    board1 = Board(pos1, PLAYER1, COMPUTE, 41)#B move
    b1_pm =  board1.get_all_moves()
    assert ('E1','F1') in b1_pm,"%s should be a possibile move for\n%s"%(('E1','F1'),board1)
    assert ('E1','E2') in b1_pm,"%s should be a possibile move for\n%s"%(('E1','E2'),board1)
    assert ('H5','I5') in b1_pm,"%s should be a possibile move for\n%s"%(('H5','I5'),board1)
    assert ('E4','B4') in b1_pm,"%s should be a possibile move for\n%s"%(('E4','B4'),board1)
    assert ('E4','E3') in b1_pm,"%s should be a possibile move for\n%s"%(('E4','E3'),board1)
    assert ('E4','H4') in b1_pm,"%s should be a possibile move for\n%s"%(('E4','H4'),board1)
    assert ('E4','F4') in b1_pm,"%s should be a possibile move for\n%s"%(('E4','F4'),board1)
    assert ('G8','G1') in b1_pm,"%s should be a possibile move for\n%s"%(('G8','G1'),board1)
    assert ('H8','H9') in b1_pm,"%s should be a possibile move for\n%s"%(('H8','H9'),board1)
    assert ('H8','H7') in b1_pm,"%s should be a possibile move for\n%s"%(('H8','H7'),board1)
    
    assert ('E4','E2') not in b1_pm,"%s should NOT be a possibile move for\n%s"%(('E4','E2'),board1)
    assert ('E4','A4') not in b1_pm,"%s should NOT be a possibile move for\n%s"%(('E4','A4'),board1)
    assert ('E4','I4') not in b1_pm,"%s should NOT be a possibile move for\n%s"%(('E4','I4'),board1)
    assert ('E4','E5') not in b1_pm,"%s should NOT be a possibile move for\n%s"%(('E4','E5'),board1)
    assert ('E4','E6') not in b1_pm,"%s should NOT be a possibile move for\n%s"%(('E4','E6'),board1)
    assert ('D1','F1') not in b1_pm,"%s should NOT be a possibile move for\n%s"%(('D1','F1'),board1)
    assert ('D1','D9') not in b1_pm,"%s should NOT be a possibile move for\n%s"%(('D1','D9'),board1)
    assert ('E1','E6') not in b1_pm,"%s should NOT be a possibile move for\n%s"%(('E1','E6'),board1)
    assert ('B5','E5') not in b1_pm,"%s should NOT be a possibile move for\n%s"%(('B5','E5'),board1)
    assert ('H5','D5') not in b1_pm,"%s should NOT be a possibile move for\n%s"%(('H5','D5'),board1)
    assert ('H5','H6') not in b1_pm,"%s should NOT be a possibile move for\n%s"%(('H5','H6'),board1)
    assert ('H5','H7') not in b1_pm,"%s should NOT be a possibile move for\n%s"%(('H5','H7'),board1)
    assert ('G8','E8') not in b1_pm,"%s should NOT be a possibile move for\n%s"%(('G8','E8'),board1)
    assert ('G8','C8') not in b1_pm,"%s should NOT be a possibile move for\n%s"%(('G8','C8'),board1)
    assert ('G8','I8') not in b1_pm,"%s should NOT be a possibile move for\n%s"%(('G8','I8'),board1)
    assert ('H8','F8') not in b1_pm,"%s should NOT be a possibile move for\n%s"%(('H8','F8'),board1)
    assert ('H8','H4') not in b1_pm,"%s should NOT be a possibile move for\n%s"%(('H8','H4'),board1)
    assert ('H8','H1') not in b1_pm,"%s should NOT be a possibile move for\n%s"%(('H8','H1'),board1)
    
    assert len(b1_pm) == 49,"the following board:\n%s\nshould have %s possible moves instead of %s per Player:%s"%(board1,49,len(b1_pm),board1.stm)

    board1 = Board(pos1, PLAYER2, COMPUTE, 69)#W move
    b1_pm =  board1.get_all_moves()
    assert ('C3','B3') in b1_pm,"%s should be a possibile move for\n%s"%(('C3','B3'),board1)
    assert ('C3','D3') in b1_pm,"%s should be a possibile move for\n%s"%(('C3','D3'),board1)
    assert ('C3','C1') in b1_pm,"%s should be a possibile move for\n%s"%(('C3','C1'),board1)
    assert ('C3','C8') in b1_pm,"%s should be a possibile move for\n%s"%(('C3','C8'),board1)
    assert ('C3','I3') in b1_pm,"%s should be a possibile move for\n%s"%(('C3','I3'),board1)
    assert ('F5','G5') in b1_pm,"%s should be a possibile move for\n%s"%(('F5','G5'),board1)
    assert ('F5','F2') in b1_pm,"%s should be a possibile move for\n%s"%(('F5','F2'),board1)
    assert ('F5','F3') in b1_pm,"%s should be a possibile move for\n%s"%(('F5','F3'),board1)
    assert ('F5','F6') in b1_pm,"%s should be a possibile move for\n%s"%(('F5','F6'),board1)
    assert ('B8','B6') in b1_pm,"%s should be a possibile move for\n%s"%(('B8','B6'),board1)
    assert ('B8','B9') in b1_pm,"%s should be a possibile move for\n%s"%(('B8','B9'),board1)
    assert ('B8','D8') in b1_pm,"%s should be a possibile move for\n%s"%(('B8','D8'),board1)
    assert ('H6','B6') in b1_pm,"%s should be a possibile move for\n%s"%(('H6','B6'),board1)
    assert ('H6','H7') in b1_pm,"%s should be a possibile move for\n%s"%(('H6','H7'),board1)
    assert ('I8','I7') in b1_pm,"%s should be a possibile move for\n%s"%(('I8','I7'),board1)
    assert ('I8','I9') in b1_pm,"%s should be a possibile move for\n%s"%(('I8','I9'),board1)
    assert ('E7','E6') in b1_pm,"%s should be a possibile move for\n%s"%(('E7','E6'),board1)
    assert ('E7','B7') in b1_pm,"%s should be a possibile move for\n%s"%(('E7','B7'),board1)
    assert ('E7','I7') in b1_pm,"%s should be a possibile move for\n%s"%(('E7','I7'),board1)
    
    assert ('B8','B4') not in b1_pm,"%s should NOT be a possibile move for\n%s"%(('B8','B4'),board1)
    assert ('B8','E8') not in b1_pm,"%s should NOT be a possibile move for\n%s"%(('B8','E8'),board1)
    assert ('B8','F8') not in b1_pm,"%s should NOT be a possibile move for\n%s"%(('B8','F8'),board1)
    assert ('F5','E5') not in b1_pm,"%s should NOT be a possibile move for\n%s"%(('B8','E5'),board1)
    assert ('F5','I5') not in b1_pm,"%s should NOT be a possibile move for\n%s"%(('B8','I5'),board1)
    assert ('F5','D5') not in b1_pm,"%s should NOT be a possibile move for\n%s"%(('B8','D5'),board1)
    assert ('H6','I6') not in b1_pm,"%s should NOT be a possibile move for\n%s"%(('H6','I6'),board1)
    assert ('H6','A6') not in b1_pm,"%s should NOT be a possibile move for\n%s"%(('H6','A6'),board1)
    assert ('H6','H3') not in b1_pm,"%s should NOT be a possibile move for\n%s"%(('H6','H3'),board1)
    assert ('H6','H9') not in b1_pm,"%s should NOT be a possibile move for\n%s"%(('H6','H9'),board1)
    assert ('I8','I6') not in b1_pm,"%s should NOT be a possibile move for\n%s"%(('I8','I6'),board1)
    assert ('I8','I2') not in b1_pm,"%s should NOT be a possibile move for\n%s"%(('I8','I2'),board1)
    assert ('I8','F8') not in b1_pm,"%s should NOT be a possibile move for\n%s"%(('I8','F8'),board1)
    assert ('I8','C8') not in b1_pm,"%s should NOT be a possibile move for\n%s"%(('I8','C8'),board1)
    assert ('I8','G8') not in b1_pm,"%s should NOT be a possibile move for\n%s"%(('I8','G8'),board1)
    assert ('E7','E5') not in b1_pm,"%s should NOT be a possibile move for\n%s"%(('E7','E5'),board1)
    assert ('E7','E8') not in b1_pm,"%s should NOT be a possibile move for\n%s"%(('E7','E8'),board1)
    assert ('E7','E9') not in b1_pm,"%s should NOT be a possibile move for\n%s"%(('E7','E9'),board1)
    
    assert len(b1_pm) == 47,"the following board:\n%s\nshould have %s possible moves instead of %s per Player:%s"%(board1,38,len(b1_pm),board1.stm)
    
def test_move_b3():
    b3 = Board(pos3, PLAYER2, COMPUTE, 65, {})#W move
    
    b3_1 = b3.move(('F8','F7'))
    b3_1_pos = np.array([[0,0,0,0,1,0,0,0,0],
                         [0,0,2,0,1,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0],
                         [1,0,0,0,2,1,0,0,0],
                         [1,1,0,0,0,3,1,0,0],
                         [0,0,0,0,2,0,0,0,0],
                         [0,0,0,0,0,2,0,0,0],
                         [0,0,1,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0]])
    assert (b3_1.pos.flatten() == b3_1_pos.flatten()).all()
    
    b3_2 = b3_1.move(('C8','C7'))
    b3_2_pos = np.array([[0,0,0,0,1,0,0,0,0],
                         [0,0,2,0,1,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0],
                         [1,0,0,0,2,1,0,0,0],
                         [1,1,0,0,0,3,1,0,0],
                         [0,0,0,0,2,0,0,0,0],
                         [0,0,1,0,0,2,0,0,0],
                         [0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0]])
    assert (b3_2.pos.flatten() == b3_2_pos.flatten()).all()
    
    b3_3 = b3_2.move(('E4','E3'))
    b3_3_pos = np.array([[0,0,0,0,1,0,0,0,0],
                         [0,0,2,0,1,0,0,0,0],
                         [0,0,0,0,2,0,0,0,0],
                         [1,0,0,0,0,1,0,0,0],
                         [1,1,0,0,0,3,1,0,0],
                         [0,0,0,0,2,0,0,0,0],
                         [0,0,1,0,0,2,0,0,0],
                         [0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0]])
    assert (b3_3.pos.flatten() == b3_3_pos.flatten()).all(),"\n%s\n%s"%(b3_3, b3_3_pos)
    
    b3_4 = b3_3.move(('G5','G7'))
    b3_4_pos = np.array([[0,0,0,0,1,0,0,0,0],
                         [0,0,2,0,1,0,0,0,0],
                         [0,0,0,0,2,0,0,0,0],
                         [1,0,0,0,0,1,0,0,0],
                         [1,1,0,0,0,3,0,0,0],
                         [0,0,0,0,2,0,0,0,0],
                         [0,0,1,0,0,2,1,0,0],
                         [0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0]])
    assert (b3_4.pos.flatten() == b3_4_pos.flatten()).all()
    
    b3_5 = b3_4.move(('E3','F3'))
    b3_5_pos = np.array([[0,0,0,0,1,0,0,0,0],
                         [0,0,2,0,1,0,0,0,0],
                         [0,0,0,0,0,2,0,0,0],
                         [1,0,0,0,0,0,0,0,0],
                         [1,1,0,0,0,3,0,0,0],
                         [0,0,0,0,2,0,0,0,0],
                         [0,0,1,0,0,2,1,0,0],
                         [0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0]])
    assert (b3_5.pos.flatten() == b3_5_pos.flatten()).all()
    
    b3_6 = b3_5.move(('C7','E7'))
    b3_6_pos = np.array([[0,0,0,0,1,0,0,0,0],
                         [0,0,2,0,1,0,0,0,0],
                         [0,0,0,0,0,2,0,0,0],
                         [1,0,0,0,0,0,0,0,0],
                         [1,1,0,0,0,3,0,0,0],
                         [0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,1,0,1,0,0],
                         [0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0]])
    assert (b3_6.pos.flatten() == b3_6_pos.flatten()).all()
    
    b3_7 = b3_6.move(('F5','F7'))
    b3_7_pos = np.array([[0,0,0,0,1,0,0,0,0],
                         [0,0,2,0,1,0,0,0,0],
                         [0,0,0,0,0,2,0,0,0],
                         [1,0,0,0,0,0,0,0,0],
                         [1,1,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,1,3,1,0,0],
                         [0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0]])
    assert (b3_7.pos.flatten() == b3_7_pos.flatten()).all()
    
    b3_8 = b3_7.move(('G7','H7'))
    b3_8_pos = np.array([[0,0,0,0,1,0,0,0,0],
                         [0,0,2,0,1,0,0,0,0],
                         [0,0,0,0,0,2,0,0,0],
                         [1,0,0,0,0,0,0,0,0],
                         [1,1,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,1,3,0,1,0],
                         [0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0]])
    assert (b3_8.pos.flatten() == b3_8_pos.flatten()).all()

    b3_9 = b3_8.move(('F7','G7'))
    b3_9_pos = np.array([[0,0,0,0,1,0,0,0,0],
                         [0,0,2,0,1,0,0,0,0],
                         [0,0,0,0,0,2,0,0,0],
                         [1,0,0,0,0,0,0,0,0],
                         [1,1,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,1,0,3,1,0],
                         [0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0]])                    
    assert (b3_9.pos.flatten() == b3_9_pos.flatten()).all()

    b3_10 = b3_9.move(('E7','F7'))
    b3_10_pos = np.array([[0,0,0,0,1,0,0,0,0],
                         [0,0,2,0,1,0,0,0,0],
                         [0,0,0,0,0,2,0,0,0],
                         [1,0,0,0,0,0,0,0,0],
                         [1,1,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,1,3,1,0],
                         [0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0]])           
    assert (b3_10.pos.flatten() == b3_10_pos.flatten()).all()
    assert b3_10.end == PLAYER1,"\n%s \n the end should be %s(PLAYER1)"%(b3_10,PLAYER1)

def test_move_b6():
    b6 = Board(pos6, PLAYER1, COMPUTE, 28, {})

    b6_ended = b6.move(('I4','C4'))
    b6_ended_pos = np.array([[0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,1,0,0,0,0],
                            [0,1,0,0,0,0,0,2,0],
                            [1,3,1,0,0,0,0,0,0],
                            [0,0,0,0,0,2,0,0,0],
                            [0,2,2,0,1,0,0,0,1],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,1,0,1,1,0,0,0]])
    assert (b6_ended.pos.flatten() == b6_ended_pos.flatten()).all()
    assert b6_ended.end == PLAYER1,"\n%s \n the end should be %s(PLAYER1)"%(b6_ended,PLAYER1)

def test_move():
    b = Board(draw_dic = {})

    b_1 = b.move(('F5','F8'))
    b_1_pos = np.array([[0,0,0,1,1,1,0,0,0],
                        [0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,2,0,0,0,0],
                        [1,0,0,0,2,0,0,0,1],
                        [1,1,2,2,3,0,2,1,1],
                        [1,0,0,0,2,0,0,0,1],
                        [0,0,0,0,2,0,0,0,0],
                        [0,0,0,0,1,2,0,0,0],
                        [0,0,0,1,1,1,0,0,0]])
    assert (b_1.pos.flatten() == b_1_pos.flatten()).all()

    b_2 = b_1.move(('F1','F5'))
    b_2_pos = np.array([[0,0,0,1,1,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,2,0,0,0,0],
                        [1,0,0,0,2,0,0,0,1],
                        [1,1,2,2,3,1,0,1,1],
                        [1,0,0,0,2,0,0,0,1],
                        [0,0,0,0,2,0,0,0,0],
                        [0,0,0,0,1,2,0,0,0],
                        [0,0,0,1,1,1,0,0,0]])
    assert (b_2.pos.flatten() == b_2_pos.flatten()).all()

    b_3 = b_2.move(('D5','D8'))
    b_3_pos = np.array([[0,0,0,1,1,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,2,0,0,0,0],
                        [1,0,0,0,2,0,0,0,1],
                        [1,1,2,0,3,1,0,1,1],
                        [1,0,0,0,2,0,0,0,1],
                        [0,0,0,0,2,0,0,0,0],
                        [0,0,0,2,0,2,0,0,0],
                        [0,0,0,1,1,1,0,0,0]])
    assert (b_3.pos.flatten() == b_3_pos.flatten()).all()

    b_4 = b_3.move(('D1','D7'))
    b_4_pos = np.array([[0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,2,0,0,0,0],
                        [1,0,0,0,2,0,0,0,1],
                        [1,1,2,0,3,1,0,1,1],
                        [1,0,0,0,2,0,0,0,1],
                        [0,0,0,1,2,0,0,0,0],
                        [0,0,0,0,0,2,0,0,0],
                        [0,0,0,1,1,1,0,0,0]])
    assert (b_4.pos.flatten() == b_4_pos.flatten()).all()

    b_5 = b_4.move(('E3','G3'))
    b_5_pos = np.array([[0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,2,0,0],
                        [1,0,0,0,2,0,0,0,1],
                        [1,1,2,0,3,1,0,1,1],
                        [1,0,0,0,2,0,0,0,1],
                        [0,0,0,1,2,0,0,0,0],
                        [0,0,0,0,0,2,0,0,0],
                        [0,0,0,1,1,1,0,0,0]])
    assert (b_5.pos.flatten() == b_5_pos.flatten()).all()

    b_6 = b_5.move(('F5','F3'))
    b_6_pos = np.array([[0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,1,2,0,0],
                        [1,0,0,0,2,0,0,0,1],
                        [1,1,2,0,3,0,0,1,1],
                        [1,0,0,0,2,0,0,0,1],
                        [0,0,0,1,2,0,0,0,0],
                        [0,0,0,0,0,2,0,0,0],
                        [0,0,0,1,1,1,0,0,0]])
    assert (b_6.pos.flatten() == b_6_pos.flatten()).all()

    b_7 = b_6.move(('E4','E3'))
    b_7_pos = np.array([[0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,2,0,2,0,0],
                        [1,0,0,0,0,0,0,0,1],
                        [1,1,2,0,3,0,0,1,1],
                        [1,0,0,0,2,0,0,0,1],
                        [0,0,0,1,2,0,0,0,0],
                        [0,0,0,0,0,2,0,0,0],
                        [0,0,0,1,1,1,0,0,0]])
    assert (b_7.pos.flatten() == b_7_pos.flatten()).all()

    b_8 = b_7.move(('A4','E4'))
    b_8_pos = np.array([[0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,2,0,0],
                        [0,0,0,0,1,0,0,0,1],
                        [1,1,2,0,3,0,0,1,1],
                        [1,0,0,0,2,0,0,0,1],
                        [0,0,0,1,2,0,0,0,0],
                        [0,0,0,0,0,2,0,0,0],
                        [0,0,0,1,1,1,0,0,0]])
    assert (b_8.pos.flatten() == b_8_pos.flatten()).all()

    b_9 = b_8.move(('E7','G7'))
    b_9_pos = np.array([[0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,2,0,0],
                        [0,0,0,0,1,0,0,0,1],
                        [1,1,2,0,3,0,0,1,1],
                        [1,0,0,0,2,0,0,0,1],
                        [0,0,0,1,0,0,2,0,0],
                        [0,0,0,0,0,2,0,0,0],
                        [0,0,0,1,1,1,0,0,0]])
    assert (b_9.pos.flatten() == b_9_pos.flatten()).all()
    
    b_10 = b_9.move(('H5','H7'))
    b_10_pos = np.array([[0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,2,0,0],
                        [0,0,0,0,1,0,0,0,1],
                        [1,1,2,0,3,0,0,0,1],
                        [1,0,0,0,2,0,0,0,1],
                        [0,0,0,1,0,0,2,1,0],
                        [0,0,0,0,0,2,0,0,0],
                        [0,0,0,1,1,1,0,0,0]])
    assert (b_10.pos.flatten() == b_10_pos.flatten()).all()

    b_11 = b_10.move(('E6','E7'))
    b_11_pos = np.array([[0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,2,0,0],
                        [0,0,0,0,1,0,0,0,1],
                        [1,1,2,0,3,0,0,0,1],
                        [1,0,0,0,0,0,0,0,1],
                        [0,0,0,1,2,0,2,1,0],
                        [0,0,0,0,0,2,0,0,0],
                        [0,0,0,1,1,1,0,0,0]])
    assert (b_11.pos.flatten() == b_11_pos.flatten()).all()

    b_12 = b_11.move(('I5','F5'))
    b_12_pos = np.array([[0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,2,0,0],
                        [0,0,0,0,1,0,0,0,1],
                        [1,1,2,0,3,1,0,0,0],
                        [1,0,0,0,0,0,0,0,1],
                        [0,0,0,1,2,0,2,1,0],
                        [0,0,0,0,0,2,0,0,0],
                        [0,0,0,1,1,1,0,0,0]])
    assert (b_12.pos.flatten() == b_12_pos.flatten()).all()

    b_13 = b_12.move(('G3','G6'))
    b_13_pos = np.array([[0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0,1],
                        [1,1,2,0,3,1,0,0,0],
                        [1,0,0,0,0,0,2,0,1],
                        [0,0,0,1,2,0,2,1,0],
                        [0,0,0,0,0,2,0,0,0],
                        [0,0,0,1,1,1,0,0,0]])
    assert (b_13.pos.flatten() == b_13_pos.flatten()).all()

    b_14 = b_13.move(('F5','F7'))
    b_14_pos = np.array([[0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0,1],
                        [1,1,2,0,3,0,0,0,0],
                        [1,0,0,0,0,0,2,0,1],
                        [0,0,0,1,0,1,0,1,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,1,1,1,0,0,0]])
    assert (b_14.pos.flatten() == b_14_pos.flatten()).all()

    b_15 = b_14.move(('E5','E7'))
    b_15_pos = np.array([[0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0,1],
                        [1,1,2,0,0,0,0,0,0],
                        [1,0,0,0,0,0,2,0,1],
                        [0,0,0,1,3,1,0,1,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,1,1,1,0,0,0]])
    assert (b_15.pos.flatten() == b_15_pos.flatten()).all()

    b_16 = b_15.move(('A6','E6'))
    b_16_pos = np.array([[0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,1,0,0,0,1],
                        [1,1,2,0,0,0,0,0,0],
                        [0,0,0,0,1,0,2,0,1],
                        [0,0,0,1,3,1,0,1,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,1,1,1,0,0,0]])
    assert (b_16.pos.flatten() == b_16_pos.flatten()).all()
    print(b_16)

def test_coordinate_transformation():
    m1 = ('H5','H2')
    assert Board.coordinates_transformation(m1,'VF')     == ('B5','B2'),"the move: %s with the %s transformation should be %s"%(m1,'VF',('B5','B2'))
    assert Board.coordinates_transformation(m1,'HF')     == ('H5','H8'),"the move: %s with the %s transformation should be %s"%(m1,'HF',('H5','H8'))
    assert Board.coordinates_transformation(m1,'LR')     == ('E2','B2'),"the move: %s with the %s transformation should be %s"%(m1,'LR',('E2','B2'))
    assert Board.coordinates_transformation(m1,'LRVF')   == ('E2','H2'),"the move: %s with the %s transformation should be %s"%(m1,'LRVF',('E2','H2'))
    assert Board.coordinates_transformation(m1,'LRHF')   == ('E8','B8'),"the move: %s with the %s transformation should be %s"%(m1,'LRHF',('E8','B8'))
    assert Board.coordinates_transformation(m1,'LRLR')   == ('B5','B8'),"the move: %s with the %s transformation should be %s"%(m1,'LRLR',('B5','B8'))
    assert Board.coordinates_transformation(m1,'LRLRLR') == ('E8','H8'),"the move: %s with the %s transformation should be %s"%(m1,'LRLRLR',('E8','H8'))

    m2 = ('E5','G5')
    assert Board.coordinates_transformation(m2,'VF')     == ('E5','C5'),"the move: %s with the %s transformation should be %s"%(m2,'VF',('E5','C5'))
    assert Board.coordinates_transformation(m2,'HF')     == ('E5','G5'),"the move: %s with the %s transformation should be %s"%(m2,'HF',('E5','G5'))
    assert Board.coordinates_transformation(m2,'LR')     == ('E5','E3'),"the move: %s with the %s transformation should be %s"%(m2,'LR',('E5','E3'))
    assert Board.coordinates_transformation(m2,'LRVF')   == ('E5','E3'),"the move: %s with the %s transformation should be %s"%(m2,'LRVF',('E5','E3'))
    assert Board.coordinates_transformation(m2,'LRHF')   == ('E5','E7'),"the move: %s with the %s transformation should be %s"%(m2,'LRHF',('E5','E7'))
    assert Board.coordinates_transformation(m2,'LRLR')   == ('E5','C5'),"the move: %s with the %s transformation should be %s"%(m2,'LRLR',('E5','C5'))
    assert Board.coordinates_transformation(m2,'LRLRLR') == ('E5','E7'),"the move: %s with the %s transformation should be %s"%(m2,'LRLRLR',('E5','E7'))

    m3 = ('A8','C8')
    assert Board.coordinates_transformation(m3,'VF')     == ('I8','G8'),"the move: %s with the %s transformation should be %s"%(m3,'VF',('I8','G8'))
    assert Board.coordinates_transformation(m3,'HF')     == ('A2','C2'),"the move: %s with the %s transformation should be %s"%(m3,'HF',('A2','C2'))
    assert Board.coordinates_transformation(m3,'LR')     == ('H9','H7'),"the move: %s with the %s transformation should be %s"%(m3,'LR',('H9','H7'))
    assert Board.coordinates_transformation(m3,'LRVF')   == ('B9','B7'),"the move: %s with the %s transformation should be %s"%(m3,'LRVF',('B9','B7'))
    assert Board.coordinates_transformation(m3,'LRHF')   == ('H1','H3'),"the move: %s with the %s transformation should be %s"%(m3,'LRHF',('H1','H3'))
    assert Board.coordinates_transformation(m3,'LRLR')   == ('I2','G2'),"the move: %s with the %s transformation should be %s"%(m3,'LRLR',('E5','C5'))
    assert Board.coordinates_transformation(m3,'LRLRLR') == ('B1','B3'),"the move: %s with the %s transformation should be %s"%(m3,'LRLRLR',('E5','E7'))

'''
blacks = np.array([[0,0,0,0,1,0,0,0,1],
                [0,0,0,0,1,0,0,0,0],
                [0,0,0,0,0,1,1,0,0],
                [0,0,0,1,0,0,0,0,0],
                [1,1,0,0,0,0,0,0,1],
                [0,0,0,0,0,0,0,0,0],
                [0,0,1,0,0,0,0,1,0],
                [0,0,0,0,1,0,1,0,0],
                [1,0,0,0,0,1,0,0,1]])
whites = np.array([[0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,1,0,0],
                [0,0,0,0,0,1,1,0,0],
                [0,0,0,1,1,0,0,0,0],
                [0,0,0,0,1,0,0,0,0],
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
pos = {PLAYER1:blacks, PLAYER2: (whites,king)}
b = Board(pos, PLAYER1)
print(b)
b.king_stats(b.pos)
'''