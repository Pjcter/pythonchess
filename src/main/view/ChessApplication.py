import tkinter as tk

from src.main.model.Game import Game

LARGE_FONT = ("Calibri", 12)

class ChessApplication(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self,*args,**kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill = "both", expand = True)

        container.rowconfigure(0,weight=1)
        container.columnconfigure(0,weight=1)

        self.frames = {}

        for F in (ChessGUI, OpeningScreen):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")




        self.show_frame(ChessGUI)

    def show_frame(self,cont):

        frame = self.frames[cont]
        frame.tkraise()


class ChessGUI(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.imgs = []
        self.game = Game()
        for sqr in self.game.board.squares:
            if sqr.color == "Black":
                img = tk.PhotoImage(file = "black_square.png")
            else:
                img = tk.PhotoImage(file = "white_square.png")
            label = tk.Label(self,image=img)
            label.place(y = 9 - int(sqr.num) , x =ord(sqr.letter) - 64)
            self.imgs.append(img)
        self.play()

    def play(self):
            self.redraw()

    def redraw(self):
        for piece in self.game.board.pieces:
            if piece.name == "Pawn" and piece.color == "White":
                img = tk.PhotoImage(file = "whtPawn.png")
            elif piece.name == "Pawn" and piece.color == "Black":
                img = tk.PhotoImage(file = "blkPawn.png")
            elif piece.name == "Knight" and piece.color == "White":
                img = tk.PhotoImage(file = "whtKnight.png")
            elif piece.name == "Knight" and piece.color == "Black":
                img = tk.PhotoImage(file = "blkKnight.png")
            elif piece.name == "Bishop" and piece.color == "White":
                img = tk.PhotoImage(file = "whtBishop.png")
            elif piece.name == "Bishop" and piece.color == "Black":
                img = tk.PhotoImage(file = "blkBishop.png")
            elif piece.name == "Rook" and piece.color == "White":
                img = tk.PhotoImage(file = "whtRook.png")
            elif piece.name == "Rook" and piece.color == "Black":
                img = tk.PhotoImage(file = "blkRook.png")
            elif piece.name == "King" and piece.color == "White":
                img = tk.PhotoImage(file = "whtKing.png")
            elif piece.name == "King" and piece.color == "Black":
                img = tk.PhotoImage(file = "blkKing.png")
            elif piece.name == "Queen" and piece.color == "White":
                img = tk.PhotoImage(file = "whtQueen.png")
            elif piece.name == "Queen" and piece.color == "Black":
                img = tk.PhotoImage(file="blkQueen.png")

            canv = tk.Canvas(tk, width=100, height=100)
            canv.create_image(50, 50, img)
            canv.place(y = (8 - int(piece.square[1]))*100, x = 100*(ord(piece.square[0]) - 97))
            self.imgs.append(img)

class OpeningScreen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        startBtn = tk.Button(self, text="New Game", font=LARGE_FONT)
        startBtn.pack()
        loadBtn = tk.Button(self, text="Load Game")
        loadBtn.pack()


app = ChessApplication()
app.mainloop()


