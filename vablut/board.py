# -*- coding: utf-8 -*-
import numpy as np
from vablut.modules.tables import _indices, move_segments, capture_segments, rev_segments, possible_move_segments
from vablut.modules.ashton import PLAYER1, PLAYER2, DRAW, COMPUTE, KING_VALUE, throne_el, blacks, whites, king, king_capture_segments, winning_el, prohibited_segments, capturing_dic
from random import shuffle

COL = int(len(_indices[0]))
ROW = int(len(_indices.transpose()[0]))

class WrongMoveError(Exception):
    pass

class Board(object):
    def __init__(self, pos=None, stm=PLAYER2, end=COMPUTE, last_move=None, draw_dic=None):
        if pos is None:
            pos = {PLAYER1:blacks, PLAYER2: (whites,king)}
 
        self._pos = pos
        self._stm = stm
        if end == COMPUTE:
            self._end = self._check_end(self.pos, last_move, draw_dic)
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
    
    def _check_end(self, pos, last_move=None, draw_dic=None):
        if draw_dic is not None:
            if self.hashkey() in draw_dic:
                return DRAW
            else:
                draw_dic[self.hashkey()] = True
        
        if KING_VALUE in self.win_segments(pos):
            return PLAYER2
        
        if len(self.get_all_moves()) == 0:
            return self.other
        
        if last_move is not None:
            pos = pos.flatten()
            if pos[pos==KING_VALUE].sum() == 0:#if in the previous black movement the king is been captured
                return PLAYER1
            #pos drug
            i_king = _indices.flatten()[pos == KING_VALUE][0]
            pos = self.pos_update(pos, last_move)
            pos[i_king] = KING_VALUE
            for seg in king_capture_segments[i_king]:
                if last_move in seg:
                    c = np.bincount(pos[seg])
                    if c[PLAYER1] == len(seg)-1:
                        return PLAYER1
        return None
    
    @classmethod
    def win_segments(cls, pos):
        if isinstance(pos, Board):
            return cls.win_segments(pos.pos)
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
            s += '\n<<< Game over: draw'
        elif self.end is not None:
            s += '\n<<< Game over: %s win' % disc[self.end]
        else:
            s += '\n<<< Move to %s' % disc[self.stm]
        
        return s
    
    #m must be a tuple (FROM, TO). es ('D1', 'F1')
    def move(self, m):
        if not isinstance(m, tuple):
            raise ValueError(m)
        
        check_pos = self.pos

        #Conversation from ('letter''number', 'letter''number') to ('0-48', '0-48')
        FROM, TO = self.coordinates_string_to_int(m)
        #print('FROM: %s, TO:%s'%(FROM,TO))
        
        #FROM piece must be a self.stm piece(if stm == PLAYER2, FROM can be W or K)
        if not ((self.stm == PLAYER1 and check_pos.flatten()[FROM] == self.stm) or (self.stm == PLAYER2 and (check_pos.flatten()[FROM] == self.stm or check_pos.flatten()[FROM] == KING_VALUE))):
            raise WrongMoveError('Not Permitted: FROM Value not Player_%s'%self.stm)
        #TO must be empty to move on a piece
        if not (check_pos.flatten()[TO] == 0):
            raise WrongMoveError('Not Permitted: TO Value not empty')
            
        check_drug_pos = self.pos_update(check_pos, FROM)

        #Free space in movement(FROM-TO)
        try:
            mov = self.orthogonal_segment(check_drug_pos,FROM,TO)
        except:
            raise WrongMoveError('Not Permitted: FROM-TO movement can not be oblique')
        
        if not mov.sum()==check_drug_pos[FROM]:
            raise WrongMoveError('Not Permitted: FROM-TO movement not free')
        
        #"move" the piece FROM -> TO
        check_pos_ret = check_pos.flatten()
        check_pos_ret[TO] = check_pos_ret[FROM]
        check_pos_ret[FROM] = 0
        check_pos = check_pos_ret.copy()
        
        check_drug_pos = self.pos_update_capturing(check_pos, TO)
        
        #Captures Check
        for s in rev_segments[TO]:
            seg = check_drug_pos[s].copy()
            seg_pos = check_pos[s]
            if seg[1] != self.other:#Non posso mangiare il re, è utlizzato dal _check_end per controllare se l'intorno lo ha catturato o meno
                continue
            seg[seg==KING_VALUE] = PLAYER2
            c = np.bincount(seg)
            if c[0] or len(c)!=3:
                continue
            if c[self.stm]==2:
                seg_pos[1]=0
                check_pos[s] = seg_pos
            
        future_pos = self.from_pos_to_dic(check_pos, COL, ROW)
        return Board(future_pos, self.other, COMPUTE, TO)
    
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
    
    @classmethod
    def pos_update_capturing(cls, pos, TO):
        pos = pos.flatten()        
        piece = pos[TO] #1:black 2:white 3:king
        if piece == 0:
            return pos
        pos[capturing_dic[piece]] = piece
        #pos[throne_el] = piece  #THRONE always considerated friend, the camp's elements(the center one not included) friends if they are not occupied
        return pos
    
    #the actual and real pos(board configuration) is updated setting the prohibited elements for piece = piece if the element is empty
    @classmethod
    def pos_update(cls, pos, FROM):
        pos = pos.flatten()        
        piece = pos[FROM] #1:black 2:white 3:king
        if piece == 0:
            return pos
        #NO -> TO DRUG ALWAYS mask = pos[prohibited_segments[piece][FROM]] == 0 #elements to modified just if in pos the el is empty
        #seg = prohibited_segments[piece][FROM]
        pos[prohibited_segments[piece][FROM]] = piece
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
        shuffle(ret)
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
    #Conversion from ('letter''number', 'letter''number') to ('0-48', '0-48')
    @classmethod
    def coordinates_string_to_int(cls, m, col=COL, row=ROW):
        if not isinstance(m, tuple):
            raise ValueError('Move conversion Error: m is not a tuple')

        FROM, TO = m[0], m[1]
        alp = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9}
        
        if ((FROM[0] not in alp) or (TO[0] not in alp) or (int(FROM[1]) not in range(1,row+1)) or (int(TO[1]) not in range(1,row+1))):
            raise ValueError(m)
        
        FROM, TO = ((int(FROM[1])-1)*col)+alp[FROM[0]]-1, ((int(TO[1])-1)*col)+alp[TO[0]]-1 
        return (FROM, TO)
    #===---===---===---===---===---===---===---===---===---===---===---===
    
    def hashkey(self):
        return hash(str(self.pos))
    
    # === === === Method for Evaluator purpose === === ===
    #Return black pieces - white pieces(king excluded)
    @classmethod
    def pieces_difference(cls, pos):
        c = np.bincount(pos.flatten(), minlength=3)
        return c[PLAYER1]-c[PLAYER2]
    
    #Number of winning elements that are blocked from w/b and number of w/b pieces that can get with 1 movement
    @classmethod
    def escape_el_stats(cls, pos): #[OCCUPIED from w, OCCUPIED from b, 1 move w to occupied, 1 move b to occupied]
        stats = {PLAYER1: np.zeros(2, dtype=int), PLAYER2: np.zeros(2, dtype=int), KING_VALUE: np.zeros(2, dtype=int)}
        block_stats = {PLAYER1: np.zeros(3, dtype=int), PLAYER2: np.zeros(3, dtype=int), KING_VALUE: np.zeros(3, dtype=int)} # b:[blocking black, blocking white, blocking king] w:same k:same
        pos = pos.flatten()
        for w in winning_el:
            if pos[w]: # if w pos is full it will be impossible get it on
                #print('w-pos: %s occupata da Pezzo%s'%(str(w),pos[w]))
                stats[pos[w]][0] += 1
                continue
            for pms in possible_move_segments[w]:
                segment = pos[pms]
                if not segment.sum():#void board segment filtered
                    #print('%s - %s FILTRATO'%(segment,pms))
                    continue
                c = np.bincount(segment, minlength=4)
                if c[1:].sum()==1 and segment[-1]!=0:#1 move check
                    if cls.pos_update(pos,pms[-1])[pms[1:-1]].sum() == 0:
                        stats[segment[-1]][1] += 1
                        #print('%s - %s <-- Pezzo%s 1 move to winning %s-pos'%(segment,pms,segment[-1],pms[0]))
                    #else:
                    #    print('%s - %s <-- Pezzo%s 1 move OSTACOLATO to %s-pos[%s]'%(segment,pms,segment[-1],pms[0],self.pos_update(pos,pms[-1])[pms[1:-1]]))
                elif segment[-1]!=0: # Direct Blocking check [win_el, 0, ..., ->#<-, 0, ..., #]
                    cutted_seg = segment[1:-1]
                    if (cutted_seg == cls.pos_update(pos,pms[-1])[pms[1:-1]]).all():
                        #print('prima:%s dopo:%s uguale a:%s'%(segment,cutted_seg,self.pos_update(pos,pms[-1])[pms[1:-1]]))
                        cutted_seg = cutted_seg[cutted_seg>0]
                        if len(cutted_seg) == 1:
                            block_stats[cutted_seg[0]][segment[-1]-1] += 1
                    #else:
                    #    print('prima:%s dopo:%s uguale a:%s FILTRATO'%(segment,cutted_seg,self.pos_update(pos,pms[-1])[pms[1:-1]]))
        #print('[Occupied w els, 1 move to w els]- B%s  W%s  K%s'%(stats[PLAYER1],stats[PLAYER2],stats[KING_VALUE]))
        #print('[blocking B pieces, blocking W pieces, blocking the K]- B%s  W%s  K%s'%(block_stats[PLAYER1],block_stats[PLAYER2],block_stats[KING_VALUE]))  
        return stats, block_stats
    # get stats about the king position
    # [escape distance, capturable, # move for capturing, free els around k, b pieces around k, w pieces around k, b 1 move to king, w 1 move to king]
    @classmethod
    def king_stats(cls, pos):
        pos = pos.flatten()
        stats = np.zeros(8, dtype=int)
        king_i = int(_indices.flatten()[pos == 3])
        # 1-capturable) The king is capturable if the black player can move his pieces next to the king
        for k_capture_s in king_capture_segments[king_i]:
            k_capture_s = k_capture_s[k_capture_s!=king_i]
            ret = np.zeros(len(k_capture_s), dtype=bool)
            num_moves = 0
            for i,nex_to_k in enumerate(k_capture_s):
                print('checking:%s'%nex_to_k)
                if pos[nex_to_k] == PLAYER1:
                    ret[i] = True
                elif cls.pos_reachable_by_player(pos, nex_to_k, PLAYER1):
                    ret[i] = True
                    num_moves += 1
                    print(ret)
            print('moves:%s'%num_moves)
            if (ret == True).all():
                stats[1] = True
            if (stats[2]== 0 or stats[2]>num_moves) and num_moves>0:
                stats[2]=num_moves
        print(stats)
    # True if the board index is empty and reachable in 1 move by the player[PLAYER1, PLAYER2 or KING_VALUE]
    @classmethod
    def pos_reachable_by_player(cls, pos, index, player):
        pos = pos.flatten()
        if pos[index]:#index already occupied, return False
            return False      
        for move in possible_move_segments[index]:
            segment = pos[move]
            if segment[-1] and np.bincount(segment[segment!=0]).sum() == 1:
                drug_pos     = cls.pos_update(pos, move[-1])
                drug_segment = drug_pos[move]
                if (segment == drug_segment).all() and segment[-1]==player:
                    return True
        return False
                    