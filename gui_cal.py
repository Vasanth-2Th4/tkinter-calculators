import tkinter as tk
from tkinter import *

def click(num):
    bar.insert(tk.END,num)
    global expression
 
    # concatenation of string
    expression = expression + str(num)
 
    # update the expression by using set method
    equation.set(expression)

def clear():
    global expression
    expression = ""
    equation.set("")

def clear1():
    global expression
    expression = expression[:-1]
    equation.set(expression)

def equal():
    # Try and except statement is used
    # for handling the errors like zero
    # division error etc.
 
    # Put that code inside the try block
    # which may generate the error
    try:
 
        global expression
 
        # eval function evaluate the expression
        # and str function convert the result
        # into string
        total = str(eval(expression))
 
        equation.set(total)
 
        # initialize the expression variable
        # by empty string
        expression = ""
 
    # if error is generate then handle
    # by the except block
    except:
 
        equation.set(" error ")
        expression = ""

expression = ''
win = tk.Tk()
win.geometry('426x300')
equation = tk.StringVar()
lb = tk.Label(win,text='''
CALCULATOR''')
lb.place(x=170,y=1)
bar = tk.Entry(win,textvariable=equation)
bar.place(x=150,y=50)
btn = tk.Button(win,text='   7   ',command=lambda: click(7))
btn.place(x=130,y=80)

btn = tk.Button(win,text='   8   ',command=lambda: click(8))
btn.place(x=180,y=80)
btn = tk.Button(win,text='   9   ',command=lambda: click(9))
btn.place(x=230,y=80)
btn = tk.Button(win,text='   4   ',command=lambda: click(4))
btn.place(x=130,y=110)
btn = tk.Button(win,text='   5   ',command=lambda: click(5))
btn.place(x=180,y=110)
btn = tk.Button(win,text='   6   ',command=lambda: click(6))
btn.place(x=230,y=110)
btn = tk.Button(win,text='   1   ',command=lambda: click(1))
btn.place(x=130,y=140)
btn = tk.Button(win,text='   2   ',command=lambda: click(2))
btn.place(x=180,y=140)
btn = tk.Button(win,text='   3   ',command=lambda: click(3))
btn.place(x=230,y=140)
btn = tk.Button(win,text='   0   ',command=lambda: click(0))
btn.place(x=180,y=170)
btn = tk.Button(win,text='   C   ',command=clear)
btn.place(x=130,y=170)

btn = tk.Button(win,text=' Del ',command=clear1)
btn.place(x=230,y=170)

btn = tk.Button(win,text='   /   ',command=lambda:click("/"))
btn.place(x=280,y=80)

btn = tk.Button(win,text='   x   ',command=lambda: click('*'))
btn.place(x=280,y=110)

btn = tk.Button(win,text='   -   ',command=lambda: click('-'))
btn.place(x=280,y=140)

btn = tk.Button(win,text='   +   ',command=lambda: click('+'))
btn.place(x=280,y=170)

btn = tk.Button(win,text='   %   ',command=lambda: click('%'))
btn.place(x=280,y=200)

btn = tk.Button(win,text='   0   ',command=lambda: click(0))
btn.place(x=180,y=170)

btn = tk.Button(win,text='          =           ',command=equal)
btn.place(x=150,y=200)
lb = tk.Label(win,text=' = ')
lb.place(x=280,y=50)
lb = tk.Label(win,text='\"value\"')
lb.place(x=300,y=50)

win.mainloop()


