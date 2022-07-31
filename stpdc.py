import lab8trial as lab
import pathlib
import tkinter
from tkinter.filedialog import asksaveasfilename
from tkinter import *
import homegui as hg
#frame
import sympy as symp
import numpy as num
import editgui as ed
from tkinter import messagebox

#global counter
counter=1
class sd():

 def save(self,root, lis):#to save the solution to share

  self.root = root
  self.lis = lis
  self.filename =asksaveasfilename(parent=root, filetypes=[('All Files', '*.*'),
           ('Python Files', '*.py'),
           ('Text Document', '*.txt')], title='Save as...')

  try:
   with open(self.filename, 'w') as  self.writer:
    self.writer.write("\n".join(lis.get(0, END))).split("\n")
    self.writer.write('\n')
    self.writer.close()
  except:
   print("no file found")
 def quit(self, root):#to quit and to open home window of our app
    self.root = root
    root.destroy()
    hg.gui()
 def __init__(self):

   # super().__init__()
   self.window = Tk()

   width = self.window.winfo_screenwidth()
   height = self.window.winfo_screenheight()
   self.window.geometry("%dx%d" % (width, height))
   self.window.title("steepestdescent calculator")
   self.window.columnconfigure(0, weight=1)
   self.window.rowconfigure(0, weight=1)


   #frames and labels
   self.framee = tkinter.Frame(self.window)
   self.framee.pack()
   self.label = tkinter.Label(self.framee, text="WELCOME TO STEEPEST DESCENT CALCULATOR", width=60, height=1, bg="red",
                              font="Times20 20 bold", fg='yellow', bd=6, relief=RIDGE)
   self.label.pack(anchor="nw", pady=10, fill=X, expand=True)

   self.frame = tkinter.Frame(self.window)
   self.frame.pack()
   self.frame1 = tkinter.Frame(self.window)
   self.frame1.pack()
   self.frame2 = tkinter.Frame(self.window)
   self.frame2.pack()
   self.frame3 = tkinter.Frame(self.window)
   self.frame3.pack()
   self.frame4 = tkinter.Frame(self.window)
   self.frame4.pack()
   self.frame5 = tkinter.Frame(self.window)
   self.frame5.pack()
   # var1 = tkinter.IntVar()
   # var2 = tkinter.IntVar()
   self.label = tkinter.Label(self.frame, text='Enter the initial value of x', width=40, bg="#DAA520",
                              font="Times20 14 bold", fg='black', bd=10, relief=RIDGE, justify=LEFT)
   # self.label.grid(row=0, column=0, pady=10,)
   self.label.pack(side="left", padx=5, pady=5)

   entry1 = tkinter.Entry(self.frame, bd=10, bg="#DAA520", font="Times20 12 bold", relief=RIDGE, fg="red", name="1")
   entry1.pack(side="left", padx=5, pady=5)
   # entry1.grid(row=0, column=1, pady=10, padx=20)

   self.label = tkinter.Label(self.frame1, text='Enter the initial value of y', width=40, bg="#DAA520",
                              font="Times20 14 bold", fg='black', bd=10, relief=RIDGE, justify=LEFT)
   # self.label.grid(row=1, column=0)
   self.label.pack(side="left", padx=5, pady=5)

   entry2 = tkinter.Entry(self.frame1, bd=10, bg="#DAA520", font="Times20 12 bold", relief=RIDGE, fg="red", name="2")
   # entry2.grid(row=1, column=1)
   entry2.pack(side="left", padx=5, pady=5)

   # entry1.grid(row=0, column=1, pady=10, padx=20)

   self.label = tkinter.Label(self.frame2, text='Enter the number of iteration do you want', width=40, bg="#DAA520",
                              font="Times20 14 bold", fg='black', bd=10, relief=RIDGE, justify=LEFT)
   # self.label.grid(row=2, column=0)
   self.label.pack(side="left", padx=5, pady=5)
   entry3 = tkinter.Entry(self.frame2, bd=10, bg="#DAA520", font="Times20 12 bold", relief=RIDGE, fg="red", name="3")
   # entry3.grid(row=2, column=1)
   entry3.pack(side="left", padx=5, pady=5)
   self.label = tkinter.Label(self.frame3, text='Enter the number of decimal place  do you want', width=40,
                              bg="#DAA520", font="Times20 14 bold", fg='black', bd=10, relief=RIDGE, justify=LEFT)
   # self.label.grid(row=3, column=0)
   self.label.pack(side="left", padx=5, pady=5)

   entry4 = tkinter.Entry(self.frame3, bd=10, bg="#DAA520", font="Times20 12 bold", relief=RIDGE, fg="red", name="4")
   # entry4.grid(row=3, column=1)
   entry4.pack(side="left", padx=5, pady=5)
   self.label = tkinter.Label(self.frame4, text='Enter the equation to be optimized', width=40, bg="#DAA520",
                              font="Times20 14 bold", fg='black', bd=10, relief=RIDGE, justify=LEFT)
   # self.label.grid(row=4, column=0)
   self.label.pack(side="left", padx=5, pady=5)

   entry5 = tkinter.Entry(self.frame4, bd=10, bg="#DAA520", font="Times20 12 bold", relief=RIDGE, fg="red", name="5")
   # entry5.grid(row=4, column=1)
   entry5.pack(side="left", padx=5, pady=5)
   self.entries = (entry1, entry2, entry3, entry4, entry5)
   self.button1 = tkinter.Button(self.frame5, text='submit', font='arial 16 bold', bd=6, bg="#DAA520", relief=RIDGE,
                                 command=lambda: self.click(self.entries, self.lis))
   # self.button1.grid(pady=20)
   self.button1.pack(side="bottom", padx=5, pady=5)
   self.frame11 = Frame(self.window)
   self.frame11.pack()
   self.frame12 = Frame(self.window)
   self.frame12.pack()
   self.lis = tkinter.Listbox(self.window, font="arial 12 bold")#listbox to show the solution
   # self.lis.grid(row=6,column=0,sticky="nsew")
   self.lis.pack(side="bottom", padx=10, pady=10, expand=True, fill=BOTH)
   self.scrolbar = Scrollbar(self.lis, orient=VERTICAL)
   self.scrolbar.pack(side='right', fill=Y, padx=5)

   # self.lis.grid(row=6, column=0, padx=5, pady=5,sticky='nsew')
   self.lis.configure(yscrollcommand=self.scrolbar.set)
   self.scrolbar.config(command=self.lis.yview)
   self.menubar = Menu(self.window,background="red",fg="white")
   self.filemenu = Menu(self.menubar)
   self.menubar.add_command(label='Home',background="yellow", command=lambda: self.quit(self.window))
   self.menubar.add_command(label='Redo',background="yellow", command=lambda: self.reset(self.entries, self.lis))
   self.menubar.add_command(label='Edit',background="yellow", command=lambda: [self.edit(self.lis)])
   self.menubar.add_command(label='Save', background="yellow",command=lambda: self.save(self.frame11, self.lis))
   # self.menubar.add_cascade(label='File', menu=self.filemenu)
   self.window.protocol('WM_DELETE_WINDOW', lambda: self.on_close(self.window))
   self.window.config(menu=self.menubar)
   self.window.mainloop()
 def on_close(self,window):
     self.window=window

     response = messagebox.askyesno('Confirm Exit', 'Are you sure you want to exit?')
     if response:
         window.destroy()

 def edit(self, lis):#to edit entry
   self.lis = lis
   lis.delete(0, END)

 def ff(self, e, q, exp):#to substitute value of expression
   x, y, f = symp.symbols(' x y f')
   self.e = e
   self.q = q
   self.exp = exp
   return exp.subs([(x, e), (y, q)]).evalf()

 def reset(self, entries, lis):#to restart the window
   self.entries = entries
   self.lis = lis
   for x in entries:
    x.delete(0, END)
   lis.delete(0, END)

 def evlder(self, d, b, c):#to evaluate value of expression
   x, y, f = symp.symbols(' x y f')
   return d.subs([(x, b), (y, c)]).evalf()

 def click(self, entries, lis):# actual calculation
   try:
    x, y, f = symp.symbols(' x y f')
    # X = [x, y]
    self.lis = lis
    self.entries = entries
    e = [x.get() for x in entries]
    #to insert content in listbox
    lis.insert(1, f"YOUR ENTERED VALUE OF X: {e[0]}")
    lis.insert(2, f"YOUR ENTERED VALUE OF Y: {e[1]}")
    lis.insert(3, f"YOUR ENTERED VALUE FOR NO OF ITERATION :{e[2]}")
    lis.insert(4, f"YOUR ENTERED VALUE FOR ROUNDING UPTO  NTH DECIMAL PLACE: {e[3]}")
    lis.insert(5, f"YOUR ENTERED VALUE OF FUNCTION TO BE OPTIMIZED: {e[4]}")

    global m
    m = 0

    self.n = []
    # for i in range(0, 2):

    self.n.append(float(e[0]))
    self.n.append(float(e[1]))
    self.s = []

    self.DE = []
    global a
    a = 0
    # self.d=lab.stc(float(e[0]),float (e[1]),int (e[2]),int (e[3]),str(e[4]))

    self.exp = symp.sympify(str(e[4]))
    dexp1 = symp.diff(self.exp, x, 1)#to evaluate derivative
    lis.insert(6, f"the derivative of func wrt to x= {dexp1}")

    print("the derivative of func wrt to x=", dexp1)
    dexp2 = symp.diff(self.exp, y, 1)
    lis.insert(7, f"the derivative of func wrt to y= {dexp2}")
    print("the derivative of func wrt to y=", dexp2)
    global i
    i = 1
    global k
    k = 8

    while (True):
     #main loop start

     lis.insert(k, '\n')
     print('\n')
     k += 1
     print("<<<<<<<<<<<-------here the number", i, "------->>>>>>>>>iteration start")
     lis.insert(k, f"<<<<<<<<<<<-------here  iteration {i} start------->>>>>>>>>")
     # vdexp1 = -1*( evlder(dexp1,n[a],n[a+1]))
     fun1 = self.evlder(dexp1, float(self.n[a]), float(self.n[a + 1]))
     self.val1 = round(fun1, int(e[3]))
     fun2 = self.evlder(dexp2, float(self.n[a]), float(self.n[a + 1]))
     self.val2 = round(fun2, int(e[3]))
     self.v = [self.val1, self.val2]
     print("the value of gradient is :", self.v)
     k += 1
     lis.insert(k, f"the value of gradient is : {self.v}")
     # print(val1)
     # print(val2)
     self.v1 = -1 * (self.val1)
     # print(v1)

     self.s.append(self.v1)
     # vdexp2 = -1*( evlder(dexp2,n[a],n[a+1]))
     self.v2 = -1 * (self.val2)
     self.s.append(self.v2)
     self.sa = [self.v1, self.v2]
     print("the value of search direction is :", self.sa)
     k += 1
     lis.insert(k, F"the value of search direction is : {self.sa}")

     for j in range(a, a + 2):
      self.g = (self.n[j] + f * self.s[j])
      self.n.append(self.g)
      # print(n[j+2])
     self.p = self.ff(self.n[a + 2], self.n[a + 3], self.exp)
     print(self.p)
     k += 1
     lis.insert(k, f'{self.p}')
     self.dp = symp.diff(self.p, f, 1)

     print(self.dp)
     k += 1
     lis.insert(k, f'{self.dp}')
     self.polyf = symp.poly(self.dp)
     # print(polyf)
     self.polyfcf = list(self.polyf.all_coeffs())

     self.r = (num.roots(self.polyfcf))
     self.l = float(self.r)
     self.dr = round(self.l, int(e[3]))
     print("the value of root f: ", self.dr)
     k += 1
     lis.insert(k, f'the value of root f: {self.dr}')

     self.n.remove(self.n[a + 2])
     self.n.remove(self.n[a + 2])
     k += 1

     for j in range(a, a + 2):
      self.g = round(self.n[j] + self.dr * self.s[j], int(e[3]))
      self.n.append(self.g)
      self.x1 = self.n[j + 2]
      print("the value of Xs are:", self.n[j + 2])
      self.DE.append(self.x1)

     lis.insert(k, f"the value of Xs are: {self.DE}")
     self.DE.clear()
     k += 1

     # print(len(n))
     m += 1
     a += 2
     print(" <<<<<<<<<<<<<-----------the Iteration ", i, "  end--------->>>>>>>>>>>>>")

     lis.insert(k, f" <<<<<<<<<<<<<-----------the Iteration  {i}  end--------->>>>>>>>>>>>>")
     k += 1
     i += 1
     lis.pack()
     if (self.v1 == self.n[a] and self.v2 == self.n[a + 1]):
      break
     elif (m == int(e[2])):
      break

   except:
    print("value error")






if __name__=='__main__':
    myapp=sd()
    print(counter)


