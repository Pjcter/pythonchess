from src.main.model.Square import Square
from src.main.model.Pieces import *

class Board:
    """Representation of a chess Board. Written by Peter Carter"""

    def __init__(self, is_new_game=True):
        """Creates a new board"""
        self.squares = []
        for num in "12345678":
            for letter in "abcdefgh":
                self.squares.append(Square(letter,num))
        self.pieces = []
        if is_new_game:
            for ltr in "abcdefgh":
                self.pieces.append((Pawn("White", ltr + "2")))
                self.pieces.append((Pawn("Black", ltr + "7")))
            self.pieces.append(Rook("White", "a1"))
            self.pieces.append(Knight("White", "b1"))
            self.pieces.append(Bishop("White", "c1"))
            self.pieces.append(Queen("White", "d1"))
            self.pieces.append(King("White", "e1"))
            self.pieces.append(Bishop("White","f1"))
            self.pieces.append(Knight("White","g1"))
            self.pieces.append(Rook("White","h1"))
            self.pieces.append(Rook("Black","a8"))
            self.pieces.append(Knight("Black","b8"))
            self.pieces.append(Bishop("Black","c8"))
            self.pieces.append(Queen("Black","d8"))
            self.pieces.append(King("Black","e8"))
            self.pieces.append(Bishop("Black","f8"))
            self.pieces.append(Knight("Black","g8"))
            self.pieces.append(Rook("Black","h8"))
            self.white_castle = False
            self.black_castle = False

    def make_move(self, s1, s2):
        new_board = self.clone_board()
        p = new_board.get_piece(s1)
        p.move(s2, new_board)
        return new_board

    def make_capture(self, square):
        p = self.get_piece(square)
        p.square = None
        self.pieces.remove(p)

    def promote(self, origin, destination):
        p = self.get_piece(origin)
        self.pieces.remove(p)
        q = Queen(p.color, destination)
        self.pieces.append(q)

    def clone_board(self):
        new_board = Board(False)
        for piece in self.pieces:
            new_board.pieces.append(piece.copy())
        new_board.white_castle = self.white_castle
        new_board.black_castle = self.black_castle
        return new_board

    def get_all_pieces(self):
        return self.pieces

    def get_pieces(self, color):
        pieces = []
        for piece in self.pieces:
            if piece.color == color:
                pieces.append(piece)
        return pieces

    def get_piece(self, square):
        for piece in self.pieces:
            if piece.square == square:
                return piece
        return None

    def has_given_piece(self, name, color, square):
        for piece in self.pieces:
            if piece.square == square:
                if piece.name == name and piece.color == color:
                    return True
        return False

    def has_any_piece(self, square):
        for piece in self.pieces:
            if piece.square == square:
                return True
        return False

    def has_color_piece(self, color, square):
        for piece in self.pieces:
            if piece.square == square and piece.color == color:
                return True
        return False

    def find_king_location(self, color):
        for piece in self.pieces:
            if piece.name == "King" and piece.color == color:
                return piece.square

    def to_string(self):
        brd = ""
        for num in "87654321":
            row = num + " "
            for ltr in "abcdefgh":
                sqr = ltr+num
                if self.has_any_piece(sqr):
                    row += self.get_piece(sqr).to_string() + "  "
                else:
                    row += "    "
            brd += row + '\n'
        brd += "  a   b   c   d   e   f   g   h"
        return brd