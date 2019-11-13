import tkinter as tk
from PIL import Image,ImageTk
from winsound import *
import winsound
from src.main.model.Game import Game

# Constant Declarations
SCALE_MULTIPLIER = 1.5;
DEFAULT_SIZE = 50
SQUARESIZE = int(DEFAULT_SIZE*SCALE_MULTIPLIER);

class ChessApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self,*args,**kwargs)

        #Create Main Window
        self.window = tk.Frame(self)
        self.window.pack(side="top", fill = "both", expand = True)
        self.window.rowconfigure(0,weight=1)
        self.window.columnconfigure(0,weight=1)
        self.minsize(8*SQUARESIZE,8*SQUARESIZE + SQUARESIZE//2)
        self.maxsize(8*SQUARESIZE,8*SQUARESIZE + SQUARESIZE//2)
        self.wm_title("Chess")
        self.iconphoto(self,ImageTk.PhotoImage(file=".\img\\blkKnight.png"))

        #Initialize Scenes
        self.scenes = {}

        #For now, main page is a new game
        self.new_game()

        #Create Option Menu
        menubar = tk.Menu(self)
        menubar.add_command(label="New Game", command=self.new_game)
        aimenu = tk.Menu(menubar,tearoff=0)
        easycolormenu = tk.Menu(aimenu,tearoff=0)
        easycolormenu.add_command(label="Black")
        easycolormenu.add_command(label="White")
        hardcolormenu = tk.Menu(aimenu,tearoff=0)
        hardcolormenu.add_command(label="Black")
        hardcolormenu.add_command(label="White")
        aimenu.add_cascade(label="Easy",menu=easycolormenu)
        aimenu.add_cascade(label="Hard",menu=hardcolormenu)
        menubar.add_cascade(label="Versus AI",menu=aimenu)
        self.config(menu=menubar)
        self.center()

    def center(win):
        win.update_idletasks()
        width = win.winfo_width()
        height = win.winfo_height()
        x = (win.winfo_screenwidth() // 2) - (width // 2)
        y = (win.winfo_screenheight() // 2) - (height // 3)
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y-100))

    def show_scene(self,cont):
        scene = self.scenes[cont]
        #TODO: redraw scene on top

    def new_game(self):
        self.scenes={}
        self.scenes[ChessGUI] = ChessGUI(self.window,self)
        self.show_scene(ChessGUI)


#This is a Canvas scene that represents a game of chess.
class ChessGUI(tk.Canvas):
    def __init__(self,parent,controller):
        tk.Canvas.__init__(self,parent)
        self.grid(row=0,column=0,sticky="nsew")
        self.imgs = []
        self.game = Game()
        self.firstInput = None
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
        if self.firstInput == None:
            if self.game.board.hasColorPiece(self.game.turn,square):
                self.firstInput = square
                raw_img = Image.open(".\img\highlight.png")
                resized = raw_img.resize((SQUARESIZE,SQUARESIZE),Image.ANTIALIAS)
                img = ImageTk.PhotoImage(resized)
                self.create_image(SQUARESIZE*x_coord,SQUARESIZE*y_coord,image=img,anchor=tk.NW)
                self.lastHighlight = img
            else:
                self.lastHighlight = None
        elif self.firstInput != None:
            if self.game.board.hasColorPiece(self.game.turn,self.firstInput):
                pieceName = self.game.board.getPiece(self.firstInput).name
                if self.game.ruleSet.validateMove(pieceName,self.game.turn,self.game.turn,self.game.board,self.firstInput,square):
                    self.game.board = self.game.board.makeMove(self.firstInput,square)
                    self.firstInput = None
                    self.lastHighlight = None
                    self.game.changeTurn()
                    if(self.game.turn=="White"):
                        winsound.Beep(260,150)
                    else:
                        winsound.Beep(200,150)
                    self.redraw()
                    return
                self.lastHighlight = None
                self.firstInput = None
            if self.game.board.hasAnyPiece(square):
                self.firstInput = square
                raw_img = Image.open(".\img\highlight.png")
                resized = raw_img.resize((SQUARESIZE,SQUARESIZE),Image.ANTIALIAS)
                img = ImageTk.PhotoImage(resized)
                self.create_image(SQUARESIZE * x_coord, SQUARESIZE * y_coord, image=img, anchor=tk.NW)
                self.lastHighlight = img
            else:
                self.firstInput = None

    def redraw(self):
        #Delete Old Images
        self.imgs.clear()
        #Redraw Squares
        for sqr in self.game.board.squares:
            if sqr.color == "Black":
                raw_img = Image.open(".\img\\black_square.png")
            else:
                raw_img = Image.open(".\img\\white_square.png")
            resized = raw_img.resize((SQUARESIZE,SQUARESIZE),Image.ANTIALIAS)
            img = ImageTk.PhotoImage(resized)
            self.create_image(SQUARESIZE*sqr.x_coord, SQUARESIZE*sqr.y_coord,image=img,anchor=tk.NW)
            self.imgs.append(img)
        #Redraw Pieces
        for piece in self.game.board.pieces:
            if piece.color == "White":
                raw_img = Image.open(".\img\\wht"+piece.name+".png")
            else:
                raw_img = Image.open(".\img\\blk"+piece.name+".png")
            x_coord = ord(piece.square[0]) - 97
            y_coord = 8 - int(piece.square[1])
            resized = raw_img.resize((SQUARESIZE,SQUARESIZE),Image.ANTIALIAS)
            img = ImageTk.PhotoImage(resized)
            self.create_image(SQUARESIZE*x_coord, SQUARESIZE*y_coord,image=img,anchor=tk.NW)
            self.imgs.append(img)
        #Redraw Bottom Menu
        self.create_rectangle((0,8*SQUARESIZE,8*SQUARESIZE,8*SQUARESIZE+SQUARESIZE//2),fill="Black",outline="Black")
        displayMessage = self.game.turn+" To Move..."
        if self.game.isChecked(self.game.turn):
            if len(self.game.ruleSet.findAllLegalMoves(self.game.board,self.game.turn))==0:
                displayMessage = "Checkmate,"
                winsound.Beep(500,100)
                winsound.Beep(500,100)
                if(self.game.turn=="White"):
                    displayMessage += " Black Wins!"
                else:
                    displayMessage += " White Wins!"
            else:
                displayMessage = "Check! " + displayMessage
                winsound.Beep(500,150)
        self.create_text((4*SQUARESIZE,8*SQUARESIZE+(SQUARESIZE//4)),text=displayMessage,font=("Fixedsys", str(int(16*SCALE_MULTIPLIER))),fill="White")

app = ChessApplication()
app.mainloop()