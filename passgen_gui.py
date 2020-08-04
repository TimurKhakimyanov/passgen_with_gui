#A program for generating passwords with a graphical interface
#August 2020

#Программа для генерации паролей с графическим интерфейсом
#Август  2020 

from tkinter import *
from tkinter.ttk import Combobox 
from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits
from random import choice

def click():
    entrydone.delete(0 , END)
    chars = ascii_letters + digits
    n = int(combonum.get())
    passgen = ''.join(choice(chars) for _ in range(n))
    entrydone.insert(0 , passgen)
    #print(passgen) расскоментируйте для вывода пароля в консоль если нужно
    
windowdone = Tk()
windowdone.title("Password generator")
windowdone.geometry('400x250')
#windowdone.configure(bg = "aqua")  для изменения цвета фона 
entrydone = Entry(windowdone , width = 25)
combonum = Combobox(windowdone)
combonum['values'] = (8,9,10,11,12,13,14,15)
combonum.current(0)
labelins = Label(windowdone , text = "Выберите длину пароля здесь")
btngen = Button(windowdone , text = "generate" , command = click , bg = "white" , fg = "black")
entrydone.place(x=30,y=40)
combonum.place(x=200,y=40)
btngen.place(x=150,y=70)
labelins.place(x=195 , y = 15)


windowdone.mainloop()
