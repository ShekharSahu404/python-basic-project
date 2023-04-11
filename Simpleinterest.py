import  customtkinter as ctk
from tkinter import  *

root  = ctk.CTk()
root.geometry("400x400")
root.title("PRT")

def PRTT():
    p = int(entry1.get())
    r = int(entry2.get())
    t = int(entry3.get())
    entry4.delete(0,END)
    prt = p*r*t
    new_prt = prt/100
    # new_prt = int(new_prt)
    entry4.insert( 1, new_prt)

label1 = ctk.CTkLabel(master=root,text="Principal",fg_color="tomato", corner_radius=8,width=30, height=24 ).grid(row=0 , column=0)
label2 = ctk.CTkLabel(master=root,text="Rate",fg_color="tomato",corner_radius=8,width=30, height=24).grid(row=1 , column=0)
label3 = ctk.CTkLabel(master=root,text="Time",fg_color="tomato",corner_radius=8,width=30, height=24).grid(row=2, column=0)

entry1 = ctk.CTkEntry(master=root ,width=150, height=30 )
entry1.grid(row=0 , column=1)
entry2 = ctk.CTkEntry(master=root ,width=150, height=30)
entry2.grid(row=1 , column=1)
entry3 = ctk.CTkEntry(master=root ,width=150, height=30)
entry3.grid(row=2 , column=1)


label4 = ctk.CTkButton(master=root,text="Submit" , command=PRTT).grid(row=5, column=0  , pady=40)
entry4 = ctk.CTkEntry(master=root)
entry4.grid(row=5 , column=1  , pady=40)






root.mainloop()