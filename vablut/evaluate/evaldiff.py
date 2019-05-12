# -*- coding: utf-8 -*-
import numpy as np
from vablut.board import Board, PLAYER1, PLAYER2, KING_VALUE
from vablut.evaluate.base import INF
from vablut.modules.tables import move_segments, _indices, cross_center_segments, possible_move_segments
from vablut.modules.ashton import winning_el

#TO TEST

def board_blocking(pos, move_seg, enemy):
    count = 0
    for seg in move_seg:
        if (np.isin(pos[seg], winning_el)).any():
            flag = False
            for el in pos[seg]:
                if not flag and el == -1:
                    flag = True
                elif flag and el == enemy:
                    count += 1
                    break
                elif el != 0:
                    break
            flag = False
            for el in pos[seg][::-1]:
                if not flag and el == -1:
                    flag = True
                elif flag and el == enemy:
                    count += 1
                    break
                elif el != 0:
                    break
    return count

"""
    [# vie di uscita che blocco - precedenti bloccate, # pezzi neri vicini, # pezzi bianchi vicini, # Re di fianco, # avversari attaccabili 1 mossa, # Re attaccabile 1 mossa, is moving king?]
"""
def evaldiff(board: Board, m, weights=None):
    #I use the default weights
    if weights is None:
        weights = {
            PLAYER1:np.array([ 10, 2, 4, 15, 5, 12, 0 ], dtype=int),
            PLAYER2:np.array([ 3, 4, 2, 10, 5, 1, 15], dtype=int)}
    else:
        weights = {board.stm: weights}

    score = np.asarray(np.zeros(7), dtype=int)

    if len(weights[board.stm]) != len(score):
        raise ValueError('weights must be contain %s elements like score'%len(score))

    #First element of score
    m     = board.coordinates_string_to_int(m)
    FROM  = m[0]
    TO    = m[1]
    #print('selected move: %s->%s'%(FROM,TO))
    original_pos   = board.pos.flatten()

    if board.stm == PLAYER2 and original_pos[FROM] == KING_VALUE:
        score[6] = 1

    pos_prima = board.pos_update_capturing(original_pos, FROM)
    pos_prima[pos_prima==KING_VALUE] = PLAYER2
    pos_prima[FROM] = -1
    #print(pos_prima.reshape((9,9)))
    blocco = board_blocking(pos_prima, move_segments[FROM], board.other)

    moved_pos = original_pos.copy()
    moved_pos[TO] = moved_pos[FROM]
    moved_pos[FROM] = 0

    pos_dopo = board.pos_update_capturing(moved_pos, TO)
    pos_dopo[TO] = -1
    blocco_dopo = board_blocking(pos_dopo, move_segments[TO], board.other)


    score[0] = blocco_dopo - blocco
    #print('blocco: %d'%blocco)
    #print('blocco_dopo: %d'%blocco_dopo)
    #print(moved_pos.reshape((9,9)))

    # pezzi neri vicini, # pezzi bianchi vicini, # Re di fianco
    c = np.bincount(moved_pos[cross_center_segments[TO]][1:], minlength=4)
    score[1], score[2], score[3] = c[1], c[2], c[3]
    
    
    pos_dopo = board.pos_update_capturing(moved_pos, TO)
    #print(pos_dopo.reshape((9,9)))

    # avversari attaccabili 1 mossa, # Re attaccabile 1 mossa
    for seg in possible_move_segments[TO]:
        line = pos_dopo[seg]
        if line[0] == board.stm and (line[-1] == board.other or line[-1] == KING_VALUE):
            c = np.bincount(line[1:], minlength=4)
            #print(line[1:])
            if c[1:].sum() == 1:
                if line[-1] == board.other:
                    score[4] += 1
                else:
                    score[5] += 1
                #print('OKKKKKKKKKKKK')
            #print(c[1:])

    return np.dot(weights[board.stm],score)
    #print(score)
    #print(np.dot(weights[board.stm],score))


"""
blacks = np.array([[0,0,0,0,1,0,0,0,0],
                   [0,0,0,0,1,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [1,0,0,0,0,1,0,0,0],
                   [1,1,0,0,0,0,1,0,0],
                   [0,0,0,0,0,1,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,1,0,0,0,0,0],
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
b = Board(pos3, PLAYER1, -1, 65)
#print(b)
evaldiff(b, ('D8','C8') )

n1 = np.array([ 3, 2, 4, 15, 5, 12, 0 ], dtype=int)
n2 = np.array([ 3, 2, 4, 15, 5, 12, 0], dtype=int)
print((n1 * n2).sum())
#print(np.dot(n1,n2))"""