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
            #Case 3.5 Leftward EnPassant
            if color == "Black" and board.hasColorPiece("White",chr(s2l)+"4"):
                if board.getPiece(chr(s2l)+"4").name == "Pawn":
                    return board.getPiece(chr(s2l)+"4").justMoved2
            elif color == "White" and board.hasColorPiece("Black",chr(s2l)+"5"):
                if board.getPiece(chr(s2l)+"5").name == "Pawn":
                    return board.getPiece(chr(s2l)+"5").justMoved2
        #Case 4: Rightward Capturing
        if s1l == s2l+1 and s1n == (s2n - move):
            if color == "Black" and board.hasColorPiece("White",s2):
                return True
            elif color == "White" and board.hasColorPiece("Black",s2):
                return True
            if color == "Black" and board.hasColorPiece("White",chr(s2l)+"4"):
                if board.getPiece(chr(s2l)+"4").name == "Pawn":
                    return board.getPiece(chr(s2l)+"4").justMoved2
            elif color == "White" and board.hasColorPiece("Black",chr(s2l)+"5"):
                if board.getPiece(chr(s2l)+"5").name == "Pawn":
                    return board.getPiece(chr(s2l)+"5").justMoved2
            #Case 4.5 Rightward EnPassant
        return False


    #Logic for legal King move
    def validateKing(self,board,s1,s2,color):
        s1l = ord(s1[0])
        s2l = ord(s2[0])
        s1n = int(s1[1])
        s2n = int(s2[1])
        #Check if castle, and if you can castle.
        if (color == "White" and board.whiteCastle == False ) or (color == "Black" and board.blackCastle == False):
            if(color == "White" and s2 == "c1"):
                if not (self.isInCheck(board,color,"c1") or self.isInCheck(board,color,"d1") or self.isInCheck(board,color,"e1")):
                    if not( board.hasAnyPiece("b1") and board.hasAnyPiece("c1") and board.hasAnyPiece("d1")):
                        return True
            elif(color == "White" and s2 == "g1"):
                if not (self.isInCheck(board,color,"e1") or self.isInCheck(board,color,"f1") or self.isInCheck(board,color,"g1")):
                    if not( board.hasAnyPiece("f1") and board.hasAnyPiece("g1") ):
                        return True
            elif(color == "Black" and s2 == "c8"):
                if not (self.isInCheck(board,color,"c8") or self.isInCheck(board,color,"d8") or self.isInCheck(board,color,"e8")):
                    if not( board.hasAnyPiece("b8") and board.hasAnyPiece("c8") and board.hasAnyPiece("d8")):
                        return True
            elif(color == "Black" and s2 == "g8"):
                if not (self.isInCheck(board,color,"e8") or self.isInCheck(board,color,"f8") or self.isInCheck(board,color,"g8")):
                    if not( board.hasAnyPiece("f8") and board.hasAnyPiece("g8") ):
                        return True
        #Normal Move
        if abs(s1l-s2l) <= 1 and abs(s1n-s2n) <= 1:
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
                if i == s2n:
                    return True
                if board.hasAnyPiece(chr(s1l)+str(i)):
                    return False
        #Case 2: Downwards Movement
        if s1l==s2l and s1n>s2n:
            i=s1n
            while i>s2n:
                i = i-1
                if i == s2n:
                    return True
                if board.hasAnyPiece(chr(s1l)+str(i)):
                    return False
        #Case 3: Rightwards Movement
        if s1n==s2n and s1l<s2l:
            i= s1l
            while i<s2l:
                i = i+1
                if i == s2l:
                    return True
                if board.hasAnyPiece(chr(i)+str(s1n)):
                    return False
        #Case 4: Leftward Movement
        if s1n==s2n and s1l>s2l:
            i= s1l
            while i>s2l:
                i = i-1
                if i == s2l:
                    return True
                if board.hasAnyPiece(chr(i)+str(s1n)):
                    return False
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
                    if i== s2l and j==s2n:
                        return True
                    if board.hasAnyPiece(chr(i)+str(j)):
                        return False
            #Case 2: Downright movement
            if s1l<s2l and s1n>s2n:
                i= s1l
                j = s1n
                while i<s2l and j>s2n:
                    i = i+1
                    j = j-1
                    if i== s2l and j==s2n:
                        return True
                    if board.hasAnyPiece(chr(i)+str(j)):
                        return False
            #Case 3: Upleft movement
            if s1l>s2l and s1n<s2n:
                i= s1l
                j = s1n
                while i>s2l and j<s2n:
                    i = i-1
                    j = j+1
                    if i== s2l and j==s2n:
                        return True
                    if board.hasAnyPiece(chr(i)+str(j)):
                        return False
            #Case 4: Downleft movement
            if s1l>s2l and s1n>s2n:
                i= s1l
                j = s1n
                while i>s2l and j>s2n:
                    i = i-1
                    j = j-1
                    if i== s2l and j==s2n:
                        return True
                    if board.hasAnyPiece(chr(i)+str(j)):
                        return False
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
                if abs(ord(piece.square[0]) - ord(kingSquare[0])) == 1 and abs( int(piece.square[1]) - int(kingSquare[1])) == 1:
                    return True
        return False

    def validSquare(self,square):
        ltr = square[0]
        num = square[1]
        if ltr in "abcdefgh" and num in "12345678":
            return True
        return False

    def findLegalMoves(self,board,location):
        moves = []
        if not board.hasAnyPiece(location):
            return moves
        else:
            p = board.getPiece(location)
        for letter in "abcdefgh":
            for num in "12345678":
                sqr = letter + num
                if self.validateMove(p.name,p.color,p.color,board,location,sqr):
                    moves.append(sqr)
        return moves

    def findAllLegalMoves(self,board,color):
        moves = []
        if color == "White":
            pieces = board.getWhitePieces()
        else:
            pieces = board.getBlackPieces()
        for piece in pieces:
            pieceMoves = self.findLegalMoves(board,piece.square)
            for move in pieceMoves:
                if piece.name == "Knight":
                    moves.append("N" + move)
                elif piece.name == "Pawn":
                    moves.append(move)
                else:
                    moves.append(piece.name[0] + move)
        return moves


