# coding=utf-8
import numpy as np
#
# Segment tables
#
# Capture_Segments are trios of indices that represent three squares aligned and
# consecutive in the board(Vertical or Horizontal).
#
# rev_segments              is an index square -> group of trios-segments to ckeck for captures
# move_segments             is an index square -> group of line-segments that pass by the square(the row and the column that pass from a i-j element of the board)
# possible_move_segments    is an index square -> group of variable-segments used to get all possible moves
# cross_center_segments     is an index square -> group of 1 segments to check the cross capture of the king. 1st element is the middle elemente of the cross.
#

col = row = 9

capture_segments        = []
all_cross               = []
cross_center_segments   = [[] for x in range(col*row)]
rev_segments            = [[] for x in range(col*row)]
move_segments           = [[] for x in range(col*row)]
possible_move_segments  = [[] for x in range(col*row)]

_indices = np.arange(col*row).reshape((row, col))

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
            cross_center_segments[seg[0]] = seg
    if len(lines) == 3:
        for x in range(len(lines[1])):
            seg = lines[1][x:x+2]
            if x > 0:
                seg = np.append(seg, lines[1][x-1])
            seg = np.append(seg, [lines[0][x],lines[2][x]])
            all_cross.append(seg)
            cross_center_segments[seg[0]] = seg

def add_move(line):
    for n in line:
        move_segments[n].append(line)

for l_row in _indices:
    add_rev(l_row)
    add_move(l_row)
    add_possible_move(l_row)
    add_possible_move(l_row[::-1])
    
for l_col in _indices.transpose():
    add_rev(l_col) 
    add_move(l_col)
    add_possible_move(l_col)
    add_possible_move(l_col[::-1])
 
#section to check the cross capture of the king-NOT USED IN THIS VERSION OF TABLUT
add_cross(_indices[0], _indices[1])
add_cross(_indices[-1], _indices[-2])
for t in range(len(_indices)-2):
    trios = _indices[t:t+3]
    add_cross(trios[0],trios[1],trios[2])

#np.asarray Trasformation
capture_segments        = np.asarray(capture_segments)
all_cross               = np.asarray(all_cross)

cross_center_segments   = np.asarray([np.asarray(x) for x in cross_center_segments])
rev_segments            = np.asarray([np.asarray(x) for x in rev_segments])
move_segments           = np.asarray([np.asarray(x) for x in move_segments])
possible_move_segments  = np.asarray([np.asarray(x) for x in possible_move_segments])

del trios, t