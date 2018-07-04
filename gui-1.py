#1
#from tkinter import *
#r= Tk()
#r.title("Welcome")
#lbl = Label(r, text="Hello world").grid(column=0, row=0)
#btn = Button(r, text="Exit",command=exit).grid(column=0, row=1)
#r.mainloop()

#2
#from tkinter import *
#r= Tk()
#r.title("Welcome")
#lbl = Label(r, text="Hello world").grid(column=0, row=0)
#btn = Button(r, text="Exit",command=exit).grid(column=0, row=1)
#def fun():
 #   print("welcome to the hello world")
#btn1=Button(r,text="click me",command=fun).grid(column=1,row=1)
#r.mainloop()

#3
#from tkinter import *
#root = Tk()
#label=Label(root,text="old text")
#def click():
 # label.config(text="ghjjg")
#b1 = Button(root, text="click me",command=click)
#label.pack()
#b1.pack()
#root.mainloop()

#4
from tkinter import *
def show_entry_fields():
   print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
master = Tk()
Label(master, text="First Name").grid(row=0)
Label(master, text="Last Name").grid(row=1)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
mainloop()