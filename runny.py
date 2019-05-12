#da linea di comando leggere se BLACK o WHITE. 
#Istanziare poi l'engine associato e passarlo al gamehandler
#from sys import getsizeof
from vablut.engine.random import RandomEngine
from vablut.engine.human import HumanEngine
from vablut.engine.negamax import NegamaxEngine
from vablut.engine.alphabeta import AlphaBetaEngine
from vablut.engine.pvs import PVSEngine

from vablut.evaluate.moveorder import MoveOrder
from vablut.game import GameHandler
from vablut.gameJava import GameJavaHandler

from vablut.board import Board, PLAYER2
from vablut.evaluate.evaluate_glutton import Evaluator_glutton
from vablut.engine.greedy import WeightedGreedyEngine

def main():
    """
    ev_g = Evaluator_glutton([1])
    mo = MoveOrder('diff')

    p1 = AlphaBetaEngine(ev_g, mo, 3)
    p2 = PVSEngine(ev_g, mo, 3)
    gh = GameHandler(p1,p2,True)
    gh.play()"""



#    gh= GameJavaHandler(AlphaBetaEngine(Evaluator_glutton([1]), MoveOrder('diff'), 4), 'black', True)
#    gh.play()


    b = Board(draw_dic = {})
    b = b.move(('G5','G3'))
    #b6 = Board(pos6, PLAYER2, -1, 27)
    #print(b6.get_all_moves())
    print(b)
    ev_g = Evaluator_glutton([1])
    mo = MoveOrder('diff')
    
    #eng  = WeightedGreedyEngine(ev_g)
    #eng = AlphaBetaEngine(ev_g, mo, 3)
    eng = PVSEngine(ev_g, mo, 3)
    print(eng.choose(b))

if __name__ == '__main__':
    main()