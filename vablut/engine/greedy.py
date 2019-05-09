# -*- coding: utf-8 -*-
from vablut.engine.base import Engine

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