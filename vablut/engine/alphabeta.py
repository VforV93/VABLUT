from vablut.evaluate.base import INF
from vablut.engine.negamax import NegamaxEngine

class AlphaBetaEngine(NegamaxEngine):
    FORMAT_STAT = (
        'score: {score} [time: {time:0.3f}s, pv: {pv}]\n' +
        'nps: {nps}, nodes: {nodes}, betacuts: {betacuts}\n' +
        'leaves: {leaves}, draws: {draws}, mates: {mates}'
        )

    def __init__(self, evaluator, moveorder, maxdepth=2, verbose=True):
        super(AlphaBetaEngine, self).__init__(evaluator, maxdepth, verbose)
        self._moveorder = MoveOrder(ordering).order