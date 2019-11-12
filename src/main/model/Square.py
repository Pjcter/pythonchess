class Square:
    ' This class represents a square on a chess board. Written by Peter Carter'

    #Constructor method
    def __init__(self,letter,num):
        self.num = num #The number of a square
        self.letter = letter #The letter of a square
        self.x_coord =  ord(letter)-97
        self.y_coord = 8-int(num)
        if letter in "aceg":
            if num in "1357":
                self.color = "Black"
            else:
                self.color = "White"
        else:
            if num in "1357":
                self.color = "White"
            else:
                self.color = "Black"

    #toString method
    def toString(self):
        if self.piece != None:
            return self.letter + self.num
        return self.letter + self.num

# End class declaration
