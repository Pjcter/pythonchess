from src.main.model.Square import Square
from src.main.model.Pieces import *

class Board:
    'Representation of a chess Board. Written by Peter Carter'

    #Creates a new board
    def __init__(self):
        squares = []
        # Populate with squares
        for num in range(1,9):
            for letter in "ABCDEFGH":
                squares.append(Square(letter,num))
        #End for loop. squares is now populated with square objects
        pieces = []
        # Now populate with pieces
        #Pawns
        for ltr in "ABCDEFGH":
            pieces.append((Pawn("White",ltr+"2")))
            pieces.append((Pawn("Black",ltr+"7")))
        #Hardcoding other pieces
        pieces.append(Rook("White","A1"))
        pieces.append(Knight("White","B1"))
        pieces.append(Bishop("White","C1"))
        pieces.append(Queen("White","D1"))
        pieces.append(King("White","E1"))
        pieces.append(Bishop("White","F1"))
        pieces.append(Knight("White","G1"))
        pieces.append(Rook("White","H1"))
        pieces.append(Rook("Black","A8"))
        pieces.append(Knight("Black","B8"))
        pieces.append(Bishop("Black","C8"))
        pieces.append(Queen("Black","D8"))
        pieces.append(King("Black","E8"))
        pieces.append(Bishop("Black","F8"))
        pieces.append(Knight("Black","G8"))
        pieces.append(Rook("Black","H8"))

        #Keeps track if white or black has castled
        self.whiteCastle = False
        self.blackCastle = False

    def getAllPieces(self):
        return self.pieces

    def getBlackPieces(self):
        bpieces = []
        for piece in self.pieces:
            if piece.color == "Black":
                bpieces.append(piece)
        return bpieces

    def getWhitePieces(self):
        wpieces = []
        for piece in self.pieces:
            if piece.color == "White":
                wpieces.append(piece)
        return wpieces

    #Logic for determining if a board has a given piece on a given square
    #Piece: Piece name
    #Square: Square name. Must be a valid square name in string form "[Letter][Number]" eg "E4"
    def hasGivenPiece(self,name,color,square):
        for piece in self.pieces:
            if piece.name == name and piece.color == color and piece.square == square:
                return True
        return False
    #Used to determine if a given square has a piece on it
    def hasAnyPiece(self,square):
        for piece in self.pieces:
            if piece.square == square:
                return True
        return False
    #Used to determine if a given square as a piece of given color on it
    def hasColorPiece(self,color,square):
        for piece in self.pieces:
            if piece.square == square and piece.color == color:
                return True
        return False

    def kingLocation(self,color):
        for piece in self.pieces:
            if piece.name == "King" and piece.color == color:
                return piece.square

    def cloneBoard(self):
        newBoard = Board()
        #Erase the initialized pieces
        newBoard.pieces = []
        for piece in self.pieces:
            #Copy over pieces
            newBoard.pieces.append(piece)
        #Copy over castle states
        newBoard.whiteCastle = self.whiteCastle
        newBoard.blackCastle = self.blackCastle
        return newBoard

    #Logic for moving a single piece
    def makeMove(self,square1Name,square2Name):
        newBoard = self.cloneBoard()
        p = newBoard.board[square1Name].piece
        if p == None:
            return newBoard
        newBoard.board[square1Name].removePiece()
        newBoard.board[square2Name].addPiece(p)
        return newBoard

    #Logic for castling
    def makeCastle(self....params):

    #Logic for capturing
    def makeCapture(self,):




