#1
from tkinter import *
root=Tk()
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)

DICT={'asa':123,'dff':345,'bbn':432,'dfd':787,'zxc':989,'yoy':678,'tyu':564,'pyp':434,'bbn':343,'hgh':544}
mylist=Listbox(root,yscrollcommand=scrollbar.set)
for i in DICT:
    mylist.insert(END,i,DICT[i])
mylist.pack(side=LEFT,fill=BOTH)
scrollbar.config(command=mylist.yview)

#2
def insert():
    DICT['klk']=112
    print(DICT)

button=Button(root,text='Insertion',command=insert)
button.pack()
root.mainloop()