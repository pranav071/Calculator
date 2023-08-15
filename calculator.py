from tkinter import *
app = Tk()
app.title('calculator')
e = Entry(app, width=30)
e.grid(row=0, column=0, columnspan=3,
padx=10, pady=10)
str_ = ""
sum_1 = ""

def num(x):
num = e.get()
e.delete(0, END)
e.insert(END, str(num) + str(x))

def clear():
e.delete(0, END)

def fun(y):
global str_
if y == "+" or "-" or "x" or "/":
str_ = y
else:
str_ = "error"
prod()

def equals():
sum_2 = e.get()
e.delete(0, END)
if str_ == "+":
e.insert(END, int(int(sum_1) +
int(sum_2)))
elif str_ == "-":
e.insert(END, int(int(sum_1) -
int(sum_2)))
elif str_ == "/":
e.insert(END, float(int(sum_1) /
int(sum_2)))
elif str_ == "x":
e.insert(END, int(int(sum_1) *
int(sum_2)))
else:
e.insert(END, "error")

def prod():
global sum_1
sum_1 = e.get()
e.delete(0, END)

btn_1 = Button(app, text='1', width=10,
command=lambda: num("1")).grid(row=1,
column=0)
btn_2 = Button(app, text='2', width=10,
command=lambda: num("2")).grid(row=1,
column=1)
btn_3 = Button(app, text='3', width=10,
command=lambda: num("3")).grid(row=1,
column=2)
btn_4 = Button(app, text='4', width=10,
command=lambda: num("4")).grid(row=2,
column=0)

btn_5 = Button(app, text='5', width=10,
command=lambda: num("5")).grid(row=2,
column=1)
btn_6 = Button(app, text='6', width=10,
command=lambda: num("6")).grid(row=2,
column=2)
btn_7 = Button(app, text='7', width=10,
command=lambda: num("7")).grid(row=3,
column=0)
btn_8 = Button(app, text='8', width=10,
command=lambda: num("8")).grid(row=3,
column=1)
btn_9 = Button(app, text='9', width=10,
command=lambda: num("9")).grid(row=3,
column=2)
btn_add = btn_ = Button(app, text='+',
width=10, command=lambda:
fun("+")).grid(row=4, column=0)
btn_0 = Button(app, text='0', width=10,
command=lambda: num("0")).grid(row=4,
column=1)
btn_minus = btn_ = Button(app, text='-'
,

width=10, command=lambda: fun("-
")).grid(row=4, column=2)
btn_divide = Button(app, text='/', width=10,
command=lambda: fun("/")).grid(row=5,
column=0)
btn_multiply = Button(app, text='x',
width=10, command=lambda:
fun("x")).grid(row=5, column=1)
btn_equals = Button(app, text='='

, width=10,

command=equals).grid(row=5, column=2)
btn_clear = Button(app, text='clear',
width=33, command=clear).grid(row=6,
column=0, columnspan=3)
app.mainloop()