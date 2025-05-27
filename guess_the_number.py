import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
import random

count = 5
randnum = random.randint(1, 10)

list = ['Я загадал совсем другое число!\nПопробуй ещё разочек! :)', 'Нет-нет, мое число меньше!\nПробуй ещё!', 'А вот и не угадал!\nДам подсказку, моё число меньше!', 'Дай подумать...\nНет, моё число другое!', 'Эй, ну куда так много!\nЯ загадал число поменьше!', 'Другое! Вот только не скажу, какое)', 'Нет, я загадал другое число!\nДавай ещё раз!', 'Нетушки! Давай ещё раз!']

list2 = ['А вот и нет! Мое число больше!', 'Маловато будет...\nДавай ещё разок!', 'Нет, мое число другое...\nДавай ещё раз!', 'Нет-нет! Совсем не то!\nПодсказка: мое число больше!', 'Не угадал! Бери число побольше!', 'А вот и не угадал, хи-хи!', 'Давай ещё разочек!', 'Хм-хм...\nНет, мое число больше!']

list3 = ['Ура! Ты угадал!', 'Молодец, ты угадал!', 'Поздравляю, ты победил! =3', 'Угадал!', 'Как ты догадался? Правильно! :)']

list4 = ['Не расстраивайся!\nПовезет в другой раз!', 'Попытки кончились!\nТы проиграл! :(', '                                               GAME OVER!', 'Игра окончена!', 'Эх, попытки кончились!\nНичего, повезёт в другой раз!']

def how_to_use(): 
	answer = mb.showinfo(title = "Справка", message = "Инструкция", detail = "1. Введи число от 1 до 10.\n2. Нажми на кнопку «Играть».\n3. Используй кнопку «Выйти»,\nчтобы закрыть игру.")

def game_rules(): 
	answer = mb.showinfo(title = "Справка", message = "Правила игры", detail = "1. Запрещены лишние символы,\nкроме цифр\n2. Нельзя вводить числа меньше\nнуля или больше десяти!")

def exit():
        answer = mb.askyesno( title="Выход", message="Вы действительно хотите выйти?")
        if answer == True:
        	window.quit()
        else:
        	pass

def play():
    n = int(num.get())
    if n <= 0:
        answer = mb.showerror(title = "Ошибка", message = "Число должно быть больше 0!")
    elif n > 10:
        answer = mb.showerror(title = "Ошибка", message = "Число не может быть больше 10!")   
    else:
        global count
        count = count - 1
      
    if n > randnum and n > 0 and n < 11:
    	R.configure(text = "Ещё раз!")
    	attempts.configure(state = NORMAL)
    	attempts.delete("1.0", END)
    	attempts.insert("1.0", "     " + str(count))
    	attempts.configure(state = DISABLED)

    	text.configure(state = NORMAL)
    	text.delete("1.0", END)
    	text.insert("1.0", random.choice(list))
    	text.configure(state = DISABLED)
    	
    if n < randnum and n > 0 and n < 11:
    	R.configure(text = "Ещё раз!")
    	attempts.configure(state = NORMAL)
    	attempts.delete("1.0", END)
    	attempts.insert("1.0", "     " + str(count))
    	attempts.configure(state = DISABLED)

    	text.configure(state = NORMAL)
    	text.delete("1.0", END)
    	text.insert("1.0", random.choice(list2))  
    	text.configure(state = DISABLED)
    	    	
    if n == randnum and n > 0 and n < 11:
    	R.configure(text = "Победа!")
    	text.configure(state = NORMAL)
    	text.delete("1.0", END)
    	text.insert("1.0", random.choice(list3))
    	text.configure(state = DISABLED)
    	R.configure(state = DISABLED) 

    if count == 0:
    	R.configure(text = "Попытки кончились")
    	num.delete(0, END)
    	num.configure(state = "readonly")	
    	text.configure(state = NORMAL)
    	text.delete("1.0", END)
    	text.insert("1.0", random.choice(list4))
    	text.configure(state = DISABLED)
    	R.configure(state = DISABLED) 	  	
    	
window = Tk()

menubar = Menu(window)

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Справка", menu=helpmenu)

menubar.add_command(label = "Выйти", command = exit)

helpmenu.add_command(label="Инструкция", command=how_to_use)

helpmenu.add_command(label= "Правила игры", command=game_rules)

window.config(menu = menubar)

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
text.insert("1.0", "Привет! Я загадал число от 1 до 10!\nПопробуешь угадать? :-)")
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

R = Button(window, width = 16, text = "Играть", command = lambda: play())
R.grid(row = 4, column = 0, sticky = NW, padx = 180, pady = 7)

window.mainloop()
