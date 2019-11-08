from tkinter import *
root = Tk()
canvas = Canvas(root, width=100, height=100)
canvas.pack()
img = PhotoImage(file='whtPawn.png')
canvas.create_image(50, 50, image=img)
root.mainloop()