#da linea di comando leggere se BLACK o WHITE. 
#Istanziare poi l'engine associato e passarlo al gamehandler
#from sys import getsizeof
import numpy as np
from vablut.board import Board, PLAYER1, PLAYER2, DRAW
from vablut.engine.rand import RandomEngine
from vablut.engine.human import HumanEngine
from vablut.engine.negamax import NegamaxEngine
from vablut.engine.alphabeta import AlphaBetaEngine, ABCachedEngine, ABCachedTimeEngine
from vablut.engine.pvs import PVSEngine, PVSCachedEngine, PVSCachedTimeEngine, PVSCachedTimeThreadsEngine

from vablut.evaluate.moveorder import MoveOrder
from vablut.game import GameHandler
from vablut.gameJava import GameJavaHandler

from vablut.board import Board, PLAYER2
from vablut.evaluate.evaluate_glutton import Evaluator_glutton
from vablut.evaluate.evaluate_escapist import Evaluator_escapist
from vablut.evaluate.evaluate_gl_esc import Evaluator_gl_esc
from vablut.evaluate.evaluate_glesc_ks import Evaluator_glesc_ks

def main():
    ev_g = Evaluator_glutton({1:[1], 2:[1]})
    ege_w = Evaluator_glesc_ks([{1:[10], 2:[3]}, None, {PLAYER1: np.array([0, 4, 1, 0, 1, 0, 1, 0], dtype=int), PLAYER2: np.array([0, -15, -1, 1, -1, 2, 0, 1], dtype=int)}])
    ege_b = Evaluator_glesc_ks([{1:[2], 2:[10]}, None, {PLAYER1: np.array([0, 4, 1, 0, 1, 0, 1, 0], dtype=int), PLAYER2: np.array([0, -15, -1, 1, -1, 2, 0, 1], dtype=int)}])
    mo = MoveOrder('diff')
    
    #pn = NegamaxEngine(ev_g, 1)
    p1 = PVSCachedTimeThreadsEngine(ege_b, mo, 4, max_sec=60, verbose=True)   #NERO
    p2 = PVSCachedTimeThreadsEngine(ege_w, mo, 4, max_sec=60, verbose=True)   #BIANCO
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
    #for a,b in b.cachehashsimmkey():
    #    print(a,b)
    
    ev_g = Evaluator_glutton({1:[1],2:[3]})
    ee = Evaluator_escapist()
    ege = Evaluator_gl_esc([{1:[1], 2:[50]}, None]) #{1:[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 2:[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}
    
    mo = MoveOrder('diff')
    
    #eng  = WeightedGreedyEngine(ev_g)
    #eng = AlphaBetaEngine(ev_g, mo, 3)
    p1 = ABCachedTimeEngine(ege, mo, 3)
    print(b.move(p1.choose(b)))
    """
if __name__ == '__main__':
    main()
