# coding=utf-8
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
    assert col*row-1 in _indices.flatten(),"0 not in _indices"

@pytest.mark.repeat(3)
def test_tables_capturesegments():
    assert capture_segments.size != 0,"capture_segments.size is equal to 0, so why are you using this module/package with a table board without captures?"
    r = randint(0,row-1)
    if _indices[:][r].size > 3:
        c = randint(0,row-3)
        assert _indices[:][r][c:c+3] in capture_segments,"%s not in capture_segments"%_indices[:][r][c:c+3]
        
    c = randint(0,col-1)
    if _indices.transpose()[:][c].size > 3:
        r = randint(0,col-3)
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
 

@pytest.mark.repeat(3)
def test_tables_possiblemovesegments():
    #Horizontal random check
    r = randint(0,row-1)
    lung = randint(2,col)
    start_el = randint(0,col-lung)
    check_move = _indices[r][start_el:start_el+lung]
    assert len(check_move)<=col
    i = check_move[0]
    ret = False
    for move in possible_move_segments[i]:
        if(len(check_move) == move.size and (check_move==move).all()):
            ret = True
    assert ret

    #Vertical random check
    r = randint(0,col-1)
    lung = randint(2,row)
    start_el = randint(0,row-lung)
    check_move = _indices.transpose()[r][start_el:start_el+lung]
    assert len(check_move)<=row
    i = check_move[0]
    ret = False
    for move in possible_move_segments[i]:
        if(len(check_move) == move.size and (check_move==move).all()):
            ret = True
    assert ret