from tkinter import *
windows=Tk()
windows.geometry("300x300")
a=StringVar()
b=StringVar()
c=StringVar()
def fun1():
    print("yaay  its working")
def addition():
    global d
   
    d=int(a.get())+int(b.get())
    c.set(d)
def subtract():
    d=int(a.get())-int(b.get())
    c.set(d)
    
          
def multi():
      d=int(a.get())*int(b.get())
      c.set(d)
def qui():
    windows.withdraw()
    
menu=Menu(windows)
windows.config(menu=menu)
subMenu=Menu(menu)
menu.add_cascade(label="file",menu=subMenu)
subMenu.add_command(label="New project..",command=fun1)
subMenu.add_command(label="New..",command=fun1)
editMenu=Menu(menu)
menu.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="cut",command=fun1)
editMenu.add_command(label="copy",command=fun1)
Label(windows,text="enter 1 no").grid(row=5,column=0,sticky=W)
Label(windows,text="enter second no").grid(row=6,column=0,sticky=W)
Label(windows,text="result").grid(row=7,column=0,sticky=W)
Entry(windows,textvariable=a).grid(row=5,column=1)
Entry(windows,textvariable=b).grid(row=6,column=1)
Entry(windows,textvariable=c).grid(row=7,column=1)
operations=Menu(menu)
menu.add_cascade(label="operations",menu=operations)
operations.add_command(label="sum",command=addition)
operations.add_command(label="subtract",command=subtract)
operations.add_command(label="multiply",command=multi)
returns=Menu(menu)
menu.add_cascade(label="quit",menu=returns)
returns.add_command(label="EXIT",command=qui)
windows.mainloop()
