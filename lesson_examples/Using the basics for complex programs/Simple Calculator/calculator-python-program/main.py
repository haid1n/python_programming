"""
Dimensions of Buttons -
    height: 1
    width: 3 (or (height*2)+1)

Distance between two buttons -
    In Rows: 60
    In Columns: 60

Font size in buttons: 9
"""

# Importing everything from tkinter
from tkinter import *
from tkinter.messagebox import showerror

# Creating the functions
def add_text(text, strvar: StringVar):
    strvar.set(f'{strvar.get()}{text}')


def submit(entry: Entry, strvar: StringVar):
    operation = entry.get()
    try:
        strvar.set(f"{strvar.get()}={eval(operation)}")
    except:
        showerror('Error!', 'Please enter a properly defined equation!')


# Creating a GUI
root = Tk()
root.title("PythonGeeks Calculator")
root.geometry('250x500')
root.resizable(0, 0)
root.configure(background='LightCyan2')

# StringVar variables
entry_strvar = StringVar(root)

# Defining the top
Label(root, text='PythonGeeks Calculator', font=("Comic Sans MS", 15), bg='LightCyan2').place(x=15, y=0)

Label(root, text='Press \'x\' twice for exponentiation', font=("Georgia", 10), bg='LightCyan2').place(x=20, y=30)

eqn_entry = Entry(root, justify=RIGHT, textvariable=entry_strvar, width=25, font=12, state='disabled')
eqn_entry.place(x=10, y=70)

# Number Buttons
Button(root, height=2, width=5, text='7', font=9, bg='Gold', command=lambda: add_text("7", entry_strvar)).place(x=5,
                                                                                                              y=170)

Button(root, height=2, width=5, text='8', font=9, bg='Gold', command=lambda: add_text('8', entry_strvar)).place(x=65, y=170)

Button(root, height=2, width=5, text='9', font=9, bg='Gold', command=lambda: add_text('9', entry_strvar)).place(x=125, y=170)

Button(root, height=2, width=5, text='4', font=9, bg='Gold', command=lambda: add_text('4', entry_strvar)).place(x=5, y=225)

Button(root, height=2, width=5, text='5', font=9, bg='Gold', command=lambda: add_text('5', entry_strvar)).place(x=65, y=225)

Button(root, height=2, width=5, text='6', font=9, bg='Gold', command=lambda: add_text('6', entry_strvar)).place(x=125, y=225)

Button(root, height=2, width=5, text='1', font=9, bg='Gold', command=lambda: add_text('1', entry_strvar)).place(x=5, y=280)

Button(root, height=2, width=5, text='2', font=9, bg='Gold', command=lambda: add_text('2', entry_strvar)).place(x=65, y=280)

Button(root, height=2, width=5, text='3', font=9, bg='Gold', command=lambda: add_text('3', entry_strvar)).place(x=125, y=280)

Button(root, height=2, width=5, text='0', font=9, bg='Gold', command=lambda: add_text('0', entry_strvar)).place(x=5, y=340)

# Operator Buttons
add = Button(root, height=2, width=5, text='+', font=9, bg='DarkOrange', command=lambda: add_text('+', entry_strvar))
add.place(x=195, y=340)

subtract = Button(root, height=2, width=5, text='-', font=9, bg='DarkOrange', command=lambda: add_text('-', entry_strvar))
subtract.place(x=195, y=280)

multiply = Button(root, height=2, width=5, text='x', font=9, bg='DarkOrange', command=lambda: add_text('*', entry_strvar))
multiply.place(x=195, y=225)

divide = Button(root, height=2, width=5, text='/', bg='DarkOrange', font=9, command=lambda: add_text('/', entry_strvar))
divide.place(x=195, y=170)

decimal = Button(root, height=2, width=5, text='.', font=9, bg='DarkOrange', command=lambda: add_text('.', entry_strvar))
decimal.place(x=65, y=340)

bracket_open = Button(root, height=2, width=5, text='(', font=9, bg='DarkOrange', command=lambda: add_text('.', entry_strvar))
bracket_open.place(x=65, y=110)

bracket_close = Button(root, height=2, width=5, text=')', font=9, bg='DarkOrange', command=lambda: add_text('.', entry_strvar))
bracket_close.place(x=125, y=110)

# Equal, C and AC buttons
equal = Button(root, height=2, width=5, text='=', font=9, bg='Blue', command=lambda: submit(eqn_entry, entry_strvar))
equal.place(x=125, y=340)

clear = Button(root, height=2, width=5, text='C', font=9, bg='OrangeRed',
               command=lambda: entry_strvar.set(entry_strvar.get()[:-1]))
clear.place(x=195, y=110)

AC_btn = Button(root, height=2, width=5, text='AC', font=9, bg='Red', command=lambda: entry_strvar.set(''))
AC_btn.place(x=5, y=110)

# Ok Button
ok_btn = Button(root, height=2, width=22, text='Ok', font=9, bg='CadetBlue', command=lambda: root.destroy())
ok_btn.place(x=20, y=420)

# Updating root
root.update()
root.mainloop()
