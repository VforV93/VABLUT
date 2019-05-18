import time
from multiprocessing import Queue, Pool, Manager, Process

from vablut.evaluate.base import INF
from vablut.engine.alphabeta import AlphaBetaEngine
from vablut.engine.cached import CachedEngineMixin
from vablut.engine.base import Engine
from vablut.engine.negamax import NegamaxEngine

from vablut.modules.cache import Cache, CacheSimm

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
    q = args[5]
    c = CacheSimm(initial = args[7])
    engine = PVSCachedTimeEngine(args[0], args[1], args[2], max_sec = args[3], verbose = args[4], cache = c)

    engine.initcnt()
    pv, score = engine.search(args[6], args[2], ply=2, alpha=args[8], beta=args[9])
    m = [args[10]]
    m = m + pv
    q.put((m, score, c))

class PVSCachedTimeThreadsEngine(PVSEngine):
    def __init__(self, evaluator, moveorder, maxdepth, max_sec=None, verbose=True):
        super(PVSCachedTimeThreadsEngine, self).__init__(evaluator, moveorder, maxdepth, verbose)
        self._max_sec = max_sec-1
        
        self._moveorder = moveorder
        self._res = Queue()
        self._cache = CacheSimm()
        self._pool = Pool(processes=MAXT)


    def search(self, board, depth, ply=1, alpha=-INF, beta=INF, max_sec=None):
        q = Manager().Queue()
        count = 0
        #tot = 0
        if board.end is not None:
            return self.endscore(board, ply)

        if depth <= 0:
            return [], self.evaluate(board)

        bestmove = []
        bestscore = alpha

        for i, m in enumerate(self.moveorder(board, board.get_all_moves(), None, self._evaluator)):
            max_sec = self._max_sec - (time.time() - self._startt)
            res = self._pool.apply_async(func_thread, (self._evaluator, self._moveorder, self._maxdepth-1, max_sec, False, q, board.move(m), self._cache._cache.copy(), -beta, -bestscore, m))  # ...Instantiate a thread and pass a unique ID to it
            count += 1
            #tot += 1

            if i == 0:
                bestmove = [m]
                
            if count >= MAXT:
                try:
                    ti = self._max_sec - (time.time() - self._startt)
                    entry = q.get(timeout=ti)
                    count -= 1
                    self._cache._cache.update(entry[2]._cache)
                    nextmoves = entry[0]
                    score = -entry[1]
                    if score > bestscore:
                        bestscore = score
                        bestmove = nextmoves
                    elif not bestmove:
                        bestmove = nextmoves
                except Exception as e: 
                    print(e)
                    print('**HO FINITO IL TEMPO** mosse [%s/%s]'%(i+1,len(board.get_all_moves())))
                    return bestmove, bestscore

                if (time.time() - self._startt) > self._max_sec:
                    print('mosse [%s/%s]'%(i+1,len(board.get_all_moves())))
                    return bestmove, bestscore


        print('**FINITE LE MOSSE** mosse [%s/%s]'%(i+1,len(board.get_all_moves())))
        return bestmove, bestscore