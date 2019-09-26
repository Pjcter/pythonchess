class Square:
    ' This class represents a square on a chess board. Written by Peter Carter'

    #Constructor method
    def __init__(self,letter,num):
        self.piece = None
        self.num = num #The number of a square
        self.letter = letter #The letter of a square

    #toString method
    def toString(self):
        if self.piece != None:
            return self.letter + str(self.num) + ": " + self.piece.toString()
        return self.letter + str(self.num)

    def addPiece(self,piece):
        self.piece = piece

    def removePiece(self):
        self.piece = None


# End class declaration
