import tkinter as tk
from PIL import Image,ImageTk
import winsound
from src.main.model.Game import Game

# Constant Declarations
SCALE_MULTIPLIER = 1.5
DEFAULT_SIZE = 50
SQUARESIZE = int(DEFAULT_SIZE*SCALE_MULTIPLIER)


class ChessApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Create Main Window
        self.window = tk.Frame(self)
        self.window.pack(side="top", fill="both", expand=True)
        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(0, weight=1)
        self.minsize(8*SQUARESIZE, 8*SQUARESIZE + SQUARESIZE//2)
        self.maxsize(8*SQUARESIZE, 8*SQUARESIZE + SQUARESIZE//2)
        self.wm_title("Chess")
        self.iconphoto(self, ImageTk.PhotoImage(file=".\\img\\blkKnight.png"))

        # Initialize Scenes
        self.scenes = {}

        # For now, main page is a new game
        self.new_game()

        # Create Option Menu
        menu_bar = tk.Menu(self)
        menu_bar.add_command(label="New Game", command=self.new_game)
        ai_menu = tk.Menu(menu_bar, tearoff=0)
        easy_color_menu = tk.Menu(ai_menu, tearoff=0)
        easy_color_menu.add_command(label="Black")
        easy_color_menu.add_command(label="White")
        hard_color_menu = tk.Menu(ai_menu, tearoff=0)
        hard_color_menu.add_command(label="Black")
        hard_color_menu.add_command(label="White")
        ai_menu.add_cascade(label="Easy", menu=easy_color_menu)
        ai_menu.add_cascade(label="Hard", menu=hard_color_menu)
        menu_bar.add_cascade(label="Versus AI", menu=ai_menu)
        self.config(menu=menu_bar)
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
        self.tkraise(scene)
        # TODO: redraw scene on top

    def new_game(self):
        self.scenes = {}
        self.scenes[ChessGUI] = ChessGUI(self.window,self)
        self.show_scene(ChessGUI)


# This is a Canvas scene that represents a game of chess.
class ChessGUI(tk.Canvas):
    def __init__(self, parent,controller):
        tk.Canvas.__init__(self, parent)
        self.grid(row=0, column=0, sticky="nsew")
        self.imgs = []
        self.game = Game()
        self.firstInput = None
        self.lastHighlight = None
        self.bind("<Button-1>", self.handle_click)
        self.redraw()

    def handle_click(self, event):
        x_coord = int(event.x / SQUARESIZE)
        y_coord = int(event.y / SQUARESIZE)
        # Translate coords to squares
        letter = chr(x_coord+97)
        num = str(8-y_coord)
        square = letter+num
        if self.firstInput is None:
            # First click:
            if self.game.board.hasColorPiece(self.game.turn, square):
                # Your first click is on one of your pieces, highlight it
                self.firstInput = square
                self.lastHighlight = self.draw_image(".\\img\\highlight.png", x_coord, y_coord)
            else:
                self.lastHighlight = None
        elif self.firstInput is not None:
            # Second click:
            if self.game.makeMove(self.firstInput, square):
                # Second click is a valid move, make it and reset
                if self.game.turn == "White":
                    winsound.Beep(260, 150)
                else:
                    winsound.Beep(200, 150)
                self.lastHighlight = None
                self.firstInput = None
                self.redraw()
            elif self.game.board.hasColorPiece(self.game.turn, square):
                # Second click is not a valid move, but one of your pieces. Highlight it
                self.firstInput = square
                self.lastHighlight = self.draw_image(".\\img\\highlight.png", x_coord, y_coord)
            else:
                # Second click is not one of your pieces, and not a valid move. Reset highlights/inputs
                self.firstInput = None
                self.lastHighlight = None

    def redraw(self):
        # Delete Old Images
        self.imgs.clear()
        # Redraw Squares
        for sqr in self.game.board.squares:
            if sqr.color == "Black":
                sqr_file = ".\\img\\black_square.png"
            else:
                sqr_file = ".\\img\\white_square.png"
            self.imgs.append(self.draw_image(sqr_file, sqr.x_coord, sqr.y_coord))
        # Redraw Pieces
        for piece in self.game.board.pieces:
            if piece.color == "White":
                piece_file = ".\\img\\wht"+piece.name+".png"
            else:
                piece_file = ".\\img\\blk"+piece.name+".png"
            x_coord = ord(piece.square[0]) - 97
            y_coord = 8 - int(piece.square[1])
            self.imgs.append(self.draw_image(piece_file, x_coord, y_coord))
        # Redraw Bottom Menu
        self.create_rectangle((0, 8*SQUARESIZE, 8*SQUARESIZE, 8*SQUARESIZE+SQUARESIZE//2), fill="Black", outline="Black")
        display_message = self.game.turn+" To Move..."
        if self.game.isChecked(self.game.turn):
            if self.game.isCheckmated(self.game.turn):
                display_message = "Checkmate,"
                winsound.Beep(500, 100)
                winsound.Beep(500, 100)
                if self.game.turn == "White":
                    display_message += " Black Wins!"
                else:
                    display_message += " White Wins!"
            else:
                display_message = "Check! " + display_message
                winsound.Beep(500, 150)
        if self.game.isStalemated(self.game.turn):
            display_message = "Stalemate, Draw!"
        self.create_text((4*SQUARESIZE, 8*SQUARESIZE+(SQUARESIZE//4)), text=display_message, font=("Fixedsys", str(int(16*SCALE_MULTIPLIER))), fill="White")

    def draw_image(self, filename, x_coord, y_coord):
        raw_img = Image.open(filename)
        resized = raw_img.resize((SQUARESIZE, SQUARESIZE), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(resized)
        self.create_image(SQUARESIZE * x_coord, SQUARESIZE * y_coord, image=img, anchor=tk.NW)
        return img


app = ChessApplication()
app.mainloop()
