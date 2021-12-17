import tkinter as tkt
from tkinter import*
from tkinter.constants import CENTER, END
t=tkt.Tk()
temps=""
t.geometry('500x500')
t.title("calulator")
calnum=StringVar()
def press(value):   
    global temps
    temps = temps +str(value)
    num.insert(END, value)
def cal():
    global temps
    addval = str(eval(temps))
    clear()
    temps = ""
    press(addval)
    
def clear():
    global temps
    num.delete(0,END)
    temps=""
num= Entry(t,textvariable=calnum,width=25)
num.place(x=51,y=50)
num.place(height=38)
num.pack() 
b1=Button(t,text='9', command=lambda: press('9'),bd='3', padx=15, pady=15)
b1.place(x=50,y=100)
b2=Button(t,text='8', command=lambda: press('8'),bd='3', padx=15, pady=15)
b2.place(x=100,y=100)
b3=Button(t,text='7',command=lambda: press('7'),bd='3', padx=15, pady=15)
b3.place(x=150,y=100)
b4=Button(t,text='/',command=lambda: press('/'), bd='3', padx=15, pady=15)
b4.place(x=200,y=100)
b5=Button(t,text='6',command=lambda: press('6'), bd='3', padx=15, pady=15)
b5.place(x=50,y=155)
b5=Button(t,text='5',command=lambda: press('5'), bd='3', padx=15, pady=15)
b5.place(x=100,y=155)
b6=Button(t,text='4', command=lambda: press('4'),bd='3', padx=15, pady=15)
b6.place(x=150,y=155)
b1=Button(t,text='x',command=lambda: press('*'), bd='3', padx=15, pady=15)
b1.place(x=200,y=155)
b7=Button(t,text='3', command=lambda: press('3'),bd='3', padx=15, pady=15)
b7.place(x=50,y=210)
b8=Button(t,text='2',command=lambda: press('2'), bd='3', padx=15, pady=15)
b8.place(x=100,y=210)
b9=Button(t,text='1', command=lambda: press('1'),bd='3', padx=15, pady=15)
b9.place(x=150,y=210)
b1=Button(t,text='+',command=lambda: press('+'), bd='3', padx=14, pady=15)
b1.place(x=200,y=210)
b10=Button(t,text='0',command=lambda: press('0'), bd='3', padx=15, pady=15)
b10.place(x=100,y=265)
b1=Button(t,text='%', command=lambda: press('%'),bd='3', padx=14, pady=15)
b1.place(x=148,y=265)
b10=Button(t,text='00',command=lambda: press('00'), bd='3', padx=13, pady=15)
b10.place(x=50,y=265)
b1=Button(t,text='-', command=lambda: press('-'),bd='3', padx=15, pady=15)
b1.place(x=201,y=265)
b1=Button(t,text='Clear', command=lambda: clear(),bd='3',bg='black',fg='white',padx=15, pady=43)
b1.place(x=250,y=100)
b1=Button(t,text='=',command=cal, bd='3',bg='black', fg='white', padx=24, pady=44)
b1.place(x=250,y=210)

t.mainloop()