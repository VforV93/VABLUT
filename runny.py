#da linea di comando leggere se BLACK o WHITE. 
#Istanziare poi l'engine associato e passarlo al gamehandler
#from sys import getsizeof
import numpy as np
from vablut.board import PLAYER1, PLAYER2, DRAW
from vablut.engine.pvs import PVSCachedTimeEngine, PVSCachedTimeThreadsEngine

from vablut.evaluate.moveorder import MoveOrder
from vablut.game import GameHandler

from vablut.evaluate.evaluate_glutton import Evaluator_glutton
from vablut.evaluate.evaluate_glesc_ks import Evaluator_glesc_ks

def main():
    ev_g = Evaluator_glutton({1:[1], 2:[1]})
    ege_w = Evaluator_glesc_ks([{1:[50], 2:[2]}, None, {PLAYER1: np.array([0, 4, 1, -1, 1, 0, 1, 0], dtype=int), PLAYER2: np.array([0, -15, -1, 1, -1, 2, 0, 1], dtype=int)}])
    ege_b = Evaluator_glesc_ks([{1:[5], 2:[15]}, None, {PLAYER1: np.array([0, 4, 1, -1, 2, 0, 1, 0], dtype=int), PLAYER2: np.array([0, -15, -1, 1, -1, 2, 0, 1], dtype=int)}])
    mo = MoveOrder('diff')
    
    #pn = NegamaxEngine(ev_g, 1)
    p1 = PVSCachedTimeThreadsEngine(ege_b, mo, 3, 4, max_sec=60, verbose=True)   #NERO
    p2 = PVSCachedTimeThreadsEngine(ege_w, mo, 3, 4, max_sec=60, verbose=True)   #BIANCO
    gh = GameHandler(p1,p2,True)
    gh.play()

    
if __name__ == '__main__':
    main()
