#da linea di comando leggere se BLACK o WHITE. 
#Istanziare poi l'engine associato e passarlo al gamehandler
from vablut.engine.random import RandomEngine
from vablut.engine.human import HumanEngine
from vablut.game import GameHandler

def main():
    p1 = RandomEngine(0.2)
    p2 = HumanEngine('Phil')
    gh = GameHandler(p1,p2,True)
    gh.play()

if __name__ == '__main__':
    main()