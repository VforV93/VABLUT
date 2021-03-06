import numpy as np
from vablut.board import Board, PLAYER1, PLAYER2, DRAW
from vablut.evaluate.base import Evaluator, INF

class Evaluator_glutton(Evaluator):
    def __init__(self, weights={PLAYER1:[1],PLAYER2:[3]}):
        super(Evaluator_glutton, self).__init__(weights)
        
    def evaluate(self, board):
        scores = {PLAYER1: np.zeros(len(self.weights[PLAYER1]), dtype=int),
                  PLAYER2: np.zeros(len(self.weights[PLAYER2]), dtype=int)}
        
        if board.end is not None:
            if board.end == DRAW:
                return 0
            elif board.end == board.stm:
                return INF
            else:
                return -INF
        
        n_pieces = board.number_pieces(board.pos)

        scores[PLAYER1][0] = n_pieces[0]
        scores[PLAYER2][0] = n_pieces[1]
            
        s1 = (self.weights[PLAYER1] * scores[PLAYER1]).sum()
        s2 = (self.weights[PLAYER2] * scores[PLAYER2]).sum()
        #print(s1,s2)
        score = s1 - s2
        if board.stm == PLAYER1:
            return score
        else:
            return -score