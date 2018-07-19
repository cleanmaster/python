from tkinter import *
class welcome():
    def __init__(self,master):
        self.master=master
        master.geometry("600x400+100+200")
        master.title("welcome")
        Label(master,text="Welcome to wages calculator",fg="red",font=("bold",10),anchor='w').grid(row=0,column=2)
        Button(master,text="ok",bg="green",fg="white",command=self.gotwages).place(x=180,y=60)
        Button(master,text="quit",bg="red",fg="white",command=self.finish).place(x=130,y=60)
    def finish(self):
        self.master.destroy()
    def gotwages(self):
        root2=Toplevel(self.master)
        mugui=wages(root2)



class wages():
    def __init__(self,master):
        self.master=master
        self.nhours=DoubleVar()
        self.salary=DoubleVar()
        self.master.geometry("500x200+100+200")
        self.master.title("wages Calculator")
        Label(master,text="welcome to wages calculator",fg="red",font=("bold",10),anchor='w').grid(row=0,column=2)
        Label(master,text="Enter your salary",fg="red",font=("bold",10),anchor='w').grid(row=3,column=0)
        Label(master,text="Enter no of hours",fg="red",font=("bold",10),anchor='w').grid(row=4,column=0)
        self.mysalry=Entry(self.master,textvariable=self.salary).grid(row=3,column=2)
        self.myhours=Entry(self.master,textvariable=self.nhours).grid(row=4,column=2)
        Button(master,text="calculate",bg="red",fg="white",command=self.calsal).grid(row=5,column=6)
    def myquit(self):
        self.master.destroy()
    def calsal(self):
        hours=self.nhours.get()
        print(hours)
        hsal=self.salary.get()
        salary=hours*hsal
        print(salary)
        Label(self.master,text="your salary is %.2f rs"%salary).grid(row=7,column=2)
def main():
    window=Tk()
    myGUIWelcome=welcome(window)
    window.mainloop()        
if __name__=='__main__':
    main()
    
