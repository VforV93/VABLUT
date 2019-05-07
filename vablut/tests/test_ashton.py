# -*- coding: utf-8 -*-
from vablut.modules.ashton import *
from vablut.modules.tables import _indices
from random import randint

import pytest

def test_colrow():
    #ashton rules required 9x9 board
    assert col == 9,"Ashton rules: col must be 9 not %s"%col
    assert row == 9,"Ashton rules: row must be 9 not %s"%row

def test_camps():
    assert len(camps) == 4,"camps must contains 4 arrays not %s"%len(camps)
    for c in camps:
        assert len(c)       == 4,"every camp must contins 4 elements[%s]"%c
        assert len(set(c))  == 4,"camps elements must be different from each other"
        assert len(np.bincount(c)) < col*row,"each element in every camps must be an index < %s"%(col*row)

def test_campsegments():
    assert len(camp_segments) == 9*9,"camp_segments must be an index square with %s elements index"%(9*9)
    for c in camps:
        for ec in c:
            assert ec in camp_segments[ec],"camp:%s - element:%s must be in camp_segments[%s]:%s"%(c,ec,ec,camp_segments[ec])
            assert set(camp_segments[ec]) == set(c),"camp_segments[%s] should be %s instead of %s"%(ec,c,camp_segments[ec])
            
def test_throneel():
    assert throne_el == 40,"throne_el must be 40 not %s"%throne_el
            
def test_kingcapturesegments():
    corners  = {_indices[0][0]}
    corners.add(_indices[0][-1])
    corners.add(_indices[-1][0])
    corners.add(_indices[-1][-1])
    
    assert len(king_capture_segments) == 9*9,"king_capture_segments must be an index square with %s elements index"%(9*9)
    for c in corners:
        assert len(king_capture_segments[c]) == 0,"king_capture_segments[%s] must be empty because the King can not get to the corners"%c
    
    for i_kc in cross_center_segments[throne_el]:
        assert len(king_capture_segments[i_kc])         == 1,"the capture segments with king starteing index must be just one and not %s"%len(king_capture_segments[i_kc])
        assert len(set(king_capture_segments[i_kc][0])) == 5,"in the throne_el or neighborhood king_capture_segments[%s] must contains 5 elements"%i_kc
        assert set(cross_center_segments[i_kc])         == set(king_capture_segments[i_kc][0]),"king_capture_segments[%s] should be %s instead of %s"%(i_kc,cross_center_segments[i_kc],king_capture_segments[i_kc])

    horizontal_per = []
    horizontal_per.append(_indices[0][1:-1])
    horizontal_per.append(_indices[-1][1:-1])
    
    for hp in horizontal_per:
        for hpe in hp:
            assert (king_capture_segments[hpe] == np.asarray([hpe-1,hpe,hpe+1])).all(),"king_capture_segments[%s] should be %s instead of %s"%(hpe,np.asarray([hpe-1,hpe,hpe+1]),king_capture_segments[hpe])
    
    vertical_per = []
    vertical_per.append(_indices.transpose()[0][1:-1])
    vertical_per.append(_indices.transpose()[-1][1:-1])
    
    for vp in vertical_per:
        for vpe in vp:
            assert (king_capture_segments[vpe] == np.asarray([vpe-col,vpe,vpe+col])).all(),"king_capture_segments[%s] should be %s instead of %s"%(vpe,np.asarray([vpe-col,vpe,vpe+col]),king_capture_segments[vpe])
    
    for ins in _indices[1:-1].transpose()[1:-1].transpose().flatten():
        if ins not in cross_center_segments[throne_el]:
            assert [ins-1,ins,ins+1] in king_capture_segments[ins].tolist(),"king_capture_segments[%s]:%s should contain %s"%(ins,king_capture_segments[ins],np.asarray([ins-1,ins,ins+1]))
            assert [ins-col,ins,ins+col] in king_capture_segments[ins].tolist(),"king_capture_segments[%s]:%s should contain %s"%(ins,king_capture_segments[ins],np.asarray([ins-col,ins,ins+col]))
            
def test_winningel():
    per = []
    per.append(_indices[0][1:-1])
    per.append(_indices[-1][1:-1])
    per.append(_indices.transpose()[0][1:-1])
    per.append(_indices.transpose()[-1][1:-1])

    assert (len(winning_el) == ((col-2)*2 + (row-2)*2)-12),"winning_el must contain %s elements instead of %s"%(((col-2)*2 + (row-2)*2)-12,len(winning_el))
    for p in per:
        assert p[0] in winning_el,"%s should be in winning_el:%s"%(p[0],winning_el)
        assert p[1] in winning_el,"%s should be in winning_el:%s"%(p[1],winning_el)
        assert p[-1] in winning_el,"%s should be in winning_el:%s"%(p[-1],winning_el)
        assert p[-2] in winning_el,"%s should be in winning_el:%s"%(p[-2],winning_el)

def test_prohibitedsegments():
    #testing black prohibited elements
    for c in camps.flatten():
        assert c in prohibited_segments[PLAYER1][0],"the camp element %s should be prohibited for the Black Player moving FROM:%s"%(c,0)
        assert c in prohibited_segments[PLAYER1][2],"the camp element %s should be prohibited for the Black Player moving FROM:%s"%(c,2)
        assert c in prohibited_segments[PLAYER1][7],"the camp element %s should be prohibited for the Black Player moving FROM:%s"%(c,7)
        assert c in prohibited_segments[PLAYER1][11],"the camp element %s should be prohibited for the Black Player moving FROM:%s"%(c,11)
        assert c in prohibited_segments[PLAYER1][12],"the camp element %s should be prohibited for the Black Player moving FROM:%s"%(c,12)
        assert c in prohibited_segments[PLAYER1][16],"the camp element %s should be prohibited for the Black Player moving FROM:%s"%(c,16)
        assert c in prohibited_segments[PLAYER1][31],"the camp element %s should be prohibited for the Black Player moving FROM:%s"%(c,31)
        assert c in prohibited_segments[PLAYER1][39],"the camp element %s should be prohibited for the Black Player moving FROM:%s"%(c,39)
        assert c in prohibited_segments[PLAYER1][41],"the camp element %s should be prohibited for the Black Player moving FROM:%s"%(c,41)
        assert c in prohibited_segments[PLAYER1][49],"the camp element %s should be prohibited for the Black Player moving FROM:%s"%(c,49)
        assert c in prohibited_segments[PLAYER1][58],"the camp element %s should be prohibited for the Black Player moving FROM:%s"%(c,58)
        assert c in prohibited_segments[PLAYER1][68],"the camp element %s should be prohibited for the Black Player moving FROM:%s"%(c,68)
        assert c in prohibited_segments[PLAYER1][69],"the camp element %s should be prohibited for the Black Player moving FROM:%s"%(c,69)

    for i in _indices.flatten():
        for cs in camp_segments[i]:
            assert cs not in prohibited_segments[PLAYER1][i],"the camp element %s should not be prohibited for the Black Player moving FROM:%s"%(cs,i)

    #testing black prohibited elements

def test_capturingdic():
    for i,cd in capturing_dic.items():
        assert throne_el in cd,"throne element:%s should count always in capturing. It must be in %s"%(throne_el,cd)
        for c in camps:
            assert c[0] in cd,"camp element:%s should count always in capturing. It must be in %s"%(c[0],cd)
            assert c[2] in cd,"camp element:%s should count always in capturing. It must be in %s"%(c[2],cd)
            assert c[3] in cd,"camp element:%s should count always in capturing. It must be in %s"%(c[3],cd)


test_kingcapturesegments()