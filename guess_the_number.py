import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
import random

count = 5
randnum = random.randint(1, 10)

list = ['Слишком большое! Пробуй ещё!', 'Нет, моё число меньше!', 'Нет, это не такое большое число...', 'Ну не-ее, куда так много?']
list2 = ['Маловато будет...', 'Неа, мое число больше!', 'Не угадал, мое число больше!', 'Не угадал, бери число побольше)']

def play():
    
    global count
    count = count - 1
    
    number = int(num.get())
    
    if number > randnum:
    	
    	attempts.configure(state = NORMAL)
    	attempts.delete("1.0", END)
    	attempts.insert("1.0", "     " + str(count))
    	attempts.configure(state = DISABLED)

    	text.configure(state = NORMAL)
    	text.delete("1.0", END)
    	text.insert("1.0", random.choice(list))
    	text.configure(state = DISABLED)
    	
    if number < randnum:
    	
    	attempts.configure(state = NORMAL)
    	attempts.delete("1.0", END)
    	attempts.insert("1.0", "     " + str(count))
    	attempts.configure(state = DISABLED)

    	text.configure(state = NORMAL)
    	text.delete("1.0", END)
    	text.insert("1.0", random.choice(list2))  
    	text.configure(state = DISABLED)
    	    	
    if number == randnum:
    	
    	attempts.configure(state = NORMAL)
    	attempts.delete("1.0", END)
    	attempts.insert("1.0", "     ", str(count))
    	attempts.configure(state = DISABLED)

    	text.configure(state = NORMAL)
    	text.delete("1.0", END)
    	text.insert("1.0", "Молодец, ты угадал!")
    	text.configure(state = DISABLED)  
   
    if count == 0:
    	answer = mb.askyesno(title = "Вопрос", message = "lol", detail = "lal")
    	text.configure(state = NORMAL)
    	text.delete("1.0", END)
    	text.insert("1.0", "Game over")
    	text.configure(state = DISABLED)
    	R.configure(state = DISABLED) 	  	
    	
window = Tk()

#Текстовые надписи

l1 = Label(window, text = "Угадай-ка!")
l1.grid(row = 0, column = 0, padx = 270, pady = 7, sticky = NW)

l2 = Label(window, text="У тебя осталось попыток: ") 
l2.grid(row = 2, column = 0, sticky = NW, padx = 70, pady = 7)

l3 = Label(window, text="Думаю, ты загадал число:")
l3.grid(row = 3, column = 0, sticky = NW, padx = 70, pady = 7)

#Текстовый виджет

text = Text(width = 35, height = 3)
text.grid(row = 1, column = 0, padx = 70,pady = 5, sticky = NW)
text.insert("1.0", "Привет!")
text.configure(state = DISABLED)    	

attempts = Text(window, width = 11, height = 1)
attempts.grid(row = 2, column = 0, sticky = NW, padx = 450, pady = 7)
attempts.insert("1.0", "     5")
attempts.configure(state = DISABLED)    
#Поле ввода

num = Entry(window, width = 10, justify = CENTER)
num.grid(row = 3, column = 0, sticky = NW, padx = 457, pady = 7)
num.focus()

#Кнопки

R = Button(window, width = 16, text = "Готово", command = lambda: play())
R.grid(row = 4, column = 0, sticky = NW, padx = 180, pady = 7)

window.mainloop()
