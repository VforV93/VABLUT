import time
from multiprocessing import Queue, Pool, Manager

from vablut.evaluate.base import INF
from vablut.engine.alphabeta import AlphaBetaEngine
from vablut.engine.cached import CachedEngineMixin
from vablut.engine.base import Engine
from vablut.engine.negamax import NegamaxEngine

import numpy as np
from vablut.evaluate.moveorder import MoveOrder
from vablut.evaluate.evaluate_glesc_ks import Evaluator_glesc_ks
from vablut.evaluate.evaluate_glutton import Evaluator_glutton
from vablut.modules.cache import Cache, CacheSimm
from vablut.board import Board, PLAYER1, PLAYER2, DRAW
import copy
from multiprocessing import Process
MAXT = 4

class PVSEngine(AlphaBetaEngine):
    def search(self, board, depth, ply=1, alpha=-INF, beta=INF, hint=None):
        self.inc('nodes')

        if board.end is not None:
            return self.endscore(board, ply)

        if depth <= 0:
            self.inc('leaves')
            return [], self.evaluate(board)

        bestmove = []
        bestscore = alpha
        for i, m in enumerate(self.moveorder(board, board.get_all_moves(), hint, self._evaluator)):
            if i == 0 or depth == 1 or (beta-alpha) == 1:
                nextmoves, score = self.search(board.move(m), depth-1, ply+1, -beta, -bestscore)
            else:
                # pvs uses a zero window for all the other searches
                _, score = self.search(board.move(m), depth-1, ply+1, -bestscore-1, -bestscore)
                score = -score
                if score > bestscore:
                    nextmoves, score = self.search(board.move(m), depth-1, ply+1, -beta, -bestscore)
                else:
                    continue

            score = -score
            if score > bestscore:
                bestscore = score
                bestmove = [m] + nextmoves
            elif not bestmove:
                bestmove = [m] + nextmoves

            if self._verbose and self._counters['nodes']%1000==0:
                self.showstats(bestmove, bestscore)

            if bestscore >= beta:
                self.inc('betacuts')
                break

        return bestmove, bestscore

    def __str__(self):
        return 'PVS(%s)' % self._maxdepth

class PVSCachedEngine(CachedEngineMixin, PVSEngine):
    FORMAT_STAT = (
        'score: {score} [time: {time:0.3f}s, pv: {pv}]\n' +
        'nps: {nps}, nodes: {nodes}, betacuts: {betacuts}\n' +
        'hits: {hits}[{cache_len}], leaves: {leaves}, draws: {draws}, mates: {mates}'
        )

    def initcnt(self):
        super(PVSCachedEngine, self).initcnt()
        self._counters['hits'] = 0
        self._counters['cache_len'] = len(self._cache._cache)
        
    def __str__(self):
        return 'PVSCache(%s)' % self._maxdepth


class PVSCachedTimeEngine(PVSCachedEngine):
    def __init__(self, *args, max_sec=None, **kwargs):
        super(PVSCachedTimeEngine, self).__init__(*args, **kwargs)
        self._max_sec = max_sec

    def search(self, board, depth, ply=1, alpha=-INF, beta=INF, max_sec=None):
        if self._max_sec and (time.time() - self._startt) > (self._max_sec-1):
            return [], self.evaluate(board)

        return super(PVSCachedTimeEngine, self).search(board, depth, ply, alpha, beta)


def func_thread(*args, **kwargs):
    #print('dentroooooooooooo')
    q = args[5]
    c = Cache(initial = args[7])
    engine = PVSCachedTimeEngine(args[0], args[1], args[2], max_sec = args[3], verbose = args[4], cache = c)

    engine.initcnt()
    pv, score = engine.search(args[6], args[2], ply=2, alpha=args[8], beta=args[9])
    m = [args[10]]
    #if pv:
    #print('---')
    #print(pv)
    #print(m,score)
    m = m + pv
    #print(m)
    #print('---')
    q.put((m, score, c))
    #print('thread - TERMINO')

