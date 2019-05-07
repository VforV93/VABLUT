import random
import time
from vablut.engine.base import Engine

class RandomEngine(Engine):
    def __init__(self, delay=None):
        self.delay = delay
    
    def choose(self, board):
        moves = board.get_all_moves()
        if self.delay:
            time.sleep(self.delay)
        return random.choice(moves)

    def __str__(self):
        return 'Random'