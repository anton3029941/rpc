import random
from tkinter import *
score = [0, 0]
tk = Tk()


def rockf():
    rand = random.randint(0, 2)
    if rand == 0:
        label['text'] = "Камень; Ничья"
    elif rand == 1:
        label['text'] = "Ножницы; Победа"
        score[0] += 1
        scoreL['text'] = str(score[0]) + " | " + str(score[1])
    else:
        label['text'] = "Бумага; Поражение"
        score[1] += 1
        scoreL['text'] = str(score[0]) + " | " + str(score[1])


def scicf():
    rand = random.randint(0, 2)
    if rand == 0:
        label['text'] = "Камень; Поражение"
        score[1] += 1
        scoreL['text'] = str(score[0]) + " | " + str(score[1])
    elif rand == 1:
        label['text'] = "Ножницы; Ничья"
    else:
        label['text'] = "Бумага; Победа"
        score[0] += 1
        scoreL['text'] = str(score[0]) + " | " + str(score[1])


def paperf():
    rand = random.randint(0, 2)
    if rand == 0:
        label['text'] = "Камень; Победа"
        score[0] += 1
        scoreL['text'] = str(score[0]) + " | " + str(score[1])
    elif rand == 1:
        label['text'] = "Ножницы; Поражение"
        score[1] += 1
        scoreL['text'] = str(score[0]) + " | " + str(score[1])
    else:
        label['text'] = "Бумага; Ничья"


tk.geometry('1200x800')

label = Label(text="", font=("Arial", 50))
label.pack()

scoreL = Label(text="0 | 0", font=("Arial", 32))
scoreL.pack()

btn1 = Button(text="Камень", activebackground='gray', bg="black", fg="white", font=("Comic Sans MS", 50), command=rockf)
btn1.place(x=100, y=400)
btn2 = Button(text="Ножницы",activebackground='gray', bg="black", fg="white",font=("Comic Sans MS", 50), command=scicf)
btn2.place(x=400, y=400)
btn3 = Button(text="Бумага", activebackground='gray', bg="black", fg="white",font=("Comic Sans MS", 50), command=paperf)
btn3.place(x=780, y=400)

tk.mainloop()
