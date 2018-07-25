#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.14
# In conjunction with Tcl version 8.6
#    Jul 25, 2018 02:18:34 PM

import sys
import pymysql
from tkinter import messagebox
try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import login_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel (root)
    login_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel (w)
    login_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None


class New_Toplevel:
    def add(self):
        ids=self.Entry1.get()
        name=self.Entry2.get()
        address=self.Entry3.get()
        self.cursor.execute("insert into records values("+ids+",'"+name+"','"+address+"')")
        self.db.commit()
        messagebox.showinfo("database","new records added")
        self.showdata()

    def delete(self):
        ids=self.Entry1.get()
        self.cursor.execute("delete from records where id="+ids)
        self.db.commit()
        self.showdata()
    def modify(self):
        ids=self.Entry1.get()
        name=self.Entry2.get()
        address=self.Entry3.get()
        self.cursor.execute("update records set name='"+name+"',address='"+address+"' where id="+ids+"")
        self.db.commit()
        self.showdata()
    def selection(self,event):
        index=self.Listbox1.curselection()[0]
        self.selected_tuple = self.Listbox1.get(index)
        print(index)
        self.Entry1.delete(0, END)
        self.Entry1.insert(END, self.selected_tuple[0])
        self.Entry2.delete(0, END)
        self.Entry2.insert(END, self.selected_tuple[1])
        self.Entry3.delete(0, END)
        self.Entry3.insert(END, self.selected_tuple[2])

    def showdata(self):
        sql="SELECT * from records"
        self.cursor.execute(sql)
        results=self.cursor.fetchall()
        i=0
        self.Listbox1.delete(0,END)
        for row in results:
            self.Listbox1.insert(i, row)
            i = i+1
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {Courier New} -size 10 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"

        top.geometry("600x450+414+179")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        self.db=pymysql.connect("127.0.0.1","root","1234","newdatabase",3306)
        self.cursor=self.db.cursor()


        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.07, rely=0.07, relheight=0.46, relwidth=0.88)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#d6d89c")
        self.Frame1.configure(width=525)

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.1, rely=0.29, height=21, width=64)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''ID''')
        self.Label1.configure(width=64)

        self.Entry1 = Entry(self.Frame1)
        self.Entry1.place(relx=0.38, rely=0.29,height=20, relwidth=0.31)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font=font10)
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")


        self.Label2 = Label(self.Frame1)
        self.Label2.place(relx=0.1, rely=0.49, height=21, width=64)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Name''')
        self.Label2.configure(width=64)

        self.Entry2 = Entry(self.Frame1)
        self.Entry2.place(relx=0.38, rely=0.49,height=20, relwidth=0.31)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font=font10)
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")

        self.Label3 = Label(self.Frame1)
        self.Label3.place(relx=0.1, rely=0.68, height=21, width=64)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Address''')
        self.Label3.configure(width=64)

        self.Entry3 = Entry(self.Frame1)
        self.Entry3.place(relx=0.38, rely=0.68,height=20, relwidth=0.31)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font=font10)
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.82, rely=0.24, height=24, width=53)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Add''')
        self.Button1.configure(width=53)
        self.Button1.configure(command=self.add)

        self.Button2 = Button(self.Frame1)
        self.Button2.place(relx=0.82, rely=0.49, height=24, width=54)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Delete''')
        self.Button2.configure(width=54)
        self.Button2.configure(command=self.delete)

        self.Button3 = Button(self.Frame1)
        self.Button3.place(relx=0.82, rely=0.73, height=24, width=59)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Modify''')
        self.Button3.configure(width=59)
        self.Button3.configure(command=self.modify)

        self.Frame2 = Frame(top)
        self.Frame2.place(relx=0.07, rely=0.58, relheight=0.34, relwidth=0.88)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="#b3d1d8")
        self.Frame2.configure(width=525)

        self.Listbox1 = Listbox(self.Frame2)
        self.Listbox1.place(relx=0.15, rely=0.06, relheight=0.79, relwidth=0.64)
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font=font10)
        self.Listbox1.configure(foreground="#000000")
        self.Listbox1.configure(width=334)
        self.Listbox1.bind('<<ListboxSelect>>', self.selection)
        self.showdata()






if __name__ == '__main__':
    vp_start_gui()



