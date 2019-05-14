# coding=utf-8
import numpy as np
from vablut.board import Board
from vablut.evaluate import evaluate_escapist
from vablut.evaluate.evaluate_escapist import Evaluator_escapist
import pytest
from vablut.tests.test_board import pos1

b = Board(pos1, PLAYER1)
ev = Evaluator_escapist(weights={1:np.asarray([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]),
                                2:np.asarray([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])})
def test_evaluate():
    scores = ev.evaluate(b)
    print(scores)
    
test_evaluate()