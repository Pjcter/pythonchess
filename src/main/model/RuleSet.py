class RuleSet:
    """Represents the rules of chess. Can be used to validate a move, or find all legal moves"""

    def validate_move(self, p_name, p_color, turn, board, s1, s2):
        """Logic for validating a generic move"""
        if p_color != turn or not self.valid_square(s1) or not self.valid_square(s2) or board.has_color_piece(p_color, s2):
            return False
        if board.has_given_piece(p_name, p_color, s1):
            movements = {
                "Pawn": self.validate_pawn(board, s1, s2, p_color),
                "King": self.validate_king(board, s1, s2, p_color),
                "Queen": self.validate_queen(board, s1, s2),
                "Knight": self.validate_knight(board, s1, s2),
                "Bishop": self.validate_bishop(board, s1, s2),
                "Rook": self.validate_rook(board, s1, s2),
            }
            if not movements.get(p_name):
                return False
        mock_board = board.make_move(s1, s2)
        return not self.is_in_check(mock_board, p_color, mock_board.find_king_location(p_color))

    def validate_pawn(self, board, s1, s2, color):
        s1l = ord(s1[0])
        s2l = ord(s2[0])
        s1n = int(s1[1])
        s2n = int(s2[1])
        if color == "White":
            move = 1
            enpassant_row = 6
        elif color == "Black":
            move = -1
            enpassant_row = 3
        #Case 1: Moving Forward Once
        if s1l == s2l and s1n == (s2n - move):
            if not board.has_any_piece(s2):
                return True
        #Case 2: Moving Forward Twice
        elif s1l == s2l and s1n == (s2n - (2 * move)):
            if not board.has_any_piece(s2) and not board.has_any_piece(chr(s1l) + str(s2n - move)):
                    if(color == "White" and s1[1] == "2" ) or (color == "Black" and s1[1] == "7"):
                        return True
        #Case 3: Capturing:
        elif board.has_color_piece(self.enemy_color(color), s2):
            #3.1: Left Capture
            if s1l == s2l-1 and s1n == (s2n - move):
                return True
            #3.2 Right Capture
            if s1l == s2l + 1 and s1n == (s2n - move):
                return True
        #Case 4: En-Passants:
        elif (s1l == s2l + 1 and s1n == (s2n - move)) or (s1l == s2l - 1 and s1n == (s2n - move)):
            if s2n == enpassant_row and board.has_color_piece(self.enemy_color(color), chr(s2l) + str(enpassant_row - move)):
                if board.get_piece(chr(s2l) + str(enpassant_row - move)).name == "Pawn":
                    return board.get_piece(chr(s2l) + str(enpassant_row - move)).just_moved_2
        return False

    def validate_king(self, board, s1, s2, color):
        s1l = ord(s1[0])
        s2l = ord(s2[0])
        s1n = int(s1[1])
        s2n = int(s2[1])
        #Check if castle, and if you can castle.
        if (color == "White" and not board.white_castle) or (color == "Black" and not board.black_castle):
            if color == "White" and s2 == "c1":
                if not (self.is_in_check(board, color, "c1") or self.is_in_check(board, color, "d1") or self.is_in_check(board, color, "e1")):
                    if not(board.has_any_piece("b1") or board.has_any_piece("c1") or board.has_any_piece("d1")):
                        return True
            elif color == "White" and s2 == "g1":
                if not (self.is_in_check(board, color, "e1") or self.is_in_check(board, color, "f1") or self.is_in_check(board, color, "g1")):
                    if not(board.has_any_piece("f1") or board.has_any_piece("g1")):
                        return True
            elif color == "Black" and s2 == "c8":
                if not (self.is_in_check(board, color, "c8") or self.is_in_check(board, color, "d8") or self.is_in_check(board, color, "e8")):
                    if not(board.has_any_piece("b8") or board.has_any_piece("c8") or board.has_any_piece("d8")):
                        return True
            elif color == "Black" and s2 == "g8":
                if not (self.is_in_check(board, color, "e8") or self.is_in_check(board, color, "f8") or self.is_in_check(board, color, "g8")):
                    if not(board.has_any_piece("f8") or board.has_any_piece("g8")):
                        return True
        #Normal Move
        if abs(s1l-s2l) <= 1 and abs(s1n-s2n) <= 1:
            return True
        return False

    def validate_rook(self, board, s1, s2):
        s1l = ord(s1[0])
        s2l = ord(s2[0])
        s1n = int(s1[1])
        s2n = int(s2[1])
        #Case 1: Upwards Movement
        if s1l==s2l and s1n<s2n:
            i=s1n
            while i<s2n:
                i = i+1
                if i == s2n:
                    return True
                if board.has_any_piece(chr(s1l) + str(i)):
                    return False
        #Case 2: Downwards Movement
        elif s1l==s2l and s1n>s2n:
            i=s1n
            while i>s2n:
                i = i-1
                if i == s2n:
                    return True
                if board.has_any_piece(chr(s1l) + str(i)):
                    return False
        #Case 3: Rightwards Movement
        elif s1n==s2n and s1l<s2l:
            i= s1l
            while i<s2l:
                i = i+1
                if i == s2l:
                    return True
                if board.has_any_piece(chr(i) + str(s1n)):
                    return False
        #Case 4: Leftward Movement
        elif s1n==s2n and s1l>s2l:
            i= s1l
            while i>s2l:
                i = i-1
                if i == s2l:
                    return True
                if board.has_any_piece(chr(i) + str(s1n)):
                    return False
        return False

    def validate_queen(self, board, s1, s2):
        return self.validate_bishop(board, s1, s2) or self.validate_rook(board, s1, s2)

    def validate_bishop(self, board, s1, s2):
        s1l = ord(s1[0])
        s2l = ord(s2[0])
        s1n = int(s1[1])
        s2n = int(s2[1])
        if abs((s1l-s2l)) == abs((s1n-s2n)):
            #Case 1: Upright movement
            if s1l<s2l and s1n<s2n:
                i= s1l
                j = s1n
                while i<s2l and j<s2n:
                    i = i+1
                    j = j+1
                    if i== s2l and j==s2n:
                        return True
                    if board.has_any_piece(chr(i) + str(j)):
                        return False
            #Case 2: Downright movement
            elif s1l<s2l and s1n>s2n:
                i= s1l
                j = s1n
                while i<s2l and j>s2n:
                    i = i+1
                    j = j-1
                    if i== s2l and j==s2n:
                        return True
                    if board.has_any_piece(chr(i) + str(j)):
                        return False
            #Case 3: Upleft movement
            elif s1l>s2l and s1n<s2n:
                i= s1l
                j = s1n
                while i>s2l and j<s2n:
                    i = i-1
                    j = j+1
                    if i== s2l and j==s2n:
                        return True
                    if board.has_any_piece(chr(i) + str(j)):
                        return False
            #Case 4: Downleft movement
            elif s1l>s2l and s1n>s2n:
                i= s1l
                j = s1n
                while i>s2l and j>s2n:
                    i = i-1
                    j = j-1
                    if i== s2l and j==s2n:
                        return True
                    if board.has_any_piece(chr(i) + str(j)):
                        return False
        return False

    def validate_knight(self, board, s1, s2):
        s1l = ord(s1[0])
        s2l = ord(s2[0])
        s1n = int(s1[1])
        s2n = int(s2[1])
        #Case 1: Vertical 2, Horizontal 1
        if abs(s1n-s2n)==2 and abs(s1l-s2l)==1:
            return True
        #Case 2: Horizontal 1, Vertical 2
        elif abs(s1n-s2n)==1 and abs(s1l-s2l)==2:
            return True
        return False

    def is_in_check(self, board, color, kingSquare):
        enemyPieces = []
        if color == "White":
            enemyPieces = board.get_pieces("Black")
            enemyColor = "Black"
        else:
            enemyPieces = board.get_pieces("White")
            enemyColor = "White"
        for piece in enemyPieces:
            movements = {
                "Pawn": self.validate_pawn(board, piece.square, kingSquare, enemyColor),
                "King": self.validate_king(board, piece.square, kingSquare, enemyColor),
                "Queen": self.validate_queen(board, piece.square, kingSquare),
                "Knight": self.validate_knight(board, piece.square, kingSquare),
                "Bishop": self.validate_bishop(board, piece.square, kingSquare),
                "Rook": self.validate_rook(board, piece.square, kingSquare),
            }
            if movements.get(piece.name):
                return True
        return False

    def find_all_legal_moves(self, board, color):
        moves = []
        pieces = board.get_pieces(color)
        for piece in pieces:
            pieceMoves = self.find_legal_moves(board, piece.square)
            for move in pieceMoves:
                moves.append(move)
        return moves

    def find_legal_moves(self, board, location):
        moves = []
        if not board.has_any_piece(location):
            return moves
        else:
            p = board.get_piece(location)
        for letter in "abcdefgh":
            for num in "12345678":
                sqr = letter + num
                if sqr==p.square:
                    continue
                else:
                    if self.validate_move(p.name, p.color, p.color, board, location, sqr):
                        move = (p.square, sqr)
                        moves.append(move)
        return moves

    def enemy_color(self, color):
        if color == "White":
            return "Black"
        elif color == "Black":
            return "White"

    def valid_square(self, square):
        ltr = square[0]
        num = square[1]
        if ltr in "abcdefgh" and num in "12345678":
            return True
        return False



