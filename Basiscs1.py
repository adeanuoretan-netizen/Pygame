import tkinter as tk
from tkinter import messagebox
screen=tk.Tk()
screen.title("GUI1")
screen.geometry("800x900")
screen.configure(bg="#06a2d6")

def showmessagebox():
    messagebox.showinfo("Success","Your details have been saved")


l1=tk.Label(text= "Welcome to GUI", width= 25, height=2, bg="grey",fg="black", font=("Arial",20))
l1.place(x=200,y=50)
l2=tk.Label(text= "Enter your name", width= 15, height=1, bg="yellow",fg="green", font=("Arial",20))
l2.place(x=50,y=150)
e1=tk.Entry(width=20)
e1.place(x=400,y=150)
l3=tk.Label(text= "Enter your adress", width= 25, height=1, bg="black",fg="white", font=("Arial",20))
l3.place(x=50,y=250)
t1=tk.Text(width=30, height=5)
t1.place(x=500, y= 240)
b1=tk.Button(text= "Submit", width= 20, height=1, bg="black",fg="white", font=("Arial",20),command=showmessagebox)
b1.place(x=270,y=800)
l4=tk.Label(text= "select your gender", width= 18, height=1, bg="grey",fg="black", font=("Arial",20))
l4.place(x=50,y=400)
r1=tk.Radiobutton(text="male",value=0)
r1.place(x=400,y=400)
r2=tk.Radiobutton(text="female",value=1)
r2.place(x=590,y=400)
l5=tk.Label(text= "What is you age", width=15, height=1, bg="green", fg="red", font=("Arial",20))
l5.place(x=50,y=450)
e2=tk.Entry(width=15)
e2.place(x=400, y=460)
l6=tk.Label(text= "select your hobbies", width= 18, height=1, bg="grey",fg="black", font=("Arial",20))
l6.place(x=20,y=500)
c1=tk.Checkbutton(text="Coding",onvalue=1, offvalue=0)
c1.place(x=345, y=500)
c2=tk.Checkbutton(text="Football",onvalue=1, offvalue=0)
c2.place(x=420, y=500)
c3=tk.Checkbutton(text="Gaming",onvalue=1, offvalue=0)
c3.place(x=500, y=500)
l7=tk.Label(text= "select your weight", width= 18, height=1, bg="grey",fg="black", font=("Arial",20))
l7.place(x=20,y=550)
s1=tk.Scale(from_=0,to=100,orient=tk.HORIZONTAL,length=150)
s1.place(x=500,y=550)
l8=tk.Label(text= "select the languages you know", width= 24, height=1, bg="grey",fg="black", font=("Arial",20))
l8.place(x=20,y=600)
Languages=["English","Spanish","French","German","Swedish","Norweigien"]
lb1=tk.Listbox(width=50,height=6,selectmode=tk.MULTIPLE)
lb1.place(x=500,y=600)
for i in Languages:
    lb1.insert(tk.END,i)







screen.mainloop()