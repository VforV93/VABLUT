import numpy as np
from sys import maxsize
from board import Board, PLAYER1, PLAYER2, DRAW
from sys import getsizeof

INF = maxsize

class Evaluator(object):
    def __init__(self, weights=[0, 0, 1, 4, 0]):
        self._weights = np.asarray(weights)
        
    def evaluate(self, board):
        scores = {PLAYER1: np.zeros(5, dtype=int),
                  PLAYER2: np.zeros(5, dtype=int)}
        
        if board.end is not None:
            if board.end == DRAW:
                return 0
            elif board.end == board.stm:
                return INF
            else:
                return -INF
        
        segments = Board.capture_segments(board, board.stm)
        filtered_segments = segments[segments.any(1)]
        
        for s in filtered_segments:
            c = np.bincount(s, minlength=3)
            print(c)