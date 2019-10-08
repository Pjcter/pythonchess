from src.main.model.Game import *
def __main__():
    game = Game()
    while True:
        print(game.board.toString())
        print(game.turn + "'s Turn!")
        #print(game.ruleSet.findAllLegalMoves(game.board,game.turn))
        if(game.isChecked(game.turn)):
            print("CHECK!")
        inpt = input("Enter move as: \"[Piece] [From] [To]\": ")
        info = inpt.split(" ")
        if info == "Q" or info.__len__() != 3:
            break
        piece = info[0]
        s1 = info[1]
        s2 = info[2]
        if game.board.hasGivenPiece(piece, game.turn, s1):
            if game.ruleSet.validateMove(piece, game.turn, game.turn, game.board, s1, s2):
                game.board = game.board.makeMove(s1, s2)
                print("Move made!")
                game.changeTurn()
            else:
                print("Move failed!")
        else:
            print("Invalid input!")
    print("Exiting Chess!")

__main__()