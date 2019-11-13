import tkinter as tk
from PIL import ImageTk

from src.main.model.Game import Game

# Constant Declarations

SCALE_MULTIPLIER = 1;
SQUARESIZE = 50*SCALE_MULTIPLIER;

class ChessApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self,*args,**kwargs)

        #Create Main Window
        window = tk.Frame(self)
        window.pack(side="top", fill = "both", expand = True)
        window.rowconfigure(0,weight=1)
        window.columnconfigure(0,weight=1)
        self.minsize(8*SQUARESIZE,8*SQUARESIZE)
        self.maxsize(8*SQUARESIZE,8*SQUARESIZE)
        self.wm_title("Chess")
        self.iconphoto(self,ImageTk.PhotoImage(file=".\img\\blkKing.png"))
        self.center()

        #Initialize Scenes
        self.scenes = {}
        self.scenes[ChessGUI] = ChessGUI(window, self)
        self.show_scene(ChessGUI)

    def center(win):
        win.update_idletasks()
        width = win.winfo_width()
        height = win.winfo_height()
        x = (win.winfo_screenwidth() // 2) - (width // 2)
        y = (win.winfo_screenheight() // 2) - (height // 2)
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y-100))

    def show_scene(self,cont):
        scene = self.scenes[cont]
        #TODO: redraw scene on top


#This is a Canvas scene that represents a game of chess.
class ChessGUI(tk.Canvas):
    def __init__(self,parent,controller):
        tk.Canvas.__init__(self,parent)
        self.grid(row=0,column=0,sticky="nsew")
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
        letter = chr(x_coord+97)
        num = str(8-y_coord)
        square = letter+num
        if self.lastClicked == None:
            if self.game.board.hasColorPiece(self.game.turn,square):
                self.lastClicked = square
                img = ImageTk.PhotoImage(file=".\img\highlight.png")
                self.create_image(SQUARESIZE*x_coord,SQUARESIZE*y_coord,image=img,anchor=tk.NW)
                self.lastHighlight = img
        elif self.lastClicked != None:
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
        #Delete Old Images
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
            if piece.color == "White":
                img = ImageTk.PhotoImage(file =(".\img\\wht"+piece.name+".png"))
            else:
                img = ImageTk.PhotoImage(file =(".\img\\blk"+piece.name+".png"))
            x_coord = ord(piece.square[0]) - 97
            y_coord = 8 - int(piece.square[1])
            self.create_image(SQUARESIZE*x_coord, SQUARESIZE*y_coord,image=img,anchor=tk.NW)
            self.imgs.append(img)

app = ChessApplication()
app.mainloop()


