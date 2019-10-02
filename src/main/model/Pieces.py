class Piece:
    'This piece is an abstract class representing a generic chess piece'

    #Constructor
    def __init__(self,color,value,name,square):
        self.color = color
        self.value = value
        self.name = name
        self.square = square

    def toString(self):
        return self.color + " " + self.name

    def isCapture(self):
        print("Piece subclass has no isCapture implementation")

    def move(self,square):
        print("Piece subclass has no move implementation")

class Pawn(Piece):
    def __init__(self,color,square):
        Piece.__init__(self,color,1,"Pawn",square)

    def move(self,destination,board):
        #Implement Move
    def isCapture(self,destination,board):
        #Implement isCapture
    def isEnPassant(self,destination,board):
        #Implmenent enpassant
    def isPromote(self,destination,board):
        #Implement promote
    def isDoubleMove(self,destination,board):
        #Implement initially moving two up

class Rook(Piece):
    def __init__(self,color,square):
        Piece.__init__(self,color,5,"Rook",square)

    def move(self,destination,board):
        #Implement Move
    def isCapture(self,destination,board):
        #Implmenet isCapture

    #Maybe add castle logic here?

class Bishop(Piece):
    def __init__(self,color,square):
        Piece.__init__(self,color,3,"Bishop",square)

    def move(self,destination,board):
        #Implement Move
    def isCapture(self,destination,board):
        #Implement isCapture

class Knight(Piece):
    def __init__(self,color,square):
        Piece.__init__(self,color,3.5,"Knight",square)
    def move(self,destination,board):
        #Implement Move
    def isCapture(self,destination,board):
        #Implement isCapture

class King(Piece):
    def __init__(self,color,square):
        Piece.__init__(self,color,10,"King",square)

    def move(self,destination,board):
        #Implmenet Move
    def isCapture(self,destination,board):
        #Implement isCapture
    def isCastle(self,destination,board):
        #Implement isCastle

class Queen(Piece):
    def __init__(self,color):
        Piece.__init__(self,color,10,"Queen",square)

    def move(self,destination,board):
        #Implement move
    def isCapture(self,destination,board):
        #Implement isCapture
