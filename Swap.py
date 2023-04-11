from tkinter import *
import customtkinter as ctk

root = ctk.CTk()

root.geometry("400x600")
root.title("Swap")

def swap():
    x = int(entry1.get())
    y = int(entry2.get())

    x,y = y,x
    entry1.delete(0, END)
    entry2.delete(0, END)

    entry1.insert(0,x)
    entry2.insert(0,y)

label1 = ctk.CTkLabel(master=root,
                      text="First Num" ,
                      fg_color="red",
                      corner_radius=8,
                      text_color="black",
                      height=30,
                      font=("ariel", 22)

                      ).grid(row=0,column=0 ,padx=20 , pady=20)

label2 = ctk.CTkLabel(master=root,
                      text="Second Num",
                      fg_color="red",
                      corner_radius=8,
                      font=("ariel", 22),

                      text_color="black",
                      height=30



                      ).grid(row=1,column=0,padx=20 , pady=20)


entry1 = ctk.CTkEntry(master=root,)
entry1.grid(row=0 , column=2)

entry2 = ctk.CTkEntry(master=root,)
entry2.grid(row= 1, column=2)


btn = ctk.CTkButton(master=root,
                    text="Swap" ,
                     fg_color="red",
                    font=("ariel" , 22),
                    hover_color="#27E1C1",
                      corner_radius=8,
                      text_color="black",
                      height=30,
                    command=swap)
btn.grid(row=3 , column=1, columnspan=2)



root.mainloop()