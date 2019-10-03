from src.main.model.Board import *
from src.main.model.Pieces import *

class RuleSet:
    'This class is responsible for determining if a given board state is valid'

    #Logic for validating a move.
    #Piece: The piece that is being moved
    #PColor: The color of the piece
    #Turn: The current turn of the game, either "White" or "Black"
    #Board: The current board state of the game
    #S1: The origin square of the move
    #S2: The destination square of the move
    def validateMove(self, piece, pcolor, turn, board, s1, s2):
        #Check if its this pieces turn
        if pcolor != turn:
            return False
        #Check if s2 is a legal square on the board
        if self.validSquare(s1) and self.validSquare(s2):
            pass
        else:
            return False
        #Check if s2 contains a friendly piece on it
        if (pcolor == "White" and board.hasColorPiece("White", s2)) or (pcolor == "Black" and board.hasColorPiece("Black", s2)):
            return False
        #Check if your king is now in check
        # to do this, iterate through all enemy pieces and see if they can move to where your king is.

        #Check if the piece can move there at all
        if board.hasGivenPiece(piece, pcolor, s1):
            if piece==Pawn:
                if not self.validatePawn(board,s1,s2,pcolor):
                    return False
            elif piece==King:
                if not self.validateKing(board,s1,s2,pcolor):
                    return False
            elif piece==Queen:
                if not self.validateQueen(board,s1,s2):
                    return False
            elif piece==Knight:
                if not self.validateKnight(board,s1,s2):
                    return False
            elif piece==Bishop:
                if not self.validateBishop(board,s1,s2):
                    return False
            elif piece==Rook:
                if not self.validateRook(board,s1,s2):
                    return False
        mockBoard = board.makeMove(s1,s2)
        #If king is not in check after move, this is a valid move!
        return not self.isInCheck(mockBoard,pcolor,mockBoard.kingLocation(pcolor))

    #Rules for legal Pawn move
    def validatePawn(self,board,s1,s2,color):
        s1l = ord(s1[0])
        s2l = ord(s2[0])
        s1n = int(s1[1])
        s2n = int(s2[1])
        if color == "White":
            move = 1
        elif color == "Black":
            move = -1
        #Case 1: Moving Forward Once
        if s1l == s2l and s1n == (s2n - move):
            if not board.hasAnyPiece(s2):
                return True
        #Case 2: Moving Forward Twice
        if s1l == s2l and s1n == (s2n - (2 * move)):
            if not board.hasAnyPiece(s2) and not board.hasAnyPiece(chr(s1l)+str(s2n-move)):
                    if(color == "White" and s1[1] == "2" ) or (color == "Black" and s1[1] == "7"):
                        return True
        #Case 3: Leftward Capturing
        if s1l == s2l-1 and s1n == (s2n - move):
            if color == "Black" and board.hasColorPiece("White",s2):
                return True
            elif color == "White" and board.hasColorPiece("Black",s2):
                return True
        #Case 4: Rightward Capturing
        if s1l == s2l+1 and s1n == (s2n - move):
            if color == "Black" and board.hasColorPiece("White",s2):
                return True
            elif color == "White" and board.hasColorPiece("Black",s2):
                return True
        return False


    #Logic for legal King move
    def validateKing(self,board,s1,s2,color):
        s1l = ord(s1[0])
        s2l = ord(s2[0])
        s1n = int(s1[1])
        s2n = int(s2[1])
        #Check if castle, and if you can castle.

        #Normal Move
        if (abs(s1l-s2l) + abs(s1n-s2n)) <= 1 and (abs(s1l-s2l) + abs(s1n-s2n)) > 0:
            return True
        return False

    #Logic for legal Rook move
    def validateRook(self,board,s1,s2):
        s1l = ord(s1[0])
        s2l = ord(s2[0])
        s1n = int(s1[1])
        s2n = int(s2[1])
        #Case 1: Upwards Movement
        if s1l==s2l and s1n<s2n:
            i=s1n
            while i<s2n:
                if board.hasAnyPiece(chr(s1l)+str(i)):
                    return False
                i = i+1
            return True
        #Case 2: Downwards Movement
        if s1l==s2l and s1n>s2n:
            i=s1n
            while i>s2n:
                if board.hasAnyPiece(chr(s1l)+str(i)):
                    return False
                i = i-1
            return True
        #Case 3: Rightwards Movement
        if s1n==s2n and s1l<s2l:
            i= s1l
            while i<s2l:
                if board.hasAnyPiece(chr(i)+int(s1n)):
                    return False
                i = i+1
            return True
        #Case 4: Leftward Movement
        if s1n==s2n and s1l>s2l:
            i= s1l
            while i>s2l:
                if board.hasAnyPiece(chr(i)+int(s1n)):
                    return False
                i = i-1
            return True
        return False


    #Logic for legal Queen move
    def validateQueen(self,board,s1,s2):
        return self.validateBishop(board,s1,s2) or self.validateRook(board,s1,s2)

    #Logic for legal Bishop move
    def validateBishop(self,board,s1,s2):
        s1l = ord(s1[0])
        s2l = ord(s2[0])
        s1n = int(s1[1])
        s2n = int(s2[1])
        if (s1l-s2l) == (s1n-s2n):
            #Case 1: Upright movement
            if s1l<s2l and s1n<s2n:
                i= s1l, j = s1n
                while i<s2l and j<s2n:
                    if board.hasAnyPiece(chr(i)+int(j)):
                        return False
                    i = i+1
                    j = j+1
                return True
            #Case 2: Downright movement
            if s1l<s2l and s1n>s2n:
                i= s1l, j = s1n
                while i<s2l and j>s2n:
                    if board.hasAnyPiece(chr(i)+int(j)):
                        return False
                    i = i+1
                    j = j-1
                return True
            #Case 3: Upleft movement
            if s1l>s2l and s1n<s2n:
                i= s1l, j = s1n
                while i>s2l and j<s2n:
                    if board.hasAnyPiece(chr(i)+int(j)):
                        return False
                    i = i-1
                    j = j+1
                return True
            #Case 4: Downleft movement
            if s1l>s2l and s1n>s2n:
                i= s1l, j = s1n
                while i>s2l and j>s2n:
                    if board.hasAnyPiece(chr(i)+int(j)):
                        return False
                    i = i-1
                    j = j-1
                return True
        return False

    #Logic for legal Knight move
    def validateKnight(self,board,s1,s2):
        s1l = ord(s1[0])
        s2l = ord(s2[0])
        s1n = int(s1[1])
        s2n = int(s2[1])
        #Case 1: Vertical 2, Horizontal 1
        if abs(s1n-s2n)==2 and abs(s1l-s2l)==1:
            return True
        #Case 2: Horizontal 1, Vertical 2
        if abs(s1n-s2n)==1 and abs(s1l-s2l)==2:
            return True
        return False

    def isInCheck(self,board,color,kingSquare):
        enemyPieces = []
        if color == "White":
            enemyPieces = board.getBlackPieces()
            enemyColor = "Black"
        else:
            enemyPieces = board.getWhitePieces()
            enemyColor = "White"
        for piece in enemyPieces:
            if piece.name == "Pawn":
                if self.validatePawn(board,piece.square,kingSquare,enemyColor):
                    return True
            elif piece.name == "Rook":
                if self.validateRook(board,piece.square,kingSquare):
                    return True
            elif piece.name == "Bishop":
                if self.validateBishop(board,piece.square,kingSquare):
                    return True
            elif piece.name == "Knight":
                if self.validateKnight(board,piece.square,kingSquare):
                    return True
            elif piece.name == "Queen":
                if self.validateQueen(board,piece.square,kingSquare):
                    return True
            else:
                if (abs( ord(piece.square[0]) - ord(kingSquare[0])) == 1) or (abs( int(piece.square[1] - int(kingSquare[1]))) == 1):
                    return True
        return False

    def validSquare(self,square):
        ltr = square[0]
        num = square[1]
        if ltr in "ABCDEFGH" and num in (1,2,3,4,5,6,7,8):
            return True
        return False

