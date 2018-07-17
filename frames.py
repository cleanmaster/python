from tkinter import *
windows=Tk()
windows.geometry("300x300")
topframe=Frame(windows)
topframe.pack()
Button(topframe,bg="pink",width=10).pack()
bottomframe=Frame(windows)
bottomframe.pack(side="bottom")
Button(bottomframe,bg="black",width=10).pack()
