from src.main.model.Board import *
from src.main.model.RuleSet import *

class Game:
    'Representation of a game of chess'

    def __init__(self):
        self.board = Board()
        self.ruleSet = RuleSet()
        self.turn = "White"
        self.gameOver = False
        self.winner = None

