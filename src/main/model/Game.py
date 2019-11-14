from src.main.model.Board import *
from src.main.model.RuleSet import *

class Game:
    'Representation of a game of chess'

    def __init__(self):
        self.boardHistory = []
        self.board = Board()
        self.boardHistory.append(self.board)
        self.ruleSet = RuleSet()
        self.turn = "White"
        self.gameOver = False
        self.winner = None

    def makeMove(self,origin,destination):
        if not self.board.hasAnyPiece(origin):
            return False
        piece = self.board.getPiece(origin)
        if self.ruleSet.validateMove(piece.name, piece.color, self.turn, self.board, origin,destination):
            # Valid move, so we make it and return true
            self.board = self.board.makeMove(origin,destination)
            self.boardHistory.append(self.board)
            self.changeTurn()
            return True
        else:
            # Invalid move, so we return false
            return False

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

    def isCheckmated(self, color):
        if self.isChecked(color):
            if len(self.ruleSet.findAllLegalMoves(self.board,color))==0:
                return True
        return False

    def isStalemated(self, color):
        if self.turn == color:
            if not self.isChecked(color):
                if len(self.ruleSet.findAllLegalMoves(self.board,color))==0:
                    return True
        return False