class PVSCachedTimeThreadsEngine(PVSEngine):
    def __init__(self, evaluator, moveorder, maxdepth, max_sec=None, verbose=True):
        super(PVSCachedTimeThreadsEngine, self).__init__(evaluator, moveorder, maxdepth, verbose)
        self._max_sec = max_sec
        
        self._moveorder = moveorder
        #self._res = queue.Queue()
        self._res = Queue()
        self._cache = Cache()


    def search(self, board, depth, ply=1, alpha=-INF, beta=INF, max_sec=None):
        self.inc('nodes')
        pool = []
        #q = Queue()
        q = Manager().Queue()
        count = 1
        if board.end is not None:
            return self.endscore(board, ply)

        if depth <= 0:
            self.inc('leaves')
            return [], self.evaluate(board)

        bestmove = []
        bestscore = alpha
        p = Pool(processes=4)
        for i, m in enumerate(self.moveorder(board, board.get_all_moves(), None, self._evaluator)):
            max_sec = self._max_sec - (time.time() - self._startt)
            #mythread =  threading.Thread(name= "Thread-{}".format(count), target=func_thread, args=(self._evaluator, self._moveorder, self._maxdepth-1, max_sec, self._verbose, q, board.move(m), self._cache._cache.copy()))  # ...Instantiate a thread and pass a unique ID to it
            #mythread =  Process(target=func_thread, args=(self._evaluator, self._moveorder, self._maxdepth-1, max_sec, self._verbose, q, board.move(m), self._cache._cache.copy(), -beta, -bestscore, m))  # ...Instantiate a thread and pass a unique ID to it
            res = p.apply_async(func_thread, (self._evaluator, self._moveorder, self._maxdepth-1, max_sec, self._verbose, q, board.move(m), self._cache._cache.copy(), -beta, -bestscore, m))  # ...Instantiate a thread and pass a unique ID to it
            #res.get()
            #mythread =  Process(target=func_thread, args=(self._evaluator, self._moveorder, self._maxdepth-1, max_sec, self._verbose, q, board.move(m), self._cache._cache.copy(), -INF, INF, m))  # ...Instantiate a thread and pass a unique ID to it
            #mythread.daemon=True
            #mythread.start()                                   # ...Start the thread, invoke the run method
            #pool.append(mythread)
            #mythread.join()
            count += 1
            #print('Lanciato Thread tot:%s'%count)

            if count >= MAXT:
                try:
                    ti = self._max_sec - (time.time() - self._startt)
                    #print('ti:%s'%str(ti))
                    entry = q.get(timeout=ti)
                    count -= 1
                    self._cache._cache.update(entry[2]._cache)
                    nextmoves = entry[0]
                    score = -entry[1]

                    #print(entry)
                    if score > bestscore:
                        bestscore = score
                        bestmove = nextmoves
                    elif not bestmove:
                        bestmove = nextmoves

                    #pool = [t for t in pool if t.isAlive()]
                except Exception as e: 
                    print(e)
                    #print("Ho finito il tempo")
                    return bestmove, bestscore

                if (time.time() - self._startt) > self._max_sec:
                    return bestmove, bestscore


        print('Nodo Radice: %s'%len(self._cache._cache))
        return bestmove, bestscore
'''
if __name__ == '__main__':
    b = Board(draw_dic = {})
    b = b.move(('E4','H4'))
    print(b)
    ev_g = Evaluator_glutton({1:[1], 2:[2]})
    ege_b = Evaluator_glesc_ks([{1:[5], 2:[50]}, None, {PLAYER1: np.array([0, 4, 1, 0, 1, 0, 1, 0], dtype=int), PLAYER2: np.array([0, -15, -1, 1, -1, 2, 0, 1], dtype=int)}])
    mo = MoveOrder('diff')
    #p1 = NegamaxEngine(ege_b, 2, True)
    #p1 = PVSCachedTimeEngine(ege_b, mo, 3, max_sec=60, verbose=True)   #NERO
    p1 = PVSCachedTimeThreadsEngine(ev_g, mo, 3, max_sec=60, verbose=True)   #NERO
    #p1 = PVSCachedTimeThreadsEngine(ege_b, mo, 4, max_sec=60)   #NERO
    print(p1.choose(b))
'''