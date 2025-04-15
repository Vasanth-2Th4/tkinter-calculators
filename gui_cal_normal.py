import tkinter as tk

def add():

    X = bar1.get()
    value1 = int(X)
    print("value1 = ",value1)

    Y = bar2.get()
    value2 = int(Y)
    print("value2 = ",value2)

    lb['text'] = (f'Addition of two numbers = {value1+value2}')
    print(f'sum of two numbers = {value1+value2}')

def sub():

    X = bar1.get()
    value1 = int(X)
    print("value1 = ",value1)

    Y = bar2.get()
    value2 = int(Y)
    print("value2 = ",value2)

    lb['text'] = (f'Subtraction of two numbers = {value1-value2}')
    print(f'sum of two numbers = {value1-value2}')

def mul():

    X = bar1.get()
    value1 = int(X)
    print("value1 = ",value1)

    Y = bar2.get()
    value2 = int(Y)
    print("value2 = ",value2)

    lb['text'] = (f'Multiplication of two numbers = {value1*value2}')
    print(f'sum of two numbers = {value1*value2}')

def div():

    X = bar1.get()
    value1 = int(X)
    print("value1 = ",value1)

    Y = bar2.get()
    value2 = int(Y)
    print("value2 = ",value2)

    lb['text'] = (f'{value1} divided by {value2} = {value1/value2}')
    print(f'sum of two numbers = {value1/value2}')


def click():

    X = bar1.get()
    value1 = int(X)
    print("value1 = ",value1)

    Y = bar2.get()
    value2 = int(Y)
    print("value2 = ",value2)

    lb['text'] = (f'''
Addition of two numbers = {value1+value2}
Subtraction of two numbers = {value1-value2}
Multiplication of two numbers = {value1*value2}
{value1} divided by {value2} = {value1/value2}''')
    print(f'''
Addition of two numbers = {value1+value2}
Subtraction of two numbers = {value1-value2}
Multiplication of two numbers = {value1*value2}
{value1} divided by {value2} = {value1/value2}''')
    


win = tk.Tk()
win.geometry('426x300')

lb = tk.Label(win,text='CALCULATOR')
lb.place(x=180,y=1)

lb1 = tk.Label(win,text='value 1 =')
lb1.place(x=95,y=50)

bar1 = tk.Entry(win)
bar1.place(x=150,y=50)

lb2 = tk.Label(win,text='value 2 =')
lb2.place(x=95,y=80)

bar2 = tk.Entry(win)
bar2.place(x=150,y=80)

lb3 = tk.Label(win,text='OPERATORS :')
lb3.place(x=50,y=115)

btn = tk.Button(win,text='   +   ',command=add)
btn.place(x=40,y=145)

btn = tk.Button(win,text='   -   ',command=sub)
btn.place(x=100,y=145)

btn = tk.Button(win,text='   x   ',command=mul)
btn.place(x=160,y=145)

btn = tk.Button(win,text='   /   ',command=div)
btn.place(x=220,y=145)

btn = tk.Button(win,text='All operators',command=click)
btn.place(x=280,y=145)

lb = tk.Label(win,text='''
Enter value 1 and value 2 
and
click on any one operators to continue''')
lb.place(x=110,y=190)

win.mainloop()
