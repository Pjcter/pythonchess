class Square:
    ' This class represents a square on a chess board. Written by Peter Carter'

    #Constructor method
    def __init__(self,letter,num):
        self.num = num #The number of a square
        self.letter = letter #The letter of a square

    #toString method
    def toString(self):
        return self.num + self.letter;


# End class declaration


