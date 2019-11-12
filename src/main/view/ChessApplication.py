import tkinter as tk
from tkinter import Canvas
from PIL import Image, ImageTk

from src.main.model.Game import Game

# Constant Declarations

SCALE_MULTIPLIER = 1;
SQUARESIZE = 50*SCALE_MULTIPLIER;

class ChessApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill = "both", expand = True)
        container.rowconfigure(0,weight=1)
        container.columnconfigure(0,weight=1)
        menubar = tk.Menu(self)
        options = tk.Menu(menubar,tearoff=0)
        options.add_command(label="Draw")
        options.add_command(label="Quit")
        help = tk.Menu(menubar,tearoff=0)
        help.add_command(label="Cheat")
        menubar.add_cascade(label="Options",menu=options)
        menubar.add_cascade(label="Help",menu=help)
        self.config(menu=menubar)
        self.canvases = {}
        self.minsize(400,400)
        self.maxsize(400,400)
        canvas = ChessGUI(container, self)
        self.canvases[ChessGUI] = canvas
        canvas.grid(row=0,column=0,sticky="nsew")
        self.show_canvas(ChessGUI)
        self.wm_title("Chess")
        self.iconphoto(self,ImageTk.PhotoImage(file=".\img\\blkKing.png"))
        self.center()

    def center(win):
        win.update_idletasks()
        width = win.winfo_width()
        height = win.winfo_height()
        x = (win.winfo_screenwidth() // 2) - (width // 2)
        y = (win.winfo_screenheight() // 2) - (height // 2)
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y-100))

    def show_canvas(self,cont):
        canvas = self.canvases[cont]

class ChessGUI(tk.Canvas):

    def __init__(self,parent,controller):
        tk.Canvas.__init__(self,parent)
        self.imgs = []
        self.game = Game()
        self.lastClicked = None
        self.lastHighlight = None
        self.bind("<Button-1>",self.handle_click)
        self.redraw()

    def handle_click(self,event):
        x_coord = int(event.x / SQUARESIZE)
        y_coord = int(event.y / SQUARESIZE)
        #Translate coords to squares
        letter = chr(x_coord + 97)
        num = str(8- y_coord)
        square = letter+num
        if self.lastClicked == None:
            if self.game.board.hasAnyPiece(square):
                self.lastClicked = square
                img = ImageTk.PhotoImage(file=".\img\highlight.png")
                self.create_image(SQUARESIZE*x_coord,SQUARESIZE*y_coord,image=img,anchor=tk.NW)
                self.lastHighlight = img
        elif self.lastClicked != None:
            #something has already been clicked!
            if self.game.board.hasColorPiece(self.game.turn,self.lastClicked):
                pieceName = self.game.board.getPiece(self.lastClicked).name
                if self.game.ruleSet.validateMove(pieceName,self.game.turn,self.game.turn,self.game.board,self.lastClicked,square):
                    self.game.board = self.game.board.makeMove(self.lastClicked,square)
                    self.lastHighlight = None
                    self.redraw()
                    self.game.changeTurn()
                self.lastClicked = None
            if self.game.board.hasAnyPiece(square):
                self.lastClicked = square
                img = ImageTk.PhotoImage(file=".\img\highlight.png")
                self.create_image(SQUARESIZE * x_coord, SQUARESIZE * y_coord, image=img, anchor=tk.NW)
                self.lastHighlight = img

    def redraw(self):
        self.imgs.clear()
        #Redraw Squares
        for sqr in self.game.board.squares:
            if sqr.color == "Black":
                img = ImageTk.PhotoImage(file = ".\img\\black_square.png")
            else:
                img = ImageTk.PhotoImage(file = ".\img\\white_square.png")
            self.create_image(SQUARESIZE*sqr.x_coord, SQUARESIZE*sqr.y_coord,image=img,anchor=tk.NW)
            self.imgs.append(img)
        #Redraw Pieces
        for piece in self.game.board.pieces:
            if piece.name == "Pawn" and piece.color == "White":
                img = ImageTk.PhotoImage(file=".\img\\whtPawn.png")
            if piece.name == "Pawn" and piece.color == "Black":
                img = ImageTk.PhotoImage(file=".\img\\blkPawn.png")
            if piece.name == "Knight" and piece.color == "White":
                img = ImageTk.PhotoImage(file=".\img\\whtKnight.png")
            if piece.name == "Knight" and piece.color == "Black":
                img = ImageTk.PhotoImage(file=".\img\\blkKnight.png")
            if piece.name == "Bishop" and piece.color == "White":
                img = ImageTk.PhotoImage(file=".\img\\whtBishop.png")
            if piece.name == "Bishop" and piece.color == "Black":
                img = ImageTk.PhotoImage(file=".\img\\blkBishop.png")
            if piece.name == "Rook" and piece.color == "White":
                img = ImageTk.PhotoImage(file=".\img\\whtRook.png")
            if piece.name == "Rook" and piece.color == "Black":
                img = ImageTk.PhotoImage(file=".\img\\blkRook.png")
            if piece.name == "King" and piece.color == "White":
                img = ImageTk.PhotoImage(file=".\img\\whtKing.png")
            if piece.name == "King" and piece.color == "Black":
                img = ImageTk.PhotoImage(file=".\img\\blkKing.png")
            if piece.name == "Queen" and piece.color == "White":
                img = ImageTk.PhotoImage(file=".\img\\whtQueen.png")
            if piece.name == "Queen" and piece.color == "Black":
                img = ImageTk.PhotoImage(file=".\img\\blkQueen.png")
            x_coord = ord(piece.square[0]) - 97
            y_coord = 8 - int(piece.square[1])
            self.create_image(SQUARESIZE*x_coord, SQUARESIZE*y_coord,image=img,anchor=tk.NW)
            self.imgs.append(img)


app = ChessApplication()
app.mainloop()


