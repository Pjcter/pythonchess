import tkinter as tk
class ChessApplication(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self,*args,**kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill = "both", expand = True)

        container.rowconfigure(0,weight=1)
        container.columnconfigure(0,weight=1)

        self.frames = {}

        frame = ChessGUI(container, self)

        self.frames[ChessGUI] = frame

        frame.grid(row=0,column=0,sticky="nsew")

        self.show_frame(ChessGUI)

    def show_frame(self,cont):

        frame = self.frames[cont]
        frame.tkraise()

class ChessGUI(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        flipFlop = True
        self.imgs = []
        for i in range(8):
            flipFlop = (not flipFlop)
            for j in range(8):
                flipFlop = (not flipFlop)
                if flipFlop:
                    img = tk.PhotoImage(file ="black_square.png")
                else:
                    img = tk.PhotoImage(file="white_square.png")
                label = tk.Label(self,image= img)
                label.grid(row = i,column = j)
                self.imgs.append(img)

app = ChessApplication()
app.mainloop()


