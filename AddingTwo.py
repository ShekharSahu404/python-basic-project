from tkinter import *
import customtkinter as ctk
root = ctk.CTk()

root.geometry("400x600")
root.title("Calulator")

def Add():
    x = int(entry1.get())
    y = int(entry2.get())
    ans.delete(0,END)
    z = x+y
    ans.insert(0,z)


def Sub():
    x = int(entry1.get())
    y = int(entry2.get())
    ans.delete(0,END)
    z = x- y
    ans.insert(0,z)


def Mul():
    x = int(entry1.get())
    y = int(entry2.get())
    ans.delete(0,END)
    z = x * y
    ans.insert(0, z)

def Div():
    x = int(entry1.get())
    y = int(entry2.get())
    ans.delete(0,END)
    z = x / y
    ans.insert(0, z)



label = ctk.CTkLabel( master=root ,
                       text="Enter 1ST Number " ,
                       width=68,
                       height=30,
                      corner_radius=8,
                       fg_color="red"
)
label.grid(row=0 , column=0 , padx=20)

entry1 = ctk.CTkEntry(master=root   ,fg_color="white" , corner_radius=8  , text_color="black", height=30)
entry1.grid(row=0, column=1)


label2 = ctk.CTkLabel(master=root ,
                       text="Enter 2nd Number ",
                       width=68,
                       height=30,
                      corner_radius=8,
                       fg_color="green")
label2.grid(row=1, column=0)

entry2 = ctk.CTkEntry(master=root  ,fg_color="white" , corner_radius=8  , text_color="black", height=30)
entry2.grid(row=1, column= 1,pady=10)

#Define


button = ctk.CTkButton(master=root ,
                       text="+" ,
                       width=68,
                       height=20,
                       font=("ariel", 20),
                       text_color="black",
                       fg_color="#B2A4FF",
                       command=Add

                       )
button.grid(row=5 , column=0, pady=10)



button2 = ctk.CTkButton(master=root ,
                       text="-" ,
                       width=68,
                       height=20,
                       font=("ariel", 20),
                       text_color="black",
                       fg_color="#B2A4FF",
                       command=Sub)
button2.grid(row=5 , column=1)



button3 = ctk.CTkButton(master=root ,
                       text="x" ,
                       width=68,
                       height=20,
                       font=("ariel", 20),
                       text_color="black",
                       fg_color="#B2A4FF",

                       command=Mul)
button3.grid(row=6 , column=0)


button4 = ctk.CTkButton(master=root ,
                       text="/" ,
                       width=68,
                       height=20,
                       font=("ariel", 20),
                       text_color="black",
                       fg_color="#B2A4FF",
                       command=Div)
button4.grid(row=6, column=1)


ans_text = ctk.CTkLabel(master=root  ,text="Ans" )
ans_text.grid(row=10 , column=0  , pady=20)

ans = ctk.CTkEntry(master=root  )
ans.grid(row=10  ,column=1  , pady=20)




root.mainloop()