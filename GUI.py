from tkinter import *


window=Tk("arms")
window.geometry("300x400")
window.title("calculator")
window.config(bg="#BF8104")
label=Label(window,text="",bg="red")
label.grid(row=0,column=0,columnspan=4,ipadx=110,ipady=15,padx=15)



button_ac=Button(window,text="ac",width=9,height=3)
button9=Button(window,text="9",width=3,height=3)
button8=Button(window,text="8",width=3,height=3)
button7=Button(window,text="7",width=3,height=3)
button6=Button(window,text="6",width=3,height=3)
button5=Button(window,text="5",width=3,height=3)
button4=Button(window,text="4",width=3,height=3)
button3=Button(window,text="3",width=3,height=3)
button2=Button(window,text="2",width=3,height=3)
button1=Button(window,text="1",width=3,height=3)
button0=Button(window,text="0",width=3,height=3)
button_dot=Button(window,text=".",width=3,height=3)

button_plus=Button(window,text="+",width=3,height=3)
button_equal=Button(window,text="=",width=3,height=3)
button_mainus=Button(window,text="-",width=3,height=3)
button_div=Button(window,text="÷",width=3,height=3)
button_mul=Button(window,text="x",width=3,height=3)



button_ac.grid(row=1,column=0,columnspan=3,ipadx=36)
button9.grid(row=2,column=0)
button8.grid(row=2,column=1)
button7.grid(row=2,column=2)
button6.grid(row=3,column=0)
button5.grid(row=3,column=1)
button4.grid(row=3,column=2)
button3.grid(row=4,column=0)
button2.grid(row=4,column=1)
button1.grid(row=4,column=2)
button0.grid(row=5,column=0,columnspan=2,ipadx=31)
button_dot.grid(row=5,column=2)

button_equal.grid(row=5,column=3)
button_plus.grid(row=4,column=3)
button_mainus.grid(row=3,column=3)
button_mul.grid(row=2,column=3)
button_div.grid(row=1,column=3)

window.mainloop()
