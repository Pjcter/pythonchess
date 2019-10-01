class Piece:
    'This piece is an abstract class representing a generic chess piece'

    #Constructor
    def __init__(self,color,value,name):
        self.color = color
        self.value = value
        self.name = name

    def toString(self):
        return self.color + " " + self.name

    def isCapture(self):
        print("Piece subclass has no isCapture implementation")
        return EnvironmentError

class Pawn(Piece):
    def __init__(self,color):
        Piece.__init__(self,color,1,"Pawn")

class Rook(Piece):
    def __init__(self,color):
        Piece.__init__(self,color,5,"Rook")

class Bishop(Piece):
    def __init__(self,color):
        Piece.__init__(self,color,3,"Bishop")

class Knight(Piece):
    def __init__(self,color):
        Piece.__init__(self,color,3.5,"Knight")

class King(Piece):
    def __init__(self,color):
        Piece.__init__(self,color,10,"King")

class Queen(Piece):
    def __init__(self,color):
        Piece.__init__(self,color,10,"Queen")
