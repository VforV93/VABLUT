#rules followed http://tafl.cyningstan.com/page/171/rules-for-brandub
import numpy as np
from modules.tables import _indices, move_segments, rev_segments, possible_move_segments
from modules.ashton import PLAYER1, PLAYER2, DRAW, COMPUTE, KING_VALUE, blacks, whites, king, throne_el, king_capture_segments, winning_el, prohibited_black_el, prohibited_white_el, prohibited_king_el, prohibited_segments
from random import shuffle

COL = int(len(_indices[0]))
ROW = int(len(_indices.transpose()[0]))

class WrongMoveError(Exception):
    pass

class Board(object):
    def __init__(self, pos=None, stm=PLAYER2, end=COMPUTE, cols=9, rows=9):
        if pos is None:
            pos = {PLAYER1:blacks, PLAYER2: (whites,king)}
        self._pos = pos
        self._stm = stm
        if end == COMPUTE:
            self._end = self._check_end(self.pos)
        else:
            self._end = end

    @property
    def end(self):
        return self._end
    
    @property
    def stm(self):
        return self._stm
    
    @property
    def other(self):
        return PLAYER1 if self._stm != PLAYER1 else PLAYER2
    
    @property
    def pos(self):
        return (PLAYER1*self._pos[PLAYER1]+PLAYER2*self._pos[PLAYER2][0]+KING_VALUE*self._pos[PLAYER2][1])
    
    def _check_end(self, pos, last_move=None):
        if KING_VALUE in self.win_segments(pos):
            return PLAYER2
