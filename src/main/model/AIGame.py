from src.main.model.Game import *
from datetime import datetime
import random

class AIGame(Game):

    def __init__(self, ai_color, ai_diff):
        super().__init__()
        self.color = ai_color
        self.diff = ai_diff
        self.n=0
        if self.color == "Black":
            self.enemy = "White"
        else:
            self.enemy = "Black"

    def make_move(self, origin, destination):
        if not self.board.has_any_piece(origin):
            return False
        piece = self.board.get_piece(origin)
        if self.rule_set.validate_move(piece.name, piece.color, self.turn, self.board, origin, destination):
            # Valid move, so we make it and return true
            self.board = self.board.make_move(origin, destination)
            self.board_history.append(self.board)
            self.change_turn()
            #Tell the AI to go
            if self.turn == self.color:
                t1 = datetime.now()
                s1, s2 = self.minimax_root(self.diff, self.board)
                t2 = datetime.now()
                self.make_move(s1, s2)
                print(str(self.n) + " boards evaluated")
                print("in " + str(t2-t1) + " seconds")
            return True
        else:
            # Invalid move, so we return false
            return False

    def evaluate_board(self, board):
        white_pieces = board.get_pieces("White")
        black_pieces = board.get_pieces("Black")
        white_sum = 0
        black_sum = 0
        for piece in white_pieces:
            white_sum += piece.value
        for piece in black_pieces:
            black_sum += piece.value
        return white_sum - black_sum

    #TODO: Fiugre out why this isn't working!! Maximizing player should be white?? and minimziing is black?
    def minimax_root(self, depth, board):
        possible_moves = self.rule_set.find_all_legal_moves(board, self.color)
        best_boardstate_value = -9999
        best_moves = []
        for move in possible_moves:
            (s1, s2) = move
            new_board = board.make_move(s1, s2)
            value = max(best_boardstate_value, self.minimax(depth, new_board, -10000, 10000, self.color=="White"))
            if value == best_boardstate_value:
                best_moves.append(move)
            elif value > best_boardstate_value:
                best_boardstate_value = value
                best_moves.clear()
                best_moves.append(move)
        print("Value of best moves: " + str(value))
        print("Number of best moves: " + str(len(best_moves)))
        print(best_moves)
        #randomly select a best move and return it
        return random.choice(best_moves)

    def minimax(self, depth, board, alpha, beta, is_maximizing):
        if is_maximizing:
            turn = self.color
        else:
            turn = self.enemy
        if depth == 0:
            self.n = self.n + 1
            return -self.evaluate_board(board)
        possible_moves = self.rule_set.find_all_legal_moves(board, turn)
        if is_maximizing:
            best_move = -9999
            for move in possible_moves:
                (s1, s2) = move
                child_board = board.make_move(s1, s2)
                best_move = max(best_move, self.minimax(depth-1, child_board, alpha, beta, False))
                alpha = max(alpha, best_move)
                if beta <= alpha:
                    return best_move
            return best_move
        else:
            best_move = 9999
            for move in possible_moves:
                (s1, s2) = move
                child_board = board.make_move(s1, s2)
                best_move = min(best_move, self.minimax(depth-1, child_board, alpha, beta, True))
                beta = min(beta, best_move)
                if beta <= alpha:
                    return best_move
            return best_move
