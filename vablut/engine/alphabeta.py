from vablut.evaluate.base import INF
from vablut.engine.negamax import NegamaxEngine
from vablut.engine.cached import CachedEngineMixin

class AlphaBetaEngine(NegamaxEngine):
    FORMAT_STAT = (
        'score: {score} [time: {time:0.3f}s, pv: {pv}]\n' +
        'nps: {nps}, nodes: {nodes}, betacuts: {betacuts}\n' +
        'leaves: {leaves}, draws: {draws}, mates: {mates}'
        )

    def __init__(self, evaluator, moveorder, maxdepth=2, verbose=True):
        super(AlphaBetaEngine, self).__init__(evaluator, maxdepth, verbose)
        self.moveorder = moveorder.order

    def initcnt(self):
        super(AlphaBetaEngine, self).initcnt()
        self._counters['betacuts'] = 0

    def search(self, board, depth, ply=1, alpha=-INF, beta=INF, hint=None):
        self.inc('nodes')
        if board.end is not None:
            return self.endscore(board, ply)

        if depth <= 0:
            self.inc('leaves')
            return [], self.evaluate(board)

        bestmove = []
        bestscore = alpha
        for m in self.moveorder(board, board.get_all_moves(), hint, self._evaluator):
            nextmoves, score = self.search(board.move(m), depth-1, ply+1, -beta, -bestscore)
            score = -score
            if score > bestscore:
                bestscore = score
                bestmove = [m] + nextmoves
            elif not bestmove:
                bestmove = [m] + nextmoves

            if self._counters['nodes']%1000==0 and self._verbose:
                self.showstats(bestmove, bestscore)

            if bestscore >= beta:
                self.inc('betacuts')
                break

        return bestmove, bestscore

    def __str__(self):
            return 'AlphaBeta(%s)' % self._maxdepth

class ABCachedEngine(CachedEngineMixin, AlphaBetaEngine):
    FORMAT_STAT = (
        'score: {score} [time: {time:0.3f}s, pv: {pv}]\n' +
        'nps: {nps}, nodes: {nodes}, betacuts: {betacuts}\n' +
        'hits: {hits}[{cache_len}], leaves: {leaves}, draws: {draws}, mates: {mates}'
        )

    def initcnt(self):
        super(ABCachedEngine, self).initcnt()
        self._counters['hits'] = 0
        self._counters['cache_len'] = len(self._cache._cache)

    def __str__(self):
        return 'ABCache(%s)' % self._maxdepth
    