from board import Board, PLAYER1, PLAYER2, DRAW

class GameHandler(object):
    def __init__(self, engine1, engine2, verbose=False):
        self.engine1 = engine1
        self.engine2 = engine2
        self.verbose = verbose
        
    def play(self):
        b = Board()
        
        players = {
            PLAYER1: self.engine1,
            PLAYER2: self.engine2
            }
        
        while b.end is None:
            if self.verbose:
                print(b)
                print('Player %s is thinking...' % {PLAYER1: 'B', PLAYER2: 'W'}[b.stm])
            player = players[b.stm]
            move = player.choose(b)
            b = b.move(move)
        
        if b.end == DRAW:
            winner = None
            looser = None
        else:
            winner = players[b.end]
            looser = players[PLAYER1 if b.end == PLAYER2 else PLAYER2]

        return b, winner, looser