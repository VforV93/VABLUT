# -*- coding: utf-8 -*-
# camp_segments is an index square -> group of board's elements that represents a camp
# king_capture_segments  is an index square -> group of 1 or more segments(3 or 5 elements) to check the king camptures
import numpy as np
from vablut.modules.tables import col, row, capture_segments, cross_center_segments, _indices


PLAYER1 = 1
PLAYER2 = 2
DRAW = 0
COMPUTE = -1
KING_VALUE = 3 #MUST be different from PLAYER1 and PLAYER2

camps                   = []
camp_segments           = [[] for x in range(col*row)]
king_capture_segments   = [[] for x in range(col*row)]

winning_el          = []    #King goal
prohibited_black_el = []    #throne
prohibited_white_el = []    #corners and throne
prohibited_king_el  = []    #throne if king leaves the position

capturing_dic       = {PLAYER1: [], PLAYER2: [], KING_VALUE: []} # dictionary used to "drug" the board position for the capture's purpose

#DEFAULT: Starting position of the game
blacks = np.array([[0,0,0,1,1,1,0,0,0],
                   [0,0,0,0,1,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [1,0,0,0,0,0,0,0,1],
                   [1,1,0,0,0,0,0,1,1],
                   [1,0,0,0,0,0,0,0,1],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,1,0,0,0,0],
                   [0,0,0,1,1,1,0,0,0]])

whites = np.array([[0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,1,0,0,0,0],
                   [0,0,0,0,1,0,0,0,0],
                   [0,0,1,1,0,1,1,0,0],
                   [0,0,0,0,1,0,0,0,0],
                   [0,0,0,0,1,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
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

throne_el = 40#king.flatten().dot(_indices.flatten())


def add_camp(line1, line2):
    seg = line1[int(len(line1)/2)-1:int(len(line1)/2)+2]
    seg = np.append(seg, line2[int(len(line2)/2)])
    camps.append(seg)
    for c in seg:
        camp_segments[c] = seg

add_camp(_indices[0], _indices[1])
add_camp(_indices.transpose()[-1], _indices.transpose()[-2])
add_camp(_indices[-1], _indices[-2])
add_camp(_indices.transpose()[0], _indices.transpose()[1])

# --- WINNING WHITE ELEMENTS ---
def add_winning_el(line):
    for x in line:
        if x not in winning_el and len(camp_segments[x]) == 0:
            winning_el.append(x)
#every border elements
add_winning_el(_indices[0][1:-1])
add_winning_el(_indices[-1][1:-1])
add_winning_el(_indices.transpose()[0][1:-1])
add_winning_el(_indices.transpose()[-1][1:-1])
# === === === === === === === === === === === === === === === === === === === === === === === === === === 
 
#Black pieces can not never take throne position. The black prohibited elements are dynamic with an evaluation that depends on FROM moving index.(checked in Board.py)
prohibited_black_el.append(throne_el)


#White prohibited elements. Whites can not go to the throne(even if it is empty) and camps
prohibited_white_el = list(prohibited_black_el)
for c in camps:
    for el in c:
        prohibited_white_el.append(el)


prohibited_king_el = list(prohibited_white_el)


# capturing_dic generation - the same for each kind of piece
cap_el = []
cap_el.append(throne_el)
for c in camps:
   cap_el.append(c[0])
   cap_el.append(c[2])
   cap_el.append(c[3])
capturing_dic[PLAYER1]    = np.asarray(cap_el[:])
capturing_dic[PLAYER2]    = np.asarray(cap_el[:])
capturing_dic[KING_VALUE] = np.asarray(cap_el[:])

# king_capture_segments
for tc in capture_segments:
    king_capture_segments[tc[1]].append(tc)
# different camptures rule in throne and adjacent elements
king_capture_segments[throne_el] = [cross_center_segments[throne_el]]
for adjacent in king_capture_segments[throne_el][0][1:]:
    king_capture_segments[adjacent] = [cross_center_segments[adjacent]]
# === === === === === === === === === === === === === === === === === === === === === === === === === === 

#np.asarray Trasformation
camps                   = np.asarray(camps)
#winning_el.remove(1)
#winning_el.append(40)
winning_el              = np.asarray(winning_el)

prohibited_black_el     = np.asarray(prohibited_black_el)
prohibited_white_el     = np.asarray(prohibited_white_el)
prohibited_king_el      = np.asarray(prohibited_king_el)


camp_segments           = np.asarray([np.asarray(x, dtype=int) for x in camp_segments])
king_capture_segments   = np.asarray([np.asarray(x, dtype=int) for x in king_capture_segments])
# prohibited_segments is a dictionary containing an index square for every kind of pieces(white, king and black) -> group of prohibited indices used to modify the pos game board to generate all moves or check camptures
prohibited_segments = {PLAYER1: [[] for x in range(col*row)], PLAYER2: [[] for x in range(col*row)], KING_VALUE: [[] for x in range(col*row)]}

mask = np.ones(col*row, dtype=bool)

w_mask = mask.copy()
w_mask[prohibited_white_el] = False
iw = _indices.flatten()*whites.flatten() #whites starting indices
iw=iw[iw>0]
w_mask[iw] = True
for pwe in _indices.flatten()[w_mask]:
    prohibited_segments[PLAYER2][pwe] = prohibited_white_el.copy()


k_mask = mask.copy()
k_mask[prohibited_king_el] = False
ik = _indices.flatten()*king.flatten() #king starting indices
ik=ik[ik>0]
k_mask[ik] = True
for pwe in _indices.flatten()[k_mask]:
    prohibited_segments[KING_VALUE][pwe] = prohibited_king_el.copy()
prohibited_segments[KING_VALUE][_indices.flatten().dot(king.flatten())] = prohibited_king_el.copy()

b_mask = mask.copy()
b_mask[prohibited_black_el] = False
ib = _indices.flatten()*blacks.flatten() #king starting indices
ib=ib[ib>0]
b_mask[ib] = True
for pwe in _indices.flatten()[b_mask]:
    prohibited_segments[PLAYER1][pwe] = np.concatenate((prohibited_black_el, camps.flatten()))#for each elements, default prohibited are all camps el...
for i,x in enumerate(camps):#...prohibited camp elements update
    for el in x:        
        prohibited_segments[PLAYER1][el] = np.concatenate((prohibited_black_el, camps[:i].flatten(), camps[i+1:].flatten()))
# === === === === === === === === === === === === === === === === === === === === === === === === === === 

#prohibited_segments[1][3][1] = 3
del c, el, i, pwe, tc, x, cap_el