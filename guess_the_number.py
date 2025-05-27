from tkinter import *
import random

window = Tk()

l1 = Label(window, text="«Угадай число»")
l1.grid(row = 0, column = 0, padx = 230, pady = 10, sticky = NW)

text = Text(width = 35, height = 1)
text.grid(row = 1, column = 0, padx = 55,pady = 10, sticky = NW)

l3 = Label(window, text="Ты загадал число: ")
l3.grid(row = 2, column = 0, padx = 55, pady = 10, sticky = NW)

num = Entry(window, width = 10, justify = CENTER)
num.grid(row = 2, column = 0, padx = 445, pady = 10, sticky = NW)
num.focus()

text.insert("1.0", "Отгадай число от 1 до 10! :)")

Button(window, state = NORMAL, width = 29, text = "Играть!", command = lambda: play()).grid(row = 3, column = 0, sticky = SW, padx = 63, pady = 10)

list = ['Слишком большое! Пробуй ещё!', 'Нет, моё число меньше!', 'Нет, это не такое большое число...', 'Ну не-ее, куда так много?']
list2 = ['Маловато будет...', 'Неа, мое число больше!', 'Не угадал, мое число больше!', 'Не угадал, бери число побольше)']

random_number = random.randint(1, 10)

def play():
    Button(window, state = NORMAL, width = 29, text = "Ещё раз!", command = lambda: play()).grid(row = 3, column = 0, sticky = SW, padx = 63, pady = 10)
    text.delete("1.0", END)
    users_number = int(num.get())
    if users_number > random_number:
    	text.insert("1.0", random.choice(list))
    if users_number < random_number:
    	text.insert("1.0", random.choice(list2))
    if users_number == random_number:
    	text.insert("1.0", "Молодец, ты угадал!")
    	Button(window, state = DISABLED, width = 29, text = "Ура!", command = lambda: play()).grid(row = 3, column = 0, sticky = SW, padx = 63, pady = 10)
    	
window.mainloop()