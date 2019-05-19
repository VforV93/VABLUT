
#da linea di comando leggere se BLACK o WHITE. 
#Istanziare poi l'engine associato e passarlo al gamehandler
#from vablut.game import GameHandler
import sys
import numpy as np
from vablut.board import PLAYER1, PLAYER2, DRAW

from vablut.evaluate.moveorder import MoveOrder
from vablut.evaluate.evaluate_glesc_ks import Evaluator_glesc_ks
from vablut.engine.pvs import PVSCachedTimeEngine, PVSCachedTimeThreadsEngine
from vablut.gameJava import GameJavaHandler

def main(): #python tabbrutt.py player_type [max_sec_mossa max_thread verbose] es: python tabbrutt.py black|white 60 4 False|True
    max_sec_mossa = 60
    max_thread    = 4
    player_type   = None
    ege           = None
    engine        = None
    mo            = MoveOrder('diff')
    verbose       = True

    try:
        if sys.argv[1]:
            player_type = str(sys.argv[1]).lower()
            if player_type not in ['black','white']:
                raise ValueError('!Wrong argv[player_type]! the first required argument[player_type] is different from black|white')
        else:
            raise ValueError('!Required argv[player_type] missing! run the script with at least one input argument black|white')

        if sys.argv[2]:
            max_sec_mossa = int(sys.argv[2])
        if sys.argv[3]:
            max_thread    = int(sys.argv[3])
        if sys.argv[4]:
            verbose       = bool(sys.argv[2])
    except Exception as e: 
                    print(e)

    if max_sec_mossa <= 0:
        raise ValueError('!Thinking seconds can not be <= 0!')
    if max_thread < 0:
        raise ValueError('!Thinking seconds can not be <= 0!')
    
    if player_type == 'black':
        ege = Evaluator_glesc_ks([{1:[2], 2:[10]}, None, {PLAYER1: np.array([0, 4, 1, 0, 1, 0, 1, 0], dtype=int), PLAYER2: np.array([0, -15, -1, 1, -1, 2, 0, 1], dtype=int)}])
    elif player_type == 'white':
        ege = Evaluator_glesc_ks([{1:[150], 2:[3]}, None, {PLAYER1: np.array([0, 4, 1, 0, 1, 0, 1, 0], dtype=int), PLAYER2: np.array([0, -15, -1, 1, -1, 2, 0, 1], dtype=int)}])
    else:
        raise ValueError('!IMPOSSIBLE!')

    if max_thread == 0:
        engine = PVSCachedTimeEngine(ege, mo, 3, max_sec=max_sec_mossa, verbose=verbose)
    else:
        engine = PVSCachedTimeThreadsEngine(ege, mo, 3, max_thread, max_sec=max_sec_mossa, verbose=verbose)

    gh  = GameJavaHandler(engine, player_type, verbose)
    gh.play()
    
if __name__ == '__main__':
    main()
