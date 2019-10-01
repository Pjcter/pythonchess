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
        if(pcolor != turn):
            return False
        #Check if s2 is a legal square on the board

        #Check if your king is now in check

        #Check if the board has the piece
        if(board.hasPiece(piece,pcolor,s1)):
            if(piece==Pawn):
                return self.validatePawn(board,s1,s2,pcolor)
            elif(piece==King):
                return self.validateKing(board,s1,s2,pcolor)
            elif(piece==Queen):
                return self.validateQueen(board,s1,s2,pcolor)
            elif(piece==Knight):
                return self.validateKnight(board,s1,s2,pcolor)
            elif(piece==Bishop):
                return self.validateBishop(board,s1,s2,pcolor)
            elif(piece==Rook):
                return self.validateRook(board,s1,s2,pcolor)
            else:
                print("Invalid piece name given to validateMove")
                return False
        return False

    #Logic for legal Pawn move
    def validatePawn(self,board,s1,s2,color):
        s1l = ord(s1[0])
        s2l = ord(s2[0])
        s1n = int(s1[1])
        s2n = int(s2[1])
        if(color == "White"):
            move = 1
        elif(color == "Black"):
            move = -1
        #Check if s2 is forward moving
        if(s1l == s2l and s1n == (s2n-move)):
            #Check if there's no piece in the way
            if(board.board[s2].piece==None):
                return True
        #Check if s2 is left taking
        if(s1l == s2l-1 and s1n == (s2n-move)):
            #Check if there's a piece in the way
            if(board.board[s2].piece!=None):
                #Check if piece is opposite to this color
                    if(board.board[s2].piece.color != color):
                        return True
            #Check if its an en-passant

        #Check if s2 is right taking
    #Logic for legal King move
    def validateKing(self,board,s1,s2):
    #Logic for legal Rook move
    def validateRook(self,board,s1,s2):
    #Logic for legal Queen move
    def validateQueen(self,board,s1,s2):
    #Logic for legal Bishop move
    def validateBishop(self,board,s1,s2):
    #Logic for legal Knight move
    def validateKnight(self,board,s1,s2):
    #Logic for legal Castle move
    def validateCastle(self,board,s1,s2):


    def validSquare(self,square):
        ltr = square[0]
        num = square[1]
        if ltr in "ABCDEFGH" and num in (1,2,3,4,5,6,7,8):
            return True
        return False

