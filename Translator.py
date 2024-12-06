from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def change(text="type", src="en", dest="hi"):
    # Use the correct variable names for source and destination languages
    trans = Translator()
    trans1 = trans.translate(text, src=src, dest=dest)
    return trans1.text

def data():
    s = comb_sor.get()  # Correct the missing parentheses to call the get method
    d = comb_des.get()  # Correct the missing parentheses to call the get method
    masg = sor_txt.get(1.0, END)
    textget = change(text=masg, src=s, dest=d)  # Correct argument names
    des_txt.delete(1.0, END)
    des_txt.insert(END, textget)

root = Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg='lightblue')

lab_txt = Label(root, text="Translator", font=("Calibri", 40, "bold"), bg="lightblue")
lab_txt.place(x=100, y=40, height=50, width=300)

frame = Frame(root).pack(side=BOTTOM)

lab_txt = Label(root, text="Source Text", font=("Calibri", 20, "bold"), fg="black", bg="lightblue")
lab_txt.place(x=100, y=100, height=30, width=300)

sor_txt = Text(frame, font=("Calibri", 20, "bold"), wrap=WORD)
sor_txt.place(x=10, y=140, height=150, width=480)

list_txt = list(LANGUAGES.values())
comb_sor = ttk.Combobox(frame, values=list_txt)  # Corrected argument name
comb_sor.place(x=10, y=300, height=40, width=150)
comb_sor.set("english")

button_change = Button(frame, text="Translate", relief=RAISED, command=data)
button_change.place(x=170, y=300, height=40, width=150)

comb_des = ttk.Combobox(frame, values=list_txt)  # Corrected argument name
comb_des.place(x=330, y=300, height=40, width=150)
comb_des.set("english")

lab_txt = Label(root, text="Destination Text", font=("Calibri", 20, "bold"), fg="black", bg="lightblue")
lab_txt.place(x=100, y=360, height=30, width=300)

des_txt = Text(frame, font=("Calibri", 20, "bold"), wrap=WORD)
des_txt.place(x=10, y=400, height=160, width=480)

root.mainloop()
