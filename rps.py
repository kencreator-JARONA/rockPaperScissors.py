from tkinter import *
from random import *

def rock():
    opp_rps = randint(1, 3)
    if opp_rps == 1:
        opp.config(text="Opponent: Rock")
        judge.config(text="Draw!")
    elif opp_rps == 2:
        opp.config(text="Opponent: Paper")
        judge.config(text="You Lost!")
    else:
        opp.config(text="Opponent: Scissors")
        judge.config(text="You Won!")

def paper():
    opp_rps = randint(1, 3)
    if opp_rps == 1:
        opp.config(text="Opponent: Rock")
        judge.config(text="You Won!")
    elif opp_rps == 2:
        opp.config(text="Opponent: Paper")
        judge.config(text="Draw!")
    else:
        opp.config(text="Opponent: Scissors")
        judge.config(text="You Lost!")

def scissors():
    opp_rps = randint(1, 3)
    if opp_rps == 1:
        opp.config(text="Opponent: Rock")
        judge.config(text="You Lost!")
    elif opp_rps == 2:
        opp.config(text="Opponent: Paper")
        judge.config(text="You Won!")
    else:
        opp.config(text="Opponent: Scissors")
        judge.config(text="Draw!")

window = Tk()
window.geometry("1000x500")
window.title("Untitled Game")

rockButton = Button(window, text="Rock", font=("Comic Sans MS", 20), command=rock)
paperButton= Button(window, text="Paper", font=("Comic Sans MS", 20), command=paper)
scissorsButton = Button(window, text="Scissors", font=("Comic Sans MS", 20), command=scissors)
opp = Label(window, text="", font=("Comic Sans MS", 20))
judge = Label(window, text="", font=("Comic Sans MS", 20))

rockButton.pack()
paperButton.pack()
scissorsButton.pack()
opp.pack()
judge.pack()

window.mainloop()