from src.main.model.Square import Square
from src.main.model.Pieces import *

class Board:
    'Representation of a chess Board. Written by Peter Carter'

    #Creates a new board
    def __init__(self):
        b = {}
        # Populate with squares
        for num in range(1,9):
            for letter in "ABCDEFGH":
                b[letter+str(num)] = Square(letter,num)
        #End for loop. squares is now populated with square objects key'd by their toString

        # Now populate with pieces
        #Pawns
        for ltr in "ABCDEFGH":
            b[ltr+"2"].addPiece(Pawn("White"))
            b[ltr+"7"].addPiece(Pawn("Black"))
        #Hardcoding other pieces
        b["A1"].addPiece(Rook("White"))
        b["B1"].addPiece(Knight("White"))
        b["C1"].addPiece(Bishop("White"))
        b["D1"].addPiece(Queen("White"))
        b["E1"].addPiece(King("White"))
        b["F1"].addPiece(Bishop("White"))
        b["G1"].addPiece(Knight("White"))
        b["H1"].addPiece(Rook("White"))
        b["A8"].addPiece(Rook("Black"))
        b["B8"].addPiece(Knight("Black"))
        b["C8"].addPiece(Bishop("Black"))
        b["D8"].addPiece(Queen("Black"))
        b["E8"].addPiece(King("Black"))
        b["F8"].addPiece(Bishop("Black"))
        b["G8"].addPiece(Knight("Black"))
        b["H8"].addPiece(Rook("Black"))
        self.board = b
        #Keeps track if white or black has castled
        self.whiteCastle = False
        self.blackCastle = False

    def getPieceList(self):
        pieces = []
        for key in self.board.keys():
            if self.board[key].piece != None:
                pieces.append(self.board[key].piece)
        return pieces

    def toString(self):
        result = ""
        for square in self.board.values():
            result += " " + square.toString()
        return result

    #Logic for determining if a board has a given piece on a given square
    #Piece: Piece name
    #Square: Square name. Must be a valid square name in string form "[Letter][Number]" eg "E4"
    def hasPiece(self,piece,color,square):
        s1 = self.board[square]
        if(s1.piece!=None):
            if(s1.piece.name == piece and s1.piece.color == color):
                return True
        return False

    def cloneBoard(self):
        newBoard = Board()
            #Remove all pieces
        for sqr in newBoard.board.values():
            sqr.removePiece()
        for key in self.board.keys():
            #Point new board squares to pieces
            if self.board[key].piece != None:
                newBoard.board[key].addPiece(self.board[key].piece)
        newBoard.whiteCastle = self.whiteCastle
        newBoard.blackCastle = self.blackCastle
        return newBoard
    #Does not alter THIS board. Creates a new board, and makes the move on that board. And returns that board.
    def makeMove(self,square1Name,square2Name):
        newBoard = self.cloneBoard()
        p = newBoard.board[square1Name].piece
        if p == None:
            return newBoard
        newBoard.board[square1Name].removePiece()
        newBoard.board[square2Name].addPiece(p)
        return newBoard

b = Board()
print(b.toString())
c = b.makeMove("E2","E4")
print(c.toString())







