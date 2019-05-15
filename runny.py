#da linea di comando leggere se BLACK o WHITE. 
#Istanziare poi l'engine associato e passarlo al gamehandler
#from sys import getsizeof
import numpy as np
from vablut.board import Board, PLAYER1, PLAYER2, DRAW
from vablut.engine.random import RandomEngine
from vablut.engine.human import HumanEngine
from vablut.engine.negamax import NegamaxEngine
from vablut.engine.alphabeta import AlphaBetaEngine, ABCachedEngine, ABCachedTimeEngine
from vablut.engine.pvs import PVSEngine, PVSCachedEngine

from vablut.evaluate.moveorder import MoveOrder
from vablut.game import GameHandler
from vablut.gameJava import GameJavaHandler

from vablut.board import Board, PLAYER2
from vablut.evaluate.evaluate_glutton import Evaluator_glutton
from vablut.evaluate.evaluate_escapist import Evaluator_escapist
from vablut.evaluate.evaluate_gl_esc import Evaluator_gl_esc
from vablut.engine.greedy import WeightedGreedyEngine

def main():
    """
    ev_g = Evaluator_glutton({1:[30], 2:[1]})
    ee = Evaluator_escapist()
    ege = Evaluator_gl_esc([{1:[1], 2:[50]}, None])
    mo = MoveOrder('diff')
    
    p1 = ABCachedTimeEngine(ege, mo, 3, max_sec=10)   #NERO
    p2 = PVSCachedEngine(ev_g, mo, 3)     #BIANCO
    gh = GameHandler(p1,p2,True)
    gh.play()

    #gh= GameJavaHandler(AlphaBetaEngine(Evaluator_glutton([1]), MoveOrder('diff'), 4), 'black', True)
    #gh.play()
    """
    '''
    blacks = np.array([[0,0,0,0,1,0,0,0,1],
                    [0,0,0,0,1,0,0,0,0],
                    [0,0,0,0,0,1,1,0,0],
                    [0,0,0,1,0,0,0,0,0],
                    [1,1,0,0,0,0,0,0,1],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,1,0,0,0,0,1,0],
                    [0,0,0,0,1,0,1,0,0],
                    [1,0,0,0,0,1,0,0,1]])
    whites = np.array([[0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,1,0,0],
                    [0,0,0,0,0,1,1,0,0],
                    [0,0,0,1,1,0,0,0,0],
                    [0,0,0,0,1,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0]])
    king  =  np.array([[0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,1,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0]])
    pos = {PLAYER1:blacks, PLAYER2: (whites,king)}
    b = Board(pos, PLAYER1)
    '''
    b = Board(draw_dic = {})
    b = b.move(('E4','H4'))
    print(b)
    
    ev_g = Evaluator_glutton({1:[1],2:[3]})
    ee = Evaluator_escapist()
    ege = Evaluator_gl_esc([{1:[1], 2:[50]}, None]) #{1:[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 2:[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}
    
    mo = MoveOrder('diff')
    
    #eng  = WeightedGreedyEngine(ev_g)
    #eng = AlphaBetaEngine(ev_g, mo, 3)
    p1 = ABCachedTimeEngine(ege, mo, 3, max_sec=10)
    print(b.move(p1.choose(b)))
    
if __name__ == '__main__':
    main()