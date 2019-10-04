from src.main.model.Square import Square
from src.main.model.Pieces import *

class Board:
    'Representation of a chess Board. Written by Peter Carter'

    #Creates a new board
    def __init__(self):
        self.squares = []
        # Populate with squares
        for num in "12345678":
            for letter in "ABCDEFGH":
                self.squares.append(Square(letter,num))
        self.pieces = []
        # Now populate with pieces
        for ltr in "ABCDEFGH":
            self.pieces.append((Pawn("White",ltr+"2")))
            self.pieces.append((Pawn("Black",ltr+"7")))
        #Hardcoding other pieces
        self.pieces.append(Rook("White", "A1"))
        self.pieces.append(Knight("White", "B1"))
        self.pieces.append(Bishop("White", "C1"))
        self.pieces.append(Queen("White", "D1"))
        self.pieces.append(King("White", "E1"))
        self.pieces.append(Bishop("White","F1"))
        self.pieces.append(Knight("White","G1"))
        self.pieces.append(Rook("White","H1"))
        self.pieces.append(Rook("Black","A8"))
        self.pieces.append(Knight("Black","B8"))
        self.pieces.append(Bishop("Black","C8"))
        self.pieces.append(Queen("Black","D8"))
        self.pieces.append(King("Black","E8"))
        self.pieces.append(Bishop("Black","F8"))
        self.pieces.append(Knight("Black","G8"))
        self.pieces.append(Rook("Black","H8"))
        #Keeps track if white or black has castled
        self.whiteCastle = False
        self.blackCastle = False

    #Accessor method for all pieces on the board
    def getAllPieces(self):
        return self.pieces

    #Accessor method for all black pieces on the board
    def getBlackPieces(self):
        bpieces = []
        for piece in self.pieces:
            if piece.color == "Black":
                bpieces.append(piece)
        return bpieces

    #Accessor method for all white pieces on the board
    def getWhitePieces(self):
        wpieces = []
        for piece in self.pieces:
            if piece.color == "White":
                wpieces.append(piece)
        return wpieces

    #Logic for determining if a board has a given piece on a given square. Name, Color, and Square are all strings.
    def hasGivenPiece(self,name,color,square):
        for piece in self.pieces:
            if piece.name == name and piece.color == color and piece.square == square:
                return True
        return False

    #Used to determine if a given square has a piece on it. Square is a string
    def hasAnyPiece(self,square):
        for piece in self.pieces:
            if piece.square == square:
                return True
        return False

    #Used to determine if a given square as a piece of given color on it, color and square are strings
    def hasColorPiece(self,color,square):
        for piece in self.pieces:
            if piece.square == square and piece.color == color:
                return True
        return False

    #Used to return the given color kings square
    def kingLocation(self,color):
        for piece in self.pieces:
            if piece.name == "King" and piece.color == color:
                return piece.square

    #Used to clone the board. Returns a board object
    def cloneBoard(self):
        newBoard = Board()
        newBoard.pieces = []
        for piece in self.pieces:
            newBoard.pieces.append(piece.copy())
        newBoard.whiteCastle = self.whiteCastle
        newBoard.blackCastle = self.blackCastle
        return newBoard

    #Moves a piece. Call through method from Game to a single Piece. Returns the new board.
    def makeMove(self,s1,s2):
        newBoard = self.cloneBoard()
        p = newBoard.getPiece(s1)
        p.move(s2,newBoard)
        return newBoard

    #Logic for capturing. If a piece makes a capture in Piece.Move, it tells the board to remove the piece using this.
    def makeCapture(self,square):
        p = self.getPiece(square)
        p.square = None
        self.pieces.remove(p)

    def getPiece(self,square):
        for piece in self.pieces:
            if piece.square == square:
                return piece
        return None

    def toString(self):
        ltrs = "ABCDEFGH"
        nums = "87654321"
        brd = ""
        for num in nums:
            row = num + " "
            for ltr in ltrs:
                sqr = ltr+num
                if self.hasAnyPiece(sqr):
                    row += self.getPiece(sqr).toString() + "  "
                else:
                    row += "    "
            brd += row + '\n'
        brd += "  A   B   C   D   E   F   G   H"
        return brd