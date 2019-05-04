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

#test_properties()
#print(board1)
