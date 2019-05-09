# -*- coding: utf-8 -*-
import numpy as np
from vablut.board import Board

INF = 10000

class Evaluator(object):
    def __init__(self, weights):
        self._weights = np.asarray(weights)
        
    @property
    def weights(self):
        return self._weights
    
    def evaluate(self, board: Board):
        raise NotImplementedError