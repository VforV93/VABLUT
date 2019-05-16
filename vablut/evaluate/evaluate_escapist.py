import numpy as np
from vablut.board import Board, PLAYER1, PLAYER2, DRAW
from vablut.evaluate.base import Evaluator, INF
from vablut.evaluate.evaluate_glutton import Evaluator_glutton

class Evaluator_escapist(Evaluator):
    def __init__(self, weights={1:np.asarray([2,1,-1,-1,-150,-100,0,1,12,-1,0,-2,0,0,0,-50,0,-20]),
                                2:np.asarray([-2,-1,1,0,150,150,0,-1,-5,2,0,-10,0,0,0,100,-5,0])}):
        super(Evaluator_escapist, self).__init__(weights)

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

        stats, block_stats, free_esc_seg = board.escape_el_stats(board.pos)

        scores[PLAYER1] = np.concatenate((stats.flatten(), block_stats.flatten(), free_esc_seg))
        scores[PLAYER2] = np.concatenate((stats.flatten(), block_stats.flatten(), free_esc_seg))
        
        s1 = (self.weights[PLAYER1] * scores[PLAYER1]).sum()
        s2 = (self.weights[PLAYER2] * scores[PLAYER2]).sum()
        
        score = s1 - s2
        if board.stm == PLAYER1:
            return score
        else:
            return -score

"""
weights={
    1:[ winning els occupied from B, 1 move to occupied for B, # winning els occupied from W, 
       1 move to occupied for W, # winning els occupied from K, 1 move to occupied for K, 
     B block B to w_e, B block W to w_e, B block K to w_e, 
     W block B to w_e, W block W to w_e, W block K to w_e, 
     K block B to w_e, K block W to w_e, K block K to w_e, 
     free muerte escape line, # muerte line with just B, # muerte line with just W]
    2:[]
    3:[]
}
"""