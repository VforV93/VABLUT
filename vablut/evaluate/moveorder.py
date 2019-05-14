import random
from functools import partial

from vablut.evaluate.base import Evaluator
from vablut.evaluate.evaldiff import evaldiff

class MoveOrder(object):
    def __init__(self, name):
        name = name.lower()
        dispatcher = {
            'seq':      self._order_seq,
            'random':   self._order_random,
            'diff':     self._order_diff,
            'eval':     self._order_eval
        }

        if name not in dispatcher:
            raise NotImplemented()

        self._order = dispatcher[name.lower()]

    def _order_seq(self, board, moves, evaluator = None):
        return moves

    def _order_random(self, board, moves, evaluator = None):
        random.shuffle(moves)
        return moves

    def _order_diff(self, board, moves, evaluator = None):
        if len(moves) <= 1:
            return moves

        return sorted(moves, key=partial(evaldiff, board), reverse=True)

    def _order_eval(self, board, moves, evaluator: Evaluator):
        if not hasattr(self, 'evaluate'):
            self.evaluate = evaluator.evaluate
        if len(moves) <= 1:
            return moves
        
        return sorted(moves, key=lambda m: -self.evaluate(board.move(m)), reverse=True)

    def order(self, board, moves, hint=None, ev = None):
        if hint is not None:
            yield hint

        for x in self._order(board, moves, ev):
            if x == hint:
                continue
            yield x