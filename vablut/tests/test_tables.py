# -*- coding: utf-8 -*-
from vablut.modules.tables import *
from vablut.modules.tables import _indices
from random import randint

import pytest
import numpy as np

def test_tables_indices():
    assert col>0,"impossible to work with col<=0"
    assert row>0,"impossible to work with row<=0"
    assert 0 in _indices.flatten(),"0 not in _indices"
    assert col in _indices.flatten(),"col not in _indices"
    assert row in _indices.flatten(),"row not in _indices"
    assert col*row-1 in _indices.flatten(),"%s(last element) not in _indices"%(col*row-1)
    assert col*row == len(_indices.flatten()),"_indices must contains col(%s)*row(%s) elements"%(col,row)
    
@pytest.mark.repeat(1)
def test_tables_capturesegments():
    assert capture_segments.size != 0,"capture_segments.size is equal to 0, so why are you using this module/package with a table board without captures?"
    r = randint(0,row-1)
    if _indices[:][r].size > 3:
        c = randint(0,row-3)
        assert _indices[:][r][c:c+3] in capture_segments,"%s not in capture_segments"%_indices[:][r][c:c+3]
        
    c = randint(0,col-1)
    if _indices.transpose()[:][c].size > 3:
        r = randint(0,row-3)
        assert _indices.transpose()[:][c][r:r+3] in capture_segments,"%s not in capture_segments"%_indices[:][c][r:r+3]
        
    assert len(capture_segments) == ((col-2)*row + (row-2)*col),"col:%s row:%s capture_segments does not have %s elements"%(col,row,(col-2)*row + (row-2)*col)
    

def test_tables_revsegments():
    assert len(rev_segments)==col*row,"rev_segments len is non equal to %s(col*row)"%(col*row)
    for i,v in enumerate(rev_segments):
        assert len(v)>1,"rev_segments[%s] empty"%i
    
def test_tables_movesegments():
    assert len(rev_segments)==col*row,"move_segments len is non equal to %s(col*row)"%(col*row)
    for i,v in enumerate(move_segments):
        assert len(v)==2,"move_segments[%s] does not have exatly 2 items"%i
        assert len(set(v[0]).intersection(set(v[1])))==1,'0 or 2 and more elements are in the %s-i of move_segments'%i


def test_tables_possiblemovesegments_init():
    assert len(possible_move_segments)==col*row,"possible_move_segments len is non equal to %s(col*row)"%(col*row)
    max_moves_pos = len(possible_move_segments[0])
    for i,v in enumerate(possible_move_segments):
        assert len(v)==max_moves_pos,"possible_move_segments[%s] does not have the same amount of moves than others(%s)"%(i,max_moves_pos)
        for m in v:
            assert len(m)>1,"1 move element not allowed. The move %s inside the possible_move_segments[%s](%s) has just 1 element."%(m,i,v)
 

@pytest.mark.repeat(1)
def test_tables_possiblemovesegments():
    #Horizontal random check
    r = randint(0,row-1)
    lung = randint(2,col)
    start_el = randint(0,col-lung)
    check_move = _indices[r][start_el:start_el+lung]
    assert len(check_move)<=col,"Horizontal move can not be longer than cols"
    i = check_move[0]
    ret = False
    for move in possible_move_segments[i]:
        if(len(check_move) == move.size and (check_move==move).all()):
            ret = True
    assert ret,"horizontal move %s is not in possible_move_segments[%s]"%(check_move, i)

    #Vertical random check
    r = randint(0,col-1)
    lung = randint(2,row)
    start_el = randint(0,row-lung)
    check_move = _indices.transpose()[r][start_el:start_el+lung]
    assert len(check_move)<=row,"Vertical move can not be longer than rows"
    i = check_move[0]
    ret = False
    for move in possible_move_segments[i]:
        if(len(check_move) == move.size and (check_move==move).all()):
            ret = True
    assert ret,"vertical move %s is not in possible_move_segments[%s]"%(check_move, i)
    
