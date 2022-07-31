import homegui as hg
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename
from tkinter import *
class sor():
    def save(self, root, lis):#to save solution for future reference
        self.root=root
        self.lis=lis
        self.files = [('All Files', '*.*'),
                      ('Python Files', '*.py'),
                      ('Text Document', '*.txt')]
        #self.data = text.get('0.0', END)
        self.filename =asksaveasfilename(parent=root, filetypes=self.files, title='Save as...')
        try:
            with open(self.filename, 'w') as self.writer:
             self.writer.write("\n".join(lis.get(0, END))).split("\n")
             self.writer.write('\n')
             self.writer.close()
        except:
            print("no file found")
    def quit(self, root):#to destroy window
        self.root = root
        root.destroy()
        hg.gui()#to open homewindow

    def __init__(self):
        #main window
        self.window = Tk()
        self.window.configure(background="white")
        width = self.window.winfo_screenwidth()
        height = self.window.winfo_screenheight()

        self.window.geometry("%dx%d" % (width, height))
        self.window.title("SUCCESSIVE OVER RELAXATION  CALCULATOR")
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)

        # window=tkinter.Tk()
        #frames and labels

        self.frame =Frame(self.window,bg="white")
        self.frame.pack()
        self.label=Label(self.frame,text="WELCOME TO SUCCESSIVE OVER RELAXATION METHOD",height=1,bg="red",font="Times20 20 bold",fg='yellow',bd=6,relief=RIDGE)
        self.label.pack(padx=5,pady=5,fill="x",expand=True)
        self.frame1 =Frame(self.window,bg="white")
        self.frame1.pack()

        self.frame2 = Frame(self.window,bg="white")
        self.frame2.pack()
        self.label = Label(self.frame2, text="enter the value of coeffient of  ROW CONTAINING HIGHEST OF X (inorder-x,y,z) and then constant term ",
                     height=1,
                           bg="#DAA520", font="Times20 14 bold", fg='black', bd=6, relief=RIDGE)
        self.label.pack(side="left",pady=5)
        entry1 =Entry(self.frame2, bd=6,width=5, bg="#DAA520", font="Times20 12 bold", relief=RIDGE, fg="red")
        entry1.pack(side="left", padx=5, pady=5)
        entry2 = Entry(self.frame2, bd=6, width=5, bg="#DAA520", font="Times20 12 bold", relief=RIDGE, fg="red")
        entry2.pack(side="left", padx=5, pady=5)
        entry3 = Entry(self.frame2, bd=6, width=5, bg="#DAA520", font="Times20 12 bold", relief=RIDGE, fg="red")
        entry3.pack(side="left", padx=5, pady=5)
        entry4 = Entry(self.frame2, bd=6, width=5, bg="#DAA520", font="Times20 12 bold", relief=RIDGE, fg="red")
        entry4.pack(side="left", padx=20, pady=5)
        self.frame3 =Frame(self.window,bg="white")
        self.frame3.pack()
        self.label = Label(self.frame3,
                           text="enter the value of coeffient of  ROW CONTAINING HIGHEST OF Y (inorder-x,y,z) and then constant term ",
                            height=1,
                           bg="#DAA520", font="Times20 14 bold", fg='black', bd=6, relief=RIDGE)
        self.label.pack(side="left",pady=5)
        entry5 = Entry(self.frame3, bd=6, width=5, bg="#DAA520", font="Times20 12 bold", relief=RIDGE, fg="red")
        entry5.pack(side="left", padx=5, pady=5)
        entry6 = Entry(self.frame3, bd=6, width=5, bg="#DAA520", font="Times20 12 bold", relief=RIDGE, fg="red")
        entry6.pack(side="left", padx=5, pady=5)
        entry7 = Entry(self.frame3, bd=6, width=5, bg="#DAA520", font="Times20 12 bold", relief=RIDGE, fg="red")
        entry7.pack(side="left", padx=5, pady=5)
        entry8 = Entry(self.frame3, bd=6, width=5, bg="#DAA520", font="Times20 12 bold", relief=RIDGE, fg="red")
        entry8.pack(side="left", padx=20, pady=5)
        self.frame4 = Frame(self.window,bg="white")
        self.frame4.pack()
        self.label = Label(self.frame4,
                           text="enter the value of coeffient of  ROW CONTAINING HIGHEST OF Z (inorder-x,y,z) and then constant term ", height=1,
                           bg="#DAA520", font="Times20 14 bold", fg='black', bd=6, relief=RIDGE)
        self.label.pack(side="left",pady=5)
        entry9 = Entry(self.frame4, bd=6, width=5, bg="#DAA520", font="Times20 12 bold", relief=RIDGE, fg="red")
        entry9.pack(side="left", padx=5, pady=5)
        entry10 = Entry(self.frame4, bd=6, width=5, bg="#DAA520", font="Times20 12 bold", relief=RIDGE, fg="red")
        entry10.pack(side="left", padx=5, pady=5)
        entry11 = Entry(self.frame4, bd=6, width=5, bg="#DAA520", font="Times20 12 bold", relief=RIDGE, fg="red")
        entry11.pack(side="left", padx=5, pady=5)
        entry12= Entry(self.frame4, bd=6, width=5, bg="#DAA520", font="Times20 12 bold", relief=RIDGE, fg="red")
        entry12.pack(side="left", padx=20, pady=5)
        self.frame5 =Frame(self.window,bg="white")
        self.frame5.pack()
        self.label=Label(self.frame5,text=" enter the number of iteration do you want ", height=1,
                           bg="#DAA520", font="Times20 14 bold", fg='black', bd=6, relief=RIDGE)
        self.label.pack(side="left",pady=5)
        entry13 = Entry(self.frame5, bd=6, width=5, bg="#DAA520", font="Times20 12 bold", relief=RIDGE, fg="red")
        entry13.pack(side="left", padx=20, pady=5)
        self.frame6 =Frame(self.window,bg="white")
        self.frame6.pack()

        self.label = Label(self.frame6, text="enter the number of decimals do you want ", height=1,
                           bg="#DAA520", font="Times20 14 bold", fg='black', bd=6, relief=RIDGE)
        self.label.pack(side="left", pady=5)
        entry14 = Entry(self.frame6, bd=6, width=5, bg="#DAA520", font="Times20 12 bold", relief=RIDGE, fg="red")
        entry14.pack(side="left", padx=20, pady=5)
        self.frame7 = Frame(self.window,bg="white")
        self.frame7.pack()
        self.label=Label(self.frame7,text="          enter the value of parameter w             ",height=1,bg="#DAA520", font="Times20 14 bold", fg='black', bd=6, relief=RIDGE)
        self.label.pack(side="left",pady=5)
        entry15 = Entry(self.frame7, bd=6, width=5, bg="#DAA520", font="Times20 12 bold", relief=RIDGE, fg="red")
        entry15.pack(side="left", padx=20, pady=5)
        self.frame8 = Frame(self.window, bg="white")
        self.frame8.pack()
        self.label = Label(self.frame8, text="enter the initial value of x,y,z", height=1,
                           bg="#DAA520", font="Times20 14 bold", fg='black', bd=6, relief=RIDGE)
        self.label.pack(side="left", pady=10)
        entry16 = Entry(self.frame8, bd=6, width=5, bg="#DAA520", font="Times20 12 bold", relief=RIDGE, fg="red")
        entry16.pack(side="left", padx=10, pady=5)
        entry17 = Entry(self.frame8, bd=6, width=5, bg="#DAA520", font="Times20 12 bold", relief=RIDGE, fg="red")
        entry17.pack(side="left", padx=10, pady=5)
        entry18 = Entry(self.frame8, bd=6, width=5, bg="#DAA520", font="Times20 12 bold", relief=RIDGE, fg="red")
        entry18.pack(side="left", padx=10, pady=5)
        self.entries=(entry1,entry2,entry3,entry4,entry5,entry6,entry7,entry8,entry9,entry10,entry11,entry12,entry13,entry14,entry15,entry16,entry17,entry18)

        self.lis =Listbox(self.window, font="arial 12 bold")#listbox

        self.lis.pack(side="bottom", padx=10, pady=10, expand=True, fill=BOTH)
        self.scrolbar = Scrollbar(self.lis, orient=VERTICAL)#scrolbar attached to listbox
        self.scrolbar.pack(side='right', fill=Y, padx=5)
        self.lis.configure(yscrollcommand=self.scrolbar.set)
        self.scrolbar.config(command=self.lis.yview)#scrolbar orientation
        self.frame9 = Frame(self.window, bg="white")
        self.frame9.pack()
        self.button1 = Button(self.frame9, text='submit', font='arial 16 bold', bd=6, bg="#DAA520",
                              relief=RIDGE,command=lambda:self.click(self.entries,self.lis))

        self.button1.pack(side="bottom", padx=5, pady=5)
        #menubar
        self.menubar = Menu(self.window)
        self.filemenu = Menu(self.menubar)
        self.menubar.add_command(label='Home', command=lambda: self.quit(self.window))
        self.menubar.add_command(label='Redo', command=lambda: self.reset(self.entries, self.lis))
        self.menubar.add_command(label='Edit', command=lambda: [self.edit(self.lis)])
        self.menubar.add_command(label='Save', command=lambda: self.save(self.window, self.lis))


        #self.menubar.add_cascade(label='File', menu=self.filemenu)
        self.window.protocol('WM_DELETE_WINDOW', lambda: self.on_close(self.window))
        self.window.config(menu=self.menubar)
        #to start machinery
        self.window.mainloop()


        #root.destroy()

    def on_close(self, window):
        self.window = window

        response = messagebox.askyesno('Confirm Exit', 'Are you sure you want to exit?')
        if response:
            window.destroy()

    def edit(self, lis):#to edit one or more entry
        self.lis = lis
        lis.delete(0, END)
    def reset(self, entries, lis):#to redo the operation
        self.entries = entries
        self.lis = lis
        for x in entries:
            x.delete(0, END)
        lis.delete(0, END)
    def click(self,entries,lis):#actual simplication starts
     try:
        self.lis = lis
        self.entries = entries
        e = [x.get() for x in entries]
        #inserting contents into listbox
        lis.insert(1, f"YOUR ENTERED VALUE OF MATRIX: ")
        lis.insert(2, f"[{e[0]} {e[1]} {e[2]}\n"
                      f"{e[4]} {e[5]} {e[6]}\n"
                      f"{e[8]} {e[9]} {e[10]}\n]")

        lis.insert(3,"YOUR VALUE OF VECTORS I.E.CONSTANT TERMS:")
        lis.insert(4,f'[{e[3]} {e[7]} {e[11]}]')
        lis.insert(5,f'YOUR VALUE FOR NO OF ITERATION:{e[12]}')
        lis.insert(6,f'YOUR VALUE FOR ROUNDING UPTO {e[13]} DECIMAL PLACES')
        lis.insert(7,f'YOUR VALUE FOR PARAMETER W:{e[14]}')
        lis.insert(8,F'YOUR ENTERED VALUE OF X,Y,Z:{e[15]} {e[16]} {e[17]}' )
        x = []
        y = []
        z = []
        x.append(float(e[15]))
        y.append(float(e[16]))
        z.append(float(e[17]))
        global k
        k=9
        #finding  the solution of x,y,z for each iteration
        for i in range(0, int(e[12])):
            rd =int(e[13])
            w=float(e[14])
            x1 = round(((1.0 - w) * x[i]) + ((w / float(e[0])) * (float(e[3]) - (float(e[1]) * y[i]) - (float(e[2]) * z[i]))), rd)
            print(x1)
            x.append(x1)
            y1 = round(((1.0 - w) * y[i]) + ((w / float(e[5])) * (float(e[7]) - (float(e[4]) * x[i + 1]) - (float(e[6]) * z[i]))),
                       rd)
            y.append(y1)
            print(y1)
            z1 = round(
                ((1.0 - w) * z[i]) + ((w / float(e[10])) * (float(e[11]) - (float(e[8]) * x[i + 1]) - (float(e[9]) * y[i + 1]))), rd)
            z.append(z1)
            print(z1)
            lis.insert(k,f"for iteration {i + 1} : [{x[i + 1]}  , {y[i + 1]}  ,{z[i + 1]}]")
            k+=1
            print(f"for iteration {i + 1} : [{x[i + 1]}  , {y[i + 1]}  ,{z[i + 1]}]")
            if (x[i] == x[i + 1] and y[i] == y[i + 1] and z[i] == z[i + 1]):#if condition satisfied then break
                break
     except:
         print("value error")




if __name__=='__main__':
    myapp=sor()