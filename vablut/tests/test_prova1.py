import sys
from vablut.board import *

def operate(l):
    l[0]._stm = PLAYER1


l = []

b1 = Board()
b2 = Board()
b3 = Board()
b4 = Board()
b5 = Board()
b6 = Board()
b7 = Board()
b8 = Board()
l.append(b1)

operate(l)
print(sys.getsizeof(l))
l.append(b2)
l.append(b3)
l.append(b4)
l.append(b5)
l.append(b6)
l.append(b7)
l.append(b8)
print(sys.getsizeof(b1))
print(sys.getsizeof(l[0]))
print(sys.getsizeof(l[1]))
print(sys.getsizeof(l[2]))
print(sys.getsizeof(l[3]))
print(sys.getsizeof(l[4]))