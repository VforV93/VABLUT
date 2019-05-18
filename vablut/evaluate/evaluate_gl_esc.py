import numpy as np
from vablut.board import PLAYER1, PLAYER2, DRAW
from vablut.evaluate.base import Evaluator, INF
from vablut.evaluate.evaluate_glutton import Evaluator_glutton
from vablut.evaluate.evaluate_escapist import Evaluator_escapist

class Evaluator_gl_esc(Evaluator):
    def __init__(self, weights=[None,None]):
        super(Evaluator_gl_esc, self).__init__(weights)
        if weights[0]:
            self._eg = Evaluator_glutton(weights[0])
        else:
            self._eg = Evaluator_glutton()
            
        if weights[1]:
            self._ee = Evaluator_escapist(weights[1])
        else:
            self._ee = Evaluator_escapist()
            
    def evaluate(self, board):
        if board.end is not None:
            if board.end == DRAW:
                return 0
            elif board.end == board.stm:
                return INF
            else:
                return -INF

        score1 = self._eg.evaluate(board)
        score2 = self._ee.evaluate(board)
        
        score = score1 + score2
        return score