def test_tables_crosscentersegments():
    count = np.zeros(6,dtype=int)
    assert len(cross_center_segments) == col*row,"cross_center_segments must be an index square with %s elements index"%(col*row)
    for cross in cross_center_segments:
        assert cross.size>1,"Every cross must contain at least 2 elements"
        assert cross.size<=5,"Every cross must contain less or equal 5 elements"
        count[cross.size] += 1
        
    corners = 4
    per     = ((col-2)*2) + ((row-2)*2)
    oths    = col * row - per - corners
    assert count[3]==corners,"the 4 corners must contains 3 cross elements"
    assert count[4]==per,"the perimeters cross elements must be %s"%per
    assert count[5]==oths,"the inside elements must be %s"%oths

    left_corners    = {_indices[0][0]}
    right_corners   = {_indices[0][-1]}
    left_corners.add(_indices[-1][0])
    right_corners.add(_indices[-1][-1])
    
    uppper_per = set([])
    bottom_per = set([])
    left_per   = set([])
    right_per   = set([])
    uppper_per.update(_indices[0][1:-1])
    bottom_per.update(_indices[-1][1:-1])
    left_per.update(_indices.transpose()[0][1:-1])
    right_per.update(_indices.transpose()[-1][1:-1])
    
    oths = set(_indices.flatten())
    oths -= uppper_per
    oths -= bottom_per
    oths -= left_per
    oths -= right_per
    oths -= left_corners
    oths -= right_corners

    for lc in left_corners:
        assert lc == cross_center_segments[lc][0],"index %s must be also in the array contained in cross_center_segments[%s]"%(lc,lc)
        assert len(cross_center_segments[lc]) == 3
        assert (lc+1    in cross_center_segments[lc])
    
    for rc in right_corners:
        assert rc == cross_center_segments[rc][0],"index %s must be also in the array contained in cross_center_segments[%s]"%(rc,rc)
        assert len(cross_center_segments[rc]) == 3
        assert (rc-1    in cross_center_segments[rc])
        
    for up in uppper_per:
        assert up == cross_center_segments[up][0],"index %s must be also in the array contained in cross_center_segments[%s]"%(up,up)
        assert len(cross_center_segments[up]) == 4
        assert (up-1    in cross_center_segments[up])
        assert (up+1    in cross_center_segments[up])
        assert (up+col  in cross_center_segments[up])
        
    for bp in bottom_per:
        assert bp == cross_center_segments[bp][0],"index %s must be also in the array contained in cross_center_segments[%s]"%(up,up)
        assert len(cross_center_segments[bp]) == 4
        assert (bp-1    in cross_center_segments[bp])
        assert (bp+1    in cross_center_segments[bp])
        assert (bp-col  in cross_center_segments[bp])
        
    for lp in left_per:
        assert lp == cross_center_segments[lp][0],"index %s must be also in the array contained in cross_center_segments[%s]"%(up,up)
        assert len(cross_center_segments[lp]) == 4
        assert (lp-col  in cross_center_segments[lp])
        assert (lp+1    in cross_center_segments[lp])
        assert (lp+col  in cross_center_segments[lp])
        
    for rp in right_per:
        assert rp == cross_center_segments[rp][0],"index %s must be also in the array contained in cross_center_segments[%s]"%(up,up)
        assert len(cross_center_segments[rp]) == 4
        assert (rp-col  in cross_center_segments[rp])
        assert (rp-1    in cross_center_segments[rp])
        assert (rp+col  in cross_center_segments[rp])
        
    for ot in oths:
        assert ot == cross_center_segments[ot][0],"index %s must be also in the array contained in cross_center_segments[%s]"%(ot,ot)
        assert len(cross_center_segments[ot]) == 5
        assert (ot+1    in cross_center_segments[ot])
        assert (ot-1    in cross_center_segments[ot])
        assert (ot+col  in cross_center_segments[ot])
        assert (ot-col  in cross_center_segments[ot])