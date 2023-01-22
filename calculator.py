from tkinter import *
from tkinter import Button

window=Tk("arms")
window.geometry("255x355")
window.title("calculator")
window.config(bg="black")
old1=0
old2=0
nam1=0
nam2=0
value=""
def clicked(nam):
    global nam1,nam2
    nam1=nam
    nam2=nam1
    label = Label(window, text=str(nam), width=28, height=3)
    label.grid(row=0, column=0, columnspan=4, )
    #print(old1)

def plus(pls):
    global nam2,old1,value
    value=pls
    old1=nam2
    clicked("")


def result():
    global old1,nam2,old2,value
    if(value=="+"):
        old2 = float(old1) + float(nam2);
        clicked(old2);
    if(value=="-"):
        old2 = float(old1) - float(nam2);
        clicked(old2);
    if (value == "*"):
        old2 = float(old1) * float(nam2);
        clicked(old2);
    if (value == "/"):
        old2 = float(old1) / float(nam2);
        clicked(old2);


clicked("")

button_ac = Button(window, text="ac", width=9, height=3, command=lambda: clicked(""))
button9 = Button(window, text="9", width=3, height=3, command=lambda: clicked(nam1 + "9"))
button8 = Button(window, text="8", width=3, height=3, command=lambda: clicked(nam1 + "8"))
button7 = Button(window, text="7", width=3, height=3, command=lambda: clicked(nam1 + "7"))
button6 = Button(window, text="6", width=3, height=3, command=lambda: clicked(nam1 + "6"))
button5 = Button(window, text="5", width=3, height=3, command=lambda: clicked(nam1 + "5"))
button4 = Button(window, text="4", width=3, height=3, command=lambda: clicked(nam1 + "4"))
button3 = Button(window, text="3", width=3, height=3, command=lambda: clicked(nam1 + "3"))
button2 = Button(window, text="2", width=3, height=3, command=lambda: clicked(nam1 + "2"))
button1 = Button(window, text="1", width=3, height=3, command=lambda: clicked(nam1 + "1"))
button0 = Button(window, text="0", width=3, height=3, command=lambda: clicked(nam1 + "0"))
button_dot = Button(window, text=".", width=3, height=3, command=lambda: clicked(nam1 + "."))

button_plus = Button(window, text="+", width=3, height=3, command=lambda: plus("+"))
button_equal = Button(window, text="=", width=3, height=3, command=lambda: result())
button_mainus = Button(window, text="-", width=3, height=3, command=lambda: plus("-"))
button_div = Button(window, text="÷", width=3, height=3, command=lambda: plus("/"))
button_mul = Button(window, text="x", width=3, height=3, command=lambda: plus("*"))


button_ac.grid(row=1, column=0, columnspan=3, ipadx=36)
button9.grid(row=2, column=0)
button8.grid(row=2, column=1)
button7.grid(row=2, column=2)
button6.grid(row=3, column=0)
button5.grid(row=3, column=1)
button4.grid(row=3, column=2)
button3.grid(row=4, column=0)
button2.grid(row=4, column=1)
button1.grid(row=4, column=2)
button0.grid(row=5, column=0, columnspan=2, ipadx=31)
button_dot.grid(row=5, column=2)

button_equal.grid(row=5, column=3)
button_plus.grid(row=4, column=3)
button_mainus.grid(row=3, column=3)
button_mul.grid(row=2, column=3)
button_div.grid(row=1, column=3)


window.mainloop()
