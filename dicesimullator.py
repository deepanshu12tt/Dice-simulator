from tkinter import  *
import random


root=Tk()
root.geometry("600x500")
root.title("Dice simulator")
root.configure(bg="black")
label=Label(root,font=("Helvetica",200,'bold'),text=" ")
def rolldice():
    dice=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    label.configure(text=f'{random.choice(dice)}')
    label.pack()


btn=Button(root,font=("Helvetica",25,'bold'),text="Dice roll",command=rolldice).pack()
root.mainloop()