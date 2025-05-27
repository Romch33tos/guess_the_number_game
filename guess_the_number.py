import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
import random

count = 5

randnum = random.randint(1, 10)

#Списки с фразами

list = ['Я загадал совсем другое число!\nПопробуй ещё разочек! :)', 'Нет-нет, мое число меньше!\nПробуй ещё!', 'А вот и не угадал!\nДам подсказку, моё число меньше!', 'Дай подумать...\nНет, моё число другое!', 'Эй, ну куда так много!\nЯ загадал число поменьше!', 'Другое! Вот только не скажу, какое)', 'Нет, я загадал другое число!\nПопробуй назвать число поменьше!']

list2 = ['А вот и нет! Мое число больше!', 'Маловато будет...\nДавай ещё разок!', 'Нет, мое число другое...\nДавай ещё раз!', 'Нет-нет! Совсем не то!\nПодсказка: мое число больше!', 'Не угадал! Бери число побольше!', 'А вот и не угадал, хи-хи!', 'Давай ещё разочек!\nМое число чуть-чуть больше!', 'Хм-хм...\nНет, мое число больше!']

list3 = ['Ура! Ты угадал!', 'Молодец, ты угадал!', 'Поздравляю, ты победил! =3', 'Угадал!', 'Как ты догадался? Правильно! :)']

list4 = ['Не расстраивайся!\nПовезет в другой раз!', 'Попытки кончились!\nТы проиграл! :(', '                                               GAME OVER!', 'Игра окончена!', 'Эх, попытки кончились!\nНичего, повезёт в другой раз!']

list5 = ['Я загадал новое число!\nУгадай, какое!', 'Погоди секундочку...\nВсё, я загадал новое число!', 'Попробуем ещё раз! Начинай!', 'Сыграем ещё раз! \nЯ загадал новое число!']

list6 = ['Ещё!', 'Сейчас угадаю!', 'Вот сейчас точно угадаю!', 'Ещё разочек!', 'Ещё раз!', 'Угадал?', 'А это?', 'Я угадал?']

#Инструкция

def how_to_use(): 
	answer = mb.showinfo(title = "Справка", message = "Инструкция", detail = "1. Введи число от 1 до 10.\n2. Нажми на кнопку «Играть».\n3. Если у тебя кончатся попытки, ты\nможешь начать заново, но уже с \nдругим числом ;-)\n4. Используй кнопку «Выйти»,\nчтобы закрыть игру.")

#Правила игры
def game_rules(): 
	answer = mb.showinfo(title = "Справка", message = "Правила игры", detail = "1. Запрещены лишние символы,\nкроме цифр\n2. Нельзя вводить числа меньше\nнуля или больше десяти!")

#Функция выхода

def exit():
        answer = mb.askyesno( title="Выход", message="Ты действительно хочешь\n         выйти из игры?")
        if answer == True:
        	root.quit()
        else:
        	pass

#Начать заново

def restart():
    global randnum   
    randnum = random.randint(1, 10)  
    answer = mb.askyesno(title = "Новая игра", message = "Ты действительно хочешь\n        начать заново? ")
    if answer == True:
    	   global count
    	   count = 5
    	   l3.configure(text="Думаю, ты загадал число:")   	   
    	   attempts.configure(state = NORMAL)
    	   attempts.delete(0, END)
    	   txt2.set(str(count))
    	   attempts.configure(state = DISABLED)
    	   text.configure(state = NORMAL)
    	   text.delete("1.0", END)
    	   text.insert("1.0", random.choice(list5))
    	   text.configure(state = DISABLED)
    	   num.configure(state = NORMAL)
    	   num.delete(0, END)
    	   R.configure(state = NORMAL, text = random.choice(list6))
    
#Игра

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
    	R.configure(text = random.choice(list6))
    	attempts.configure(state = NORMAL)
    	attempts.delete(0, END)
    	txt2.set(str(count))
    	attempts.configure(state = DISABLED)

    	text.configure(state = NORMAL)
    	text.delete("1.0", END)
    	text.insert("1.0", random.choice(list))
    	text.configure(state = DISABLED)
    	
    if n < randnum and n > 0 and n < 11:
    	R.configure(text = random.choice(list6))
    	attempts.configure(state = NORMAL)
    	attempts.delete(0, END)
    	txt2.set(str(count))
    	attempts.configure(state = DISABLED)

    	text.configure(state = NORMAL)
    	text.delete("1.0", END)
    	text.insert("1.0", random.choice(list2))  
    	text.configure(state = DISABLED)
    	    	
    if n == randnum and n > 0 and n < 11:
    	attempts.configure(state = NORMAL)
    	attempts.delete(0, END)
    	txt2.set(str(count))
    	attempts.configure(state = DISABLED)
    	R.configure(text = "Победа!")
    	text.configure(state = NORMAL)
    	text.delete("1.0", END)
    	text.insert("1.0", random.choice(list3))
    	text.configure(state = DISABLED)
    	num.configure(state = "disabled")
    	R.configure(state = DISABLED) 

    if count == 0 and n != randnum:  	
            R.configure(text = "Попытки кончились")
            num.delete(0, END)
            txt.set(str(randnum))
            l3.configure(text = "Загаданное мной число:")
            num.configure(state = "disabled")
            text.configure(state = NORMAL)
            text.delete("1.0", END)
            text.insert("1.0", random.choice(list4))               
            text.configure(state = DISABLED)
            R.configure(state = DISABLED) 	  	
#Графический дизайн 
    	
root = Tk()
txt = StringVar()
txt2 = StringVar()

#Меню

menubar = Menu(root)

helpmenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Справка", menu=helpmenu)

menubar.add_command(label = "Новая игра", command = restart)

menubar.add_command(label = "Выйти", command = exit)

helpmenu.add_command(label="Инструкция", command=how_to_use)

helpmenu.add_command(label= "Правила игры", command=game_rules)

root.config(menu = menubar)

#Текстовые надписи

l1 = Label(root, text = "Угадай-ка!")
l1.grid(row = 0, column = 0, padx = 270, pady = 7, sticky = NW)

l2 = Label(root, text="У тебя осталось попыток: ") 
l2.grid(row = 2, column = 0, sticky = NW, padx = 70, pady = 7)

l3 = Label(root, text="Думаю, ты загадал число:")
l3.grid(row = 3, column = 0, sticky = NW, padx = 70, pady = 7)

#Текстовый виджет

text = Text(width = 35, height = 3)
text.grid(row = 1, column = 0, padx = 70,pady = 5, sticky = NW)
text.insert("1.0", "Привет! Я загадал число от 1 до 10!\nПопробуешь угадать? :-)")
text.configure(state = DISABLED)    	

attempts = Entry(root, width = 10, justify = CENTER, textvariable=txt2)
attempts.configure(disabledbackground="white", disabledforeground="black", state = DISABLED)
attempts.grid(row = 2, column = 0, sticky = NW, padx = 460, pady = 7)
txt2.set(str(count))

#Поле ввода

num = Entry(root, width = 10, justify = CENTER, textvariable=txt)
num.grid(row = 3, column = 0, sticky = NW, padx = 460, pady = 7)
num.configure(disabledbackground="white", disabledforeground="black")
num.focus()

#Кнопки

R = Button(root, width = 20, text = "Играть", command = lambda: play())
R.grid(row = 4, column = 0, sticky = NW, padx = 150, pady = 7)

root.mainloop()
