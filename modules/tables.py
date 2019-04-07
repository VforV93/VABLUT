import numpy as np

#
# Segment tables
#
# Capture_Segments are trios of indices that represent three squares aligned and
# consecutive in the board(Vertical or Horizontal).
#
# rev_segments  is an index square -> group of trios-segments to ckeck for captures
# move_segments is an index square -> group of line-segments that pass by the square(the row and the column that pass from a i-j element of the board)
# possible_move_segments is an index square -> group of variable-segments used to get all possible moves
# cross_center_segments  is an index square -> group of 1 segments to check the cross capture of the king. 1st element is the middle elemente ofthe cross.
#

col = row = 9

capture_segments        = []
all_cross               = []
cross_center_segments   = [[] for x in range(col*row)]
rev_segments            = [[] for x in range(col*row)]
move_segments           = [[] for x in range(col*row)]
possible_move_segments  = [[] for x in range(col*row)]

throne_el = None
winning_el = []                                     #King goal
prohibited_black_el = []                            #corners and throne
prohibited_white_el = []                            #corners and throne
prohibited_king_el = []                             #throne if king leaves the position

_indices = np.arange(col*row).reshape((col, row))

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

def add_rev(line):
    for x in range(len(line)-2):
        seg = line[x:x+3]
        capture_segments.append(seg)
        rev_segments[seg[0]].append(seg)
        rev_segments[seg[-1]].append(seg)

def add_possible_move(line):
    for x in range(len(line)-1):
        for f in range(1,len(line[x:])):
            seg = line[x:x+f+1]
            possible_move_segments[seg[0]].append(seg)


def add_cross(*lines):
    if len(lines) == 2:
        for x in range(len(lines[0])):
            seg = lines[0][x:x+2]
            if x > 0:
                seg = np.append(seg, lines[0][x-1])
            seg = np.append(seg, lines[1][x])
            all_cross.append(seg)
            cross_center_segments[seg[0]].append(seg)
    if len(lines) == 3:
        for x in range(len(lines[1])):
            seg = lines[1][x:x+2]
            if x > 0:
                seg = np.append(seg, lines[1][x-1])
            seg = np.append(seg, [lines[0][x],lines[2][x]])
            all_cross.append(seg)
            cross_center_segments[seg[0]].append(seg)

def add_move(line):
    for n in line:
        move_segments[n].append(line)

for row in _indices:
    add_rev(row)
    add_move(row)
    add_possible_move(row)
    add_possible_move(row[::-1])
    
for col in _indices.transpose():
    add_rev(col)
    add_move(col)
    add_possible_move(col)
    add_possible_move(col[::-1])
 
#section to check the cross capture of the king-NOT USED IN THIS VERSION OF TABLUT
add_cross(_indices[0], _indices[1])
add_cross(_indices[-1], _indices[-2])
for t in range(len(_indices)-2):
    trios = _indices[t:t+3]
    add_cross(trios[0],trios[1],trios[2])

#the 4 corners of the board
winning_el.append(_indices[0][0])
winning_el.append(_indices[0][-1])
winning_el.append(_indices[-1][0])
winning_el.append(_indices[-1][-1])

#Black pieces can not take corners of throne position
prohibited_black_el = winning_el.copy()
prohibited_black_el.append(king.flatten().dot(_indices.flatten()))
#White like Black pieces
prohibited_white_el = prohibited_black_el.copy()

#King in this version of tablut can go wherever he wants
#prohibited_king_el.append(king.flatten().dot(_indices.flatten())) the king can move wherever he wants
throne_el = king.flatten().dot(_indices.flatten())

#np.asarray Trasformation
capture_segments = np.asarray(capture_segments)
all_cross = np.asarray(all_cross)
winning_el = np.asarray(winning_el)
prohibited_black_el = np.asarray(prohibited_black_el)
prohibited_white_el = np.asarray(prohibited_white_el)
prohibited_king_el = np.asarray(prohibited_king_el)
rev_segments = np.asarray([np.asarray(x) for x in rev_segments])
move_segments = np.asarray([np.asarray(x) for x in move_segments])
possible_move_segments = np.asarray([np.asarray(x) for x in possible_move_segments])
del col, row, trios, t