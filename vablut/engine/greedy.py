# -*- coding: utf-8 -*-
import numpy as np
from vablut.engine.base import Engine
from vablut.evaluate.base import INF
from vablut.evaluate.evaldiff import evaldiff

class GreedyEngine(Engine):
    def __init__(self, evaluator, verbose=True):
        self._verbose = verbose
        self._evaluator = evaluator
        self.evaluate = self._evaluator.evaluate

    def choose(self, board):
        moves = board.get_all_moves()
        m = moves[0]
        moves = moves[1:]

        bestmove = m
        bestscore = -self.evaluate(board.move(m))

        for m in moves:
            score = -self.evaluate(board.move(m))
            #print("move: %s score:%d"%(m,score))
            if score > bestscore:
                bestmove = m
                bestscore = score

        if self._verbose:
            print('Selected move %d with score %s' % (bestscore, bestmove))
        
        return bestmove

    def __str__(self):
        return 'Greedy'

class WeightedGreedyEngine(Engine):
    """Same as GreedyEngine but move randomly using scores as weights"""

    def __init__(self, evaluator, verbose=True):
        self._evaluator = evaluator
        self._verbose = verbose
        self.evaluate = self._evaluator.evaluate

    def choose(self, board):
        moves = board.get_all_moves()

        # nothing to weigh
        if len(moves) < 2:
            return moves[0]

        # winning move or threat blocking?
        scores = [evaldiff(board, m) for m in moves]
        if max(scores) >= INF - 1:
            return max(zip(scores, moves))[1]

        weights = np.array(scores, dtype=float) + 1

        if weights.sum() == 0:
            weights = np.array([1 / len(moves)] * len(moves), dtype=float)
        else:
            weights /= weights.sum()

        selected_move = np.random.choice(range(len(moves)), p=weights)
        selected_move = moves[selected_move]

        if self._verbose:
            selected_score = scores[list(moves).index(selected_move)]
            print('Selected move %s with score %s' % (str(selected_move),
                                                      selected_score))

        return selected_move

    def __str__(self):
        return 'Weighted Greedy'