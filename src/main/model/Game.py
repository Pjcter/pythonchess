from src.main.model.Board import *
from src.main.model.RuleSet import *


class Game:
    """Representation of a game of chess"""

    def __init__(self):
        self.board_history = []
        self.board = Board()
        self.board_history.append(self.board)
        self.rule_set = RuleSet()
        self.turn = "White"

    def make_move(self, origin, destination):
        if not self.board.has_any_piece(origin):
            return False
        piece = self.board.get_piece(origin)
        if self.rule_set.validate_move(piece.name, piece.color, self.turn, self.board, origin, destination):
            self.board = self.board.make_move(origin, destination)
            self.board_history.append(self.board)
            self.change_turn()
            return True
        else:
            return False

    def change_turn(self):
        if self.turn == "White":
            next = "Black"
        else:
            next = "White"
        self.turn = next
        for piece in self.board.get_pieces(next):
            if piece.name == "Pawn":
                piece.just_moved_2 = False

    def is_checked(self, color):
        return self.rule_set.is_in_check(self.board, color, self.board.find_king_location(color))

    def is_checkmated(self, color):
        if self.is_checked(color):
            if len(self.rule_set.find_all_legal_moves(self.board, color)) == 0:
                return True
        return False

    def is_stalemated(self, color):
        if self.turn == color:
            if not self.is_checked(color):
                if len(self.rule_set.find_all_legal_moves(self.board, color)) == 0:
                    return True
        return False

