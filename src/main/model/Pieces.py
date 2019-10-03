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

    def isCapture(self, destination, board):
        if (board.hasAnyPiece(destination)):
            return True
        else:
            return False

    def move(self,destination,board):
        if self.isCapture(self, destination, board):
            board.makeCapture(destination)
        self.square = destination

class Pawn(Piece):
    def __init__(self,color,square):
        Piece.__init__(self,color,1,"Pawn",square)
        self.justMoved2 = False

    def move(self,destination,board):
        if self.isCapture(destination,board):
            board.makeCapture(destination)
        if self.isDoubleMove(destination,board):
            self.justMoved2 = True
        if self.isEnPassant(destination,board):
            pass
        if self.isPromote(destination,board):
            pass
        self.square = destination

    def isEnPassant(self,destination,board):
        # DO THIS
        return False

    def isPromote(self,destination,board):
        if self.color == "White" and destination[1] == "8":
            return True
        elif self.color == "Black" and destination[1] == "1":
            return True
        return False

    def isDoubleMove(self,destination,board):
        if self.color == "White" and self.square[1] == "2" and destination[1] == "4":
            return True
        elif self.color == "Black" and self.square[1] == "7" and destination[1] == "5":
            return True
        return False

class Rook(Piece):
    def __init__(self,color,square):
        Piece.__init__(self,color,5,"Rook",square)

    def move(self,destination,board):
        if self.isCapture(destination,board):
            board.makeCapture(destination)
        if self.color == "White":
            board.whiteCastle = True
        else:
            board.blackCastle = True

class Bishop(Piece):
    def __init__(self,color,square):
        Piece.__init__(self,color,3,"Bishop",square)



class Knight(Piece):
    def __init__(self,color,square):
        Piece.__init__(self,color,3.5,"Knight",square)

class King(Piece):
    def __init__(self,color,square):
        Piece.__init__(self,color,10,"King",square)

    def move(self,destination,board):
        if self.isCapture(destination,board):
            board.makeCapture(destination)
        #Check if castle, if so, move the rook too.
        if (self.color == "White" and board.whiteCastle == False ) or (self.color == "Black" and board.blackCastle == False):
            if(self.color == "White" and destination == "C1"):
                board.makeMove("A1","D1")
            elif(self.color == "White" and destination == "G1"):
                board.makeMove("H1","F1")
            elif(self.color == "Black" and destination == "C8"):
                board.makeMove("A8","D8")
            elif(self.color == "Black" and destination == "G8"):
                board.makeMove("H8,F8")
        if self.color == "White":
            board.whiteCastle = True
        else:
            board.blackCastle = True
        self.square = destination

class Queen(Piece):
    def __init__(self,color,square):
        Piece.__init__(self,color,10,"Queen",square)


