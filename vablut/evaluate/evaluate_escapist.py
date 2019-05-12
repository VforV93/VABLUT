import numpy as np
from vablut.board import Board, PLAYER1, PLAYER2, DRAW
from vablut.evaluate.base import Evaluator, INF

class Evaluator_escapist(Evaluator):
    def __init__(self, weights):
        super(Evaluator_escapist, self).__init__(weights)

    def evaluate(self, board):
        scores = {PLAYER1: np.zeros(len(self.weights), dtype=int),
                  PLAYER2: np.zeros(len(self.weights), dtype=int)}
        
        if board.end is not None:
            if board.end == DRAW:
                return 0
            elif board.end == board.stm:
                return INF
            else:
                return -INF

        stats, block_stats, free_esc_seg = board.escape_el_stats(board.pos)

        scores[PLAYER1] = np.concatenate(stats.flatten(), block_stats.flatten(), free_esc_seg)
        


        scores[PLAYER2][0] = n_pieces[1]