# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 16:53:23 2022

@author: 1
"""

import tkinter
from tkinter import*

root=Tk()
root.title("shopping_list")
root.geometry("400x650")
root.resizable(False,False)
root.configure(bg="gold")


shopping_list=[]

def additem():
    item=item_entry.get()
    item_entry.delete(0,END)
    
    if item:
        with open("list.txt","a") as file:
            if item!=("\n"):                
                file.write(item+"\n")
        shopping_list.append(item)
        listbox.insert(END,item)
        
        
def removeitem():
    
    
    item=str(listbox.get(ANCHOR))
    if item in shopping_list:
        shopping_list.remove(item)
        with open("list.txt","w") as file:
            for item in shopping_list:
                file.write(item+"\n")
        listbox.delete(ANCHOR)

def deleteitem():
    listbox.delete(0,END)
 

def opentaskfile():
    try:
        global shopping_list
        
        with open ("list.txt", "r") as file:
            files=file.readlines()
        for item in files:
            if item !="\n":
                shopping_list.remove(item)
                listbox.insert(END,item)
                
    except:
        file=open("list.txt","w")
        file.close()

#labels

heading=Label(root,text="SHOPPING LIST",font="algerian 20 bold", fg="black",bg="gold")
heading.place(x=90,y=20)

writeitem=Label(root,text="Add an item to list:",font="algerian 14 bold", fg="black",bg="light gray")
writeitem.place(x=10,y=150)

help=Label(root,text="Help",font="arial 10 bold", fg="black",bg="light gray")
help.place(x=5,y=5)


#main

frame=Frame(root,width=280,height=50, bg="white")
frame.place(x=10,y=180)

item=StringVar()
item_entry=Entry(frame,width=18,font="arial 20",bd=0)
item_entry.place(x=10,y=7)



#listbox
frame1=Frame(root,width=300,height=80,bg="#32405b")
frame1.place(x=10,y=235)

listbox=Listbox(frame1,font=("arial",16),width=20,height=16,bg="white",fg="black",cursor="hand2",selectbackground="red")
listbox.pack(side=LEFT, fill=BOTH,padx=2)
scrollbar=Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

#buttons

button=Button(root,text="ADD",font="algerian 20 bold",width=5, bg="green",fg="white",command=additem)
button.place(x=295,y=180)

remove_icon=Button(root,text="REMOVE",font="algerian 16 bold",width=7,fg="white",bg="orange",command=removeitem)
remove_icon.place(x=285,y=240)

Delete_icon=Button(root,text="DELETE",font="algerian 16 bold",width=7,fg="white",bg="red",command=deleteitem)
Delete_icon.place(x=285,y=600)

#start file

opentaskfile()

root.mainloop()
