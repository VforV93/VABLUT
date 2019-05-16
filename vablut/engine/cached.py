# -*- coding: utf-8 -*-
import time
from vablut.evaluate.base import INF
from vablut.modules.cache import Cache, CacheSimm

class CachedEngineMixin(object):
    def __init__(self, *args, **kwargs):
        super(CachedEngineMixin, self).__init__(*args, **kwargs)
        self._cache = CacheSimm()

    def showstats(self, pv, score):
        t = time.time() - self._startt
        if t:
            nps = (self._counters['nodes'] + self._counters['hits'])/ t
        else:
            nps = 0

        pv = ', '.join(str(x) for x in pv)

        ctx = self._counters.copy()
        ctx['pv'] = pv
        ctx['nps'] = nps
        ctx['score'] = score
        ctx['time'] = t
        
        print(self.FORMAT_STAT.format(**ctx))
        
    def search(self, board, depth, ply=1, alpha=-INF, beta=INF):
        hit, move, score = self._cache.lookup(board, depth, ply, alpha, beta)
        if hit:
            self.inc('hits')
            if move is not None:
                move = [move]
            else:
                move = []
            return move, score
        else:
            move, score = super(CachedEngineMixin, self).search(board, depth, ply, alpha, beta, hint=move)
            self._cache.put(board, move, depth, ply, score, alpha, beta)
            self._counters['cache_len'] = len(self._cache._cache)
            return move, score


class CachedEngineMixinC4(object):
    def __init__(self, *args, **kwargs):
        super(CachedEngineMixin, self).__init__(*args, **kwargs)
        self._cache = Cache()
        
    def search(self, board, depth, ply=1, alpha=-INF, beta=INF):
        hit, move, score = self._cache.lookup(board, depth, ply, alpha, beta)
        if hit:
            self.inc('hits')
            if move is not None:
                move = [move]
            else:
                move = []
            return move, score
        else:
            move, score = super(CachedEngineMixin, self).search(board, depth, ply, alpha, beta, hint=move)
            self._cache.put(board, move, depth, ply, score, alpha, beta)
            return move, score