# =============================================================================
#         
#         if last_move is not None:
#             if pos.flatten()[pos==KING_VALUE].sum() == 0:#if in the previous black movement the king is been captured
#                 return PLAYER1
#             
#             pos = pos.flatten()
#             pos[winning_el] = PLAYER1
#             if not pos[throne_el] == KING_VALUE:
#                 pos[throne_el] = PLAYER1
#                 
#             for seg in self.capture_segments(pos, last_move):
#                 c = np.bincount(seg)
#                 if not seg[1] == KING_VALUE:
#                     continue
#                 elif c[PLAYER1] == len(seg)-1:
#                     return PLAYER1
# =============================================================================
# =============================================================================
#         TO DO:check mosse finite ===> pareggio
#         if pos.all():
#             return DRAW
#         else:
# =============================================================================
        return None
    
    @classmethod
    def win_segments(cls, pos):
        if isinstance(pos, Board):
            return cls.segments(pos.pos)
        else:
            pos = pos.flatten()
            return pos[winning_el]
    
    def __str__(self):
        disc = {
            0: '_',
            1: 'B',
            2: 'W',
            3: 'K'
            }
        
        s = []
        for row in self.pos:
            s.append(' | '.join(disc[x] for x in row))
        s.append(' | '.join('.'*COL))
        s.append(' | '.join(map(str, 'ABCDEFGHI')))
        s = ['| ' + x + ' |' for x in s]
        s = [i + ' ' + x for i, x in zip('123456789  ', s)]
        s = '\n'.join(s)
        
        if self.end is DRAW:
            s += '\n<<< Game over: draw' % [self.end]
        elif self.end is not None:
            s += '\n<<< Game over: %s win' % disc[self.end]
        else:
            s += '\n<<< Move to %s' % disc[self.stm]
        
        return s
    
    #m must be a tuple (FROM, TO). es (D1, F1)
    def move(self, m):
        if not isinstance(m, tuple):
            raise ValueError(m)
        
        check_pos = self.pos
        col = len(check_pos[0])
        row = len(check_pos[:,0])

        #Conversation from ('letter''number', 'letter''number') to ('0-48', '0-48')
        FROM, TO = m[0], m[1]
        alp = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7}
        
        if ((FROM[0] not in alp) or (TO[0] not in alp) or (int(FROM[1]) not in range(1,row+1)) or (int(TO[1]) not in range(1,row+1))):
            raise ValueError(m)
        
        FROM, TO = ((int(FROM[1])-1)*col)+alp[FROM[0]]-1, ((int(TO[1])-1)*col)+alp[TO[0]]-1
        #===---===---===---===---===---===---===---===---===---===---===---===
        #checking FROM and TO in range(0-->col*row-1)
        if ((FROM<0) or (TO<0) or (FROM >= len(self.pos.flatten())) or (TO >= len(self.pos.flatten()))):
            raise WrongMoveError('Not Permitted: Value/s not in range')
            
        #print('FROM: %s, TO:%s'%(FROM,TO))
        
        #FROM piece must be a self.stm piece(if stm == PLAYER2, FROM can be W or K)
        if not ((self.stm == PLAYER1 and check_pos.flatten()[FROM] == self.stm) or (self.stm == PLAYER2 and (check_pos.flatten()[FROM] == self.stm or check_pos.flatten()[FROM] == KING_VALUE))):
            raise WrongMoveError('Not Permitted: FROM Value not Player_%s'%self.stm)
        #TO must be empty to move on a piece
        if not (check_pos.flatten()[TO] == 0):
            raise WrongMoveError('Not Permitted: TO Value not empty')
            
        #Corners non permitted for B and W, throne non permitted for B, W and K
        if self.stm == PLAYER1:
            if (TO in prohibited_black_el):
                raise WrongMoveError('Not Permitted: TO Value in corners or prohibited_black_el')
        elif self.stm == PLAYER2:
            if (check_pos.flatten()[FROM] == KING_VALUE):#Moving the King piece
                if (TO in prohibited_king_el):
                    raise WrongMoveError('Not Permitted: TO Value in prohibited_king_el(%s,%s)'%m)
            else:
                if (TO in prohibited_white_el):
                    raise WrongMoveError('Not Permitted: TO Value in prohibited_white_el')
        #===---===---===---===---===---===---===---===---===---===---===---===
        #Movement non oblique
        if not ((TO in move_segments[FROM][0]) or (TO in move_segments[FROM][1])):
            raise WrongMoveError('Not Permitted: FROM-TO movement can not be oblique')

        #Free space in movement(FROM-TO)
        mov = self.orthogonal_segment(check_pos,FROM,TO)
        if not mov.sum()==check_pos.flatten()[FROM]:
            raise WrongMoveError('Not Permitted: FROM-TO movement not free')
        
        #"move" the piece FROM -> TO
        check_pos_ret = check_pos.flatten()
        check_pos_ret[TO] = check_pos_ret[FROM]
        check_pos_ret[FROM] = 0

        #
        check_pos = check_pos_ret.copy()
        old_winning = check_pos[winning_el]
        check_pos[winning_el] = self.stm
        old_throne = None
        if check_pos[throne_el] == 0:
            check_pos[throne_el] = self.stm
            old_throne = 0
        
        #print(check_pos.reshape((col,row)))
        
        #Captures Check
        for s in rev_segments[TO]:
            seg = check_pos[s].copy()
            seg[seg==3] = PLAYER2
            c = np.bincount(seg)
            if c[0] or len(c)!=3:
                continue
            if c[self.stm]==2:
                update = check_pos[s].copy()
                update[1]=0
                check_pos[s] = update
        
        check_pos[winning_el] = old_winning
        if old_throne is not None:
            check_pos[throne_el] = old_throne
            
        future_pos = self.from_pos_to_dic(check_pos, col, row)
        #print(future_pos)
        return Board(future_pos, self.other, self._check_end(check_pos, TO))
        
        
    
    #Return the vector between FROM and TO
    @classmethod
    def orthogonal_segment(cls, pos, FROM, TO):
        i_to, i_from, line = None, None, None
        if TO in move_segments[FROM][0]:#mi muovo in una riga
            line = move_segments[FROM][0]
            i_from = int(FROM%len(line))
            i_to = int(TO%len(line))
        elif TO in move_segments[FROM][1]:#mi muovo in una colonna
            line = move_segments[FROM][1]
            i_from = int(FROM/len(line))
            i_to = int(TO/len(line))

        if i_to is None or i_from is None:
            raise ValueError('FROM and TO not in the same orthogonal segment')
        
        if i_to < i_from:
            line = line[i_to:i_from+1]
        else:
            line = line[i_from:i_to+1]
        ret = pos.flatten()
        
        return ret[line]
       
    #Return the trios-pos vector where TO is the first or last element
    @classmethod     
    def capture_segments(cls, pos, TO):
        if isinstance(pos, Board):
            return cls.capture_segments(pos.pos, TO)
        else:
            ret = []
            for c in rev_segments[TO]:
                ret.append(pos[c])
            return np.asarray(ret)
    
    #Transform a compact board's raffiguration(2-Dmatric with 0,1,2,3 elements) to the corresponding dictionary raffiguration 
    @classmethod
    def from_pos_to_dic(cls, pos, col=COL, row=ROW):
        ret = {PLAYER1:np.asarray([],dtype=int), PLAYER2: (np.asarray([],dtype=int),np.asarray([],dtype=int))}
        b, w, k = pos.copy(), pos.copy()-1, pos.copy()-2
        
        b[b!=1] = 0        
        w[w!=1] = 0        
        k[k!=1] = 0

        ret[PLAYER1] = b.reshape((col,row))
        ret[PLAYER2] = (w.reshape((col,row)),k.reshape((col,row)))
        return ret
    
    #the actual and real pos(board configuration) is updated setting the prohibited elements for piece = piece if the element is empty
    @classmethod
    def pos_update(cls, pos, FROM):
        pos = pos.flatten()        
        piece = pos[FROM] #1:black 2:white 3:king
        if piece == 0:
            return pos
        mask = pos[prohibited_segments[piece][FROM]] == 0 #elements to modified just if in pos the el is empty
        seg = prohibited_segments[piece][FROM]
        pos[seg[mask]] = piece
        return pos
    
    def get_all_moves(self):
        ret = []
        moving = self.stm
        original_board = self.pos.flatten()
        
        pos = {PLAYER1: self._pos[PLAYER1].copy(), PLAYER2: self._pos[PLAYER2][0].copy()+self._pos[PLAYER2][1].copy()}
        
        y = pos[moving].flatten()
        indices = _indices.flatten()
        yi = y*indices
        yi = yi[yi>0]#tutti gli indici in cui il player moving ha delle pedine
        for imoves in possible_move_segments[yi]:
            for smove in imoves:#smove[0] FROM index element
                board = original_board.copy()
                board = self.pos_update(board, smove[0])
                if board[smove].sum() == original_board[smove[0]]:
                    ret.append(self.coordinates_int_to_string((smove[0], smove[-1])))
        #shuffle(ret)
        return ret
        
    #Conversion from ('0-48', '0-48') to ('letter''number', 'letter''number')
    @classmethod
    def coordinates_int_to_string(cls, m, col=COL, row=ROW):
        if not isinstance(m, tuple):
            raise ValueError('Move conversion Error: m is not a tuple')

        
        FROM, TO = int(m[0]), int(m[1])
        alp = { 1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H', 9:'I' }
        
        if ((FROM not in range(0, int(col*row))) or (TO not in range(0, int(col*row)))):
            raise ValueError(m)
        
        FROM = alp[int(FROM%col)+1]+str(int(FROM/col)+1)
        TO = alp[int(TO%col)+1]+str(int(TO/col)+1)
        return (FROM, TO)
    #===---===---===---===---===---===---===---===---===---===---===---===
        
            