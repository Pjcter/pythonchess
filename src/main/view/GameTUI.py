from src.main.model.Game import *
from src.main.model.AIGame import *

def __main__():
    game = AIGame("Black",3)
    #game = Game()
    while True:
        print(game.board.to_string())
        print(game.turn + "'s Turn!")
        if(game.is_checked(game.turn)):
            print("CHECK!")
        inpt = input("Enter move as: \"[squareFrom] [squareTo]\": ")
        info = inpt.split(" ")
        if info == "Q" or info.__len__() != 2:
            break
        s1 = info[0]
        s2 = info[1]
        if game.make_move(s1, s2):
            print("Moved made!")
        else:
            print("Moved failed")
    print("Exiting Chess!")

__main__()