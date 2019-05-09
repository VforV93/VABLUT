#da linea di comando leggere se BLACK o WHITE. 
#Istanziare poi l'engine associato e passarlo al gamehandler
#from sys import getsizeof
from vablut.engine.random import RandomEngine
from vablut.engine.human import HumanEngine
from vablut.game import GameHandler
from vablut.gameJava import GameJavaHandler

from vablut.board import Board
from vablut.evaluate.evaluate_glutton import Evaluator_glutton
from vablut.engine.greedy import WeightedGreedyEngine

def main():
# =============================================================================
#     p1 = RandomEngine(0.2)
#     p2 = HumanEngine('Phil')
#     gh = GameHandler(p1,p2,True)
#     gh.play()
# =============================================================================

#    gh= GameJavaHandler(RandomEngine(3), 'white', True)
#    gh.play()

    b    = Board(draw_dic = {})
    ev_g = Evaluator_glutton([1])
    eng  = WeightedGreedyEngine(ev_g)

    eng.choose(b)
    
if __name__ == '__main__':
    main()