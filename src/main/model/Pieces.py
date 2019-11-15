class Piece:
    """This piece is an abstract class representing a generic chess piece"""

    def __init__(self,color,value,name,square):
        self.color = color
        self.value = value
        self.name = name
        self.square = square

    def to_string(self):
        return self.color[0] + self.name[0]

    def is_capture(self, destination, board):
        return board.has_any_piece(destination)

    def move(self, destination, board):
        if self.is_capture(destination, board):
            board.make_capture(destination)
        self.square = destination


class Pawn(Piece):
    def __init__(self, color, square):
        Piece.__init__(self, color, 10, "Pawn", square)
        self.just_moved_2 = False

    def move(self,destination,board):
        if self.isEnPassant(destination,board):
            captureSquare = destination[0] + self.square[1]
            board.make_capture(captureSquare)
        if self.is_capture(destination, board):
            board.make_capture(destination)
        if self.isDoubleMove(destination,board):
            self.just_moved_2 = True
        if self.isPromote(destination,board):
            board.promote(self.square,destination)
        self.square = destination

    def isEnPassant(self,destination,board):
        if self.color == "White" and destination[0] != self.square[0]:
            return not board.has_any_piece(destination) and self.is_capture(destination[0] + "5", board)
        elif self.color == "Black" and destination[0] != self.square[0]:
            return not board.has_any_piece(destination) and self.is_capture(destination[0] + "4", board)
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

    def copy(self):
        cpy = Pawn(self.color,self.square)
        return cpy

    def to_string(self):
        if self.color == "White":
            return "♙"
        else:
            return "♟"

class Rook(Piece):
    def __init__(self,color,square):
        Piece.__init__(self,color,50,"Rook",square)

    def move(self,destination,board):
        if self.is_capture(destination, board):
            board.make_capture(destination)
        self.square = destination
        if self.color == "White":
            board.whiteCastle = True
        else:
            board.blackCastle = True

    def copy(self):
        cpy = Rook(self.color, self.square)
        return cpy

    def to_string(self):
        if self.color == "White":
            return "♖"
        else:
            return "♜"

class Bishop(Piece):
    def __init__(self,color,square):
        Piece.__init__(self,color,30,"Bishop",square)

    def copy(self):
        cpy = Bishop(self.color,self.square)
        return cpy

    def to_string(self):
        if self.color == "White":
            return "♗"
        else:
            return "♝"

class Knight(Piece):
    def __init__(self,color,square):
        Piece.__init__(self,color,30,"Knight",square)

    def copy(self):
        cpy = Knight(self.color,self.square)
        return cpy

    def to_string(self):
        if self.color == "White":
            return "♘"
        else:
            return "♞"

class King(Piece):
    def __init__(self,color,square):
        Piece.__init__(self,color,900,"King",square)

    def move(self,destination,board):
        if self.is_capture(destination, board):
            board.make_capture(destination)
        if (self.color == "White" and not board.white_castle) or (self.color == "Black" and not board.black_castle):
            if self.color == "White" and destination == "c1":
                board.get_piece("a1").move("d1", board)
            elif self.color == "White" and destination == "g1":
                board.get_piece("h1").move("f1", board)
            elif self.color == "Black" and destination == "c8":
                board.get_piece("a8").move("d8", board)
            elif self.color == "Black" and destination == "g8":
                board.get_piece("h8").move("f8", board)
        if self.color == "White":
            board.white_castle = True
        else:
            board.black_castle = True
        self.square = destination

    def copy(self):
        cpy = King(self.color,self.square)
        return cpy

    def to_string(self):
        if self.color == "White":
            return "♔"
        else:
            return "♚"

class Queen(Piece):
    def __init__(self,color,square):
        Piece.__init__(self,color,100,"Queen",square)

    def copy(self):
        cpy = Queen(self.color,self.square)
        return cpy

    def to_string(self):
        if self.color == "White":
            return "♕"
        else:
            return "♛"