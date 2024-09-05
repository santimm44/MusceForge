# Import Module
from tkinter import *

# create root window
root = Tk()

# root window title and dimension
root.title("MuscleForge")

# Set geometry (widthxheight)
root.geometry('1000x800')

#create frame for lbl1
loginFrame = Frame(root, relief= 'sunken')
loginFrame.grid(sticky="we")

# Make the frame sticky for every case
loginFrame.grid_rowconfigure(0, weight = 1)
loginFrame.grid_columnconfigure(0, weight = 1)

root.grid_rowconfigure(0, weight = 1)
root.grid_columnconfigure(0, weight = 1)

#adding a label to the root window
lbl = Label(loginFrame, text = "Username", font=('Helvetica 15 bold'), bg = "white")
lbl.grid(row=3, column=0)
lbl.grid_rowconfigure(1, weight = 1)
lbl.grid_columnconfigure(1, weight = 1)

lbl = Label(loginFrame, text = "Password", font=('Helvetica 15 bold'), bg = "white")
lbl.grid(row=10, column=0)
lbl.grid_rowconfigure(1, weight = 1)
lbl.grid_columnconfigure(1, weight = 1)

# all widgets will be here
# Execute Tkinter
root.mainloop()
