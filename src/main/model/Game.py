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
            for piece in self.board.getBlackPieces():
                if piece.name == "Pawn":
                    piece.justMoved2 = False
        else:
            self.turn = "White"
            for piece in self.board.getWhitePieces():
                if piece.name == "Pawn":
                    piece.justMoved2 = False

    def isChecked(self,color):
        return self.ruleSet.isInCheck(self.board,color,self.board.kingLocation(color))

