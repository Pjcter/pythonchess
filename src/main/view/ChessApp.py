import tkinter as tk

from src.main.model.Game import Game

LARGE_FONT = ("Calibri", 12)


class ChessApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        self.frames = {}
        for F in (ChessGUI, OpeningScreen):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.showFrame(OpeningScreen)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class OpeningScreen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        startBtn = tk.Button(self, text="New Game", font=LARGE_FONT)
        startBtn.pack()
        loadBtn = tk.Button(self, text="Load Game")
        loadBtn.pack()


class ChessGUI(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.canvs = []
        self.game = Game()
        for sqr in self.game.board.squares:
            if sqr.color == "Black":
                img = tk.PhotoImage(file="black_square.png")
            else:
                img = tk.PhotoImage(file="white_square.png")
            canv = tk.Canvas(self, image=img)
            canv.place(y=9-int(sqr.num), x=ord(sqr.letter)-ord('a'))