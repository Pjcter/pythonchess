from src.main.model.Board import *
from src.main.model.RuleSet import *

class Game:
    'Representation of a game of chess'

    def __init__(self):
        self.board = Board()
        self.ruleSet = RuleSet()
        self.turn = "White"
        self.gameOver = False
        self.winner = None

    def changeTurn(self):
        if(self.turn == "White"):
            self.turn = "Black"
        else:
            self.turn = "White"


game = Game()
while True:
        print(game.board.toString())
        print(game.turn+"'s Turn!")
        inpt = input("Enter move as: \"[Piece] [From] [To]\": ")
        info = inpt.split(" ")
        if info == "Q" or info.__len__() < 3:
            break
        piece = info[0]
        s1 = info[1]
        s2 = info[2]
        if game.ruleSet.validateMove(piece,game.turn,game.turn,game.board,s1,s2):
            game.board = game.board.makeMove(s1,s2)
            print("Move made!")
            game.changeTurn()
        else:
            print("Move failed!")
print("Exiting Chess!")

