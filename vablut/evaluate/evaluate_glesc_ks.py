import numpy as np
from vablut.board import Board, PLAYER1, PLAYER2, DRAW
from vablut.evaluate.base import Evaluator, INF
from vablut.evaluate.evaluate_gl_esc import Evaluator_gl_esc

class Evaluator_glesc_ks(Evaluator_gl_esc):
    def __init__(self, weights=[None,None,{PLAYER2: np.array([0, 4, 1, 0, 1, 0, 1, 0], dtype=int), PLAYER1: np.array([0, -15, -1, 1, -1, 2, 0, 1], dtype=int)}]):
        super(Evaluator_glesc_ks, self).__init__(weights)

    def evaluate(self, board):
        if board.end is not None:
            if board.end == DRAW:
                return 0
            elif board.end == board.stm:
                return INF
            else:
                return -INF

        king_stats = board.king_stats(board.pos)

        s1 = (self.weights[2][PLAYER1] * king_stats).sum()
        s2 = (self.weights[2][PLAYER2] * king_stats).sum()

        score = s1 - s2
        if board.stm == PLAYER1:
            return super(Evaluator_glesc_ks, self).evaluate(board) + score
        else:
            return super(Evaluator_glesc_ks, self).evaluate(board) - score

'''
# [**escape distance**  , capturable            , # move for capturing, 
# free els around k     , # b pieces around k   , w pieces around k, 
# b 1 move to king      , w 1 move to king]
'''