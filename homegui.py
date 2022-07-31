from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
import stpdc as sa
import sormethod as sr
import gauss_siedelmethod as gd
import tkinter.dialog as dialog


#home gui to call every function
class gui():



 def __init__(self):






  try:



    self.window=Tk()
    self.window.title("LINEAR ALGEBRA SIMPLIFIER")
    self.width= self.window.winfo_screenwidth()
    self.height= self.window.winfo_screenheight()
    self.window.geometry("%dx%d" % (self.width, self.height))
    self.window.configure(background="aqua")
    #frame
    self.frame = Frame(self.window,bg="aqua")
    self.frame.pack()
    self.label = Label(self.frame, bg="red", height=2,text="Welcome to Linear Algebra Simplifier", font="Times20 20 bold ", fg="yellow", bd=6, relief=RIDGE)
    self.label.pack(side="top", expand=True, fill=X, padx=10, pady=10)
    self.label1 = Label(self.frame, text="CHOOSE FROM FOLLOWING METHODS :", font="Times20 18 bold", bg="red", bd=6,fg="gold",
                         relief=GROOVE)
    self.label1.pack(side="top", pady=20)

    self.button = Button(self.frame, text="Steepestdescent Calculator", font="Times20 18 bold",bg="red",bd=6,relief=GROOVE, command=lambda:[self.dest(self.window),sa.sd()])
    self.button.pack(side="top", pady=20)
    self.button1 = Button(self.frame, text="Successive Over Relaxation Method", font="Times20 18 bold", bg="red", bd=6,
                       relief=GROOVE, command=lambda: [self.dest(self.window),sr.sor()])
    self.button1.pack(side="top", pady=20)
    self.button2= Button(self.frame, text="Gauss Siedel Method", font="Times20 18 bold", bg="red", bd=6,
                       relief=GROOVE, command=lambda: [self.dest(self.window),gd.gsm()])
    self.button2.pack(side="top", pady=20)
    #menubar
    self.menubar=Menu(self.window,background='blue', fg='white')

    self.filemenu=Menu(self.menubar)

   # self.filemenu.add_command(label='exit', command=lambda: self.quit(window))
    self.menubar.add_command(label='exit',background="yellow", command=lambda: self.quit(self.window))

    #self.menubar.add_cascade(label='exit', menu=self.filemenu)
    self.window.config(menu=self.menubar)
    self.window.protocol('WM_DELETE_WINDOW',lambda:self.on_close(self.window))

    self.window.mainloop()
    print(self.window.winfo_exists())

  except:

      print("application destroyed")


 def dest(self,window):#to destroy CURRENT window
     self.window=window
     window.destroy()


 def quit(self,root):


     response = messagebox.askyesno('Confirm Exit', 'Are you sure you want to exit?')#to confirm exit
     if response:
         try:
             self.root = root
             root.destroy()


         except:
             print("exit")

 def on_close(self,window):
     self.window=window

     response = messagebox.askyesno('Confirm Exit', 'Are you sure you want to exit?')
     if response:
         window.destroy()




if __name__=='__main__':
    myapp = gui()










