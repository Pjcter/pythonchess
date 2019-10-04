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
        if pcolor != turn:
            return False
        if not(self.validSquare(s1) and self.validSquare(s2)):
            print("Error, invalid square given to validateMove")
            return False
        if (pcolor == "White" and board.hasColorPiece("White", s2)) or (pcolor == "Black" and board.hasColorPiece("Black", s2)):
            return False
        if board.hasGivenPiece(piece, pcolor, s1):
            if piece=="Pawn":
                if not self.validatePawn(board,s1,s2,pcolor):
                    return False
            elif piece=="King":
                if not self.validateKing(board,s1,s2,pcolor):
                    return False
            elif piece=="Queen":
                if not self.validateQueen(board,s1,s2):
                    return False
            elif piece=="Knight":
                if not self.validateKnight(board,s1,s2):
                    return False
            elif piece=="Bishop":
                if not self.validateBishop(board,s1,s2):
                    return False
            elif piece=="Rook":
                if not self.validateRook(board,s1,s2):
                    return False
            else:
                print("Error: invalid move request")
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
        if (color == "White" and board.whiteCastle == False ) or (color == "Black" and board.blackCastle == False):
            if(color == "White" and s2 == "C1"):
                if not (self.isInCheck(board,color,"C1") and self.isInCheck(board,color,"D1") and self.isInCheck(board,color,"E1")):
                    if not( board.hasAnyPiece("B1") and board.hasAnyPiece("C1") and board.hasAnyPiece("D1")):
                        return True
            elif(color == "White" and s2 == "G1"):
                if not (self.isInCheck(board,color,"E1") and self.isInCheck(board,color,"F1") and self.isInCheck(board,color,"G1")):
                    if not( board.hasAnyPiece("F1") and board.hasAnyPiece("G1") ):
                        return True
            elif(color == "Black" and s2 == "C8"):
                if not (self.isInCheck(board,color,"C8") and self.isInCheck(board,color,"D8") and self.isInCheck(board,color,"E8")):
                    if not( board.hasAnyPiece("B8") and board.hasAnyPiece("C8") and board.hasAnyPiece("D8")):
                        return True
            elif(color == "Black" and s2 == "G8"):
                if not (self.isInCheck(board,color,"E8") and self.isInCheck(board,color,"F8") and self.isInCheck(board,color,"G8")):
                    if not( board.hasAnyPiece("F8") and board.hasAnyPiece("G8") ):
                        return True
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
                i = i+1
                if board.hasAnyPiece(chr(s1l)+str(i)):
                    return False
            return True
        #Case 2: Downwards Movement
        if s1l==s2l and s1n>s2n:
            i=s1n
            while i>s2n:
                i = i-1
                if board.hasAnyPiece(chr(s1l)+str(i)):
                    return False
            return True
        #Case 3: Rightwards Movement
        if s1n==s2n and s1l<s2l:
            i= s1l
            while i<s2l:
                i = i+1
                if board.hasAnyPiece(chr(i)+str(s1n)):
                    return False
            return True
        #Case 4: Leftward Movement
        if s1n==s2n and s1l>s2l:
            i= s1l
            while i>s2l:
                i = i-1
                if board.hasAnyPiece(chr(i)+str(s1n)):
                    return False
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
        if abs((s1l-s2l)) == abs((s1n-s2n)):
            #Case 1: Upright movement
            if s1l<s2l and s1n<s2n:
                i= s1l
                j = s1n
                while i<s2l and j<s2n:
                    i = i+1
                    j = j+1
                    if board.hasAnyPiece(chr(i)+str(j)):
                        return False
                return True
            #Case 2: Downright movement
            if s1l<s2l and s1n>s2n:
                i= s1l
                j = s1n
                while i<s2l and j>s2n:
                    i = i+1
                    j = j-1
                    if board.hasAnyPiece(chr(i)+str(j)):
                        print("Piece in the way")
                        return False
                return True
            #Case 3: Upleft movement
            if s1l>s2l and s1n<s2n:
                i= s1l
                j = s1n
                while i>s2l and j<s2n:
                    i = i-1
                    j = j+1
                    if board.hasAnyPiece(chr(i)+str(j)):
                        return False
                return True
            #Case 4: Downleft movement
            if s1l>s2l and s1n>s2n:
                i= s1l
                j = s1n
                while i>s2l and j>s2n:
                    i = i-1
                    j = j-1
                    if board.hasAnyPiece(chr(i)+str(j)):
                        return False
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
                if abs(ord(piece.square[0]) - ord(kingSquare[0])) == 1 or abs( int(piece.square[1]) - int(kingSquare[1])) == 1:
                    return True
        return False

    def validSquare(self,square):
        ltr = square[0]
        num = square[1]
        if ltr in "ABCDEFGH" and num in "12345678":
            return True
        return False

