import tkinter as tk
from tkinter import messagebox as mb
import random

attempts_left = 5
secret_number = random.randint(1, 10)

too_high_messages = [
    'Я загадал совсем другое число!\nПопробуй ещё разочек! :)', 
    'Нет-нет, мое число меньше!\nПробуй ещё!', 
    'А вот и не угадал!\nДам подсказку, моё число меньше!', 
    'Дай подумать...\nНет, моё число другое!', 
    'Эй, ну куда так много!\nЯ загадал число поменьше!', 
    'Другое! Вот только не скажу, какое)', 
    'Нет, я загадал другое число!\nПопробуй назвать число поменьше!'
]

too_low_messages = [
    'А вот и нет! Мое число больше!', 
    'Маловато будет...\nДавай ещё разок!', 
    'Нет, мое число другое...\nДавай ещё раз!', 
    'Нет-нет! Совсем не то!\nПодсказка: мое число больше!', 
    'Не угадал! Бери число побольше!', 
    'А вот и не угадал, хи-хи!', 
    'Давай ещё разочек!\nМое число чуть-чуть больше!', 
    'Хм-хм...\nНет, мое число больше!'
]

win_messages = [
    'Ура! Ты угадал!', 
    'Молодец, ты угадал!', 
    'Поздравляю, ты победил! =3', 
    'Угадал!', 
    'Как ты догадался? Правильно! :)'
]

lose_messages = [
    'Не расстраивайся!\nПовезет в другой раз!', 
    'Попытки кончились!\nТы проиграл! :(', 
    'GAME OVER!', 
    'Игра окончена!', 
    'Эх, попытки кончились!\nНичего, повезёт в другой раз!'
]

new_game_messages = [
    'Я загадал новое число!\nУгадай, какое!', 
    'Погоди секундочку...\nВсё, я загадал новое число!', 
    'Попробуем ещё раз! Начинай!', 
    'Сыграем ещё раз! \nЯ загадал новое число!'
]

greeting_messages = [
    'Привет! Я загадал число от 1 до 10!\nПопробуешь угадать? :-)', 
    'Привет! Сыграем в угадай-ку?\nЯ уже загадал число!', 
    'Спорим, не угадаешь, какое число я задумал? :D'
]

duplicate_messages = [
    'Уже было!', 
    'Не, это уже было...',
    'Давай другое! Это уже было! ;)', 
    'Было!', 
    'Ты уже вводил это число! :)', 
    'Дай подумать… Нет, это уже было!', 
    'Ну нет же!', 
    'А вот и нет! :)', 
    'А вот и не угадал! :D', 
    'Говорил же, не то!'
]

guessed_numbers = []
duplicate_numbers = []

def show_help():
    mb.showinfo(
        title="Справка", 
        message="Инструкция", 
        detail="1. Введи число от 1 до 10.\n2. Нажми на клавишу Enter.\n3. Используй кнопку «Новая игра»,\nчтобы начать заново."
    )

def show_rules():
    mb.showinfo(
        title="Справка", 
        message="Правила игры", 
        detail="1. Запрещены лишние символы, кроме цифр.\n2. Нельзя вводить числа меньше нуля или больше десяти!"
    )

def restart_game():
    global secret_number
    secret_number = random.randint(1, 10)
    answer = mb.askyesno(
        title="Новая игра", 
        message="Ты действительно хочешь начать заново?"
    )
    if answer:
        guessed_numbers.clear()
        duplicate_numbers.clear()
        global attempts_left
        attempts_left = 5
        guess_label.config(text="Думаю, ты загадал число:")
        attempts_entry.config(state=tk.NORMAL)
        attempts_entry.delete(0, tk.END)
        attempts_var.set(str(attempts_left))
        attempts_entry.config(state=tk.DISABLED)
        message_text.config(state=tk.NORMAL)
        message_text.delete("1.0", tk.END)
        message_text.insert("1.0", random.choice(new_game_messages))
        message_text.config(state=tk.DISABLED)
        number_entry.config(state=tk.NORMAL)
        number_entry.delete(0, tk.END)
        number_entry.bind('<Return>', on_enter)
        number_entry.focus()

def check_duplicates():
    for num in guessed_numbers:
        if guessed_numbers.count(num) > 1 and num not in duplicate_numbers:
            duplicate_numbers.append(num)

def play_game():
    try:
        guess = int(number_entry.get())
        number_entry.delete(0, tk.END)
        if guess <= 0:
            mb.showerror(title="Ошибка", message="Число должно быть больше 0!")
            return
        elif guess > 10:
            mb.showerror(title="Ошибка", message="Число не может быть больше 10!")
            return
        guessed_numbers.append(guess)
        check_duplicates()
        global attempts_left
        if guess not in duplicate_numbers:
            attempts_left -= 1
        if guess in duplicate_numbers:
            message_text.config(state=tk.NORMAL)
            message_text.delete("1.0", tk.END)
            message_text.insert("1.0", random.choice(duplicate_messages))
            message_text.config(state=tk.DISABLED)
            return
        if guess > secret_number and 0 < guess < 11:
            update_ui(attempts_left, random.choice(too_high_messages))
        elif guess < secret_number and 0 < guess < 11:
            update_ui(attempts_left, random.choice(too_low_messages))
        elif guess == secret_number:
            update_ui(attempts_left, random.choice(win_messages))
            number_entry.config(state="disabled")
            number_entry.unbind('<Return>')
        if attempts_left == 0 and guess != secret_number:
            number_entry.delete(0, tk.END)
            number_var.set(str(secret_number))
            guess_label.config(text="Загаданное мной число:")
            number_entry.config(state="disabled")
            message_text.config(state=tk.NORMAL)
            message_text.delete("1.0", tk.END)
            message_text.insert("1.0", random.choice(lose_messages))
            message_text.config(state=tk.DISABLED)
            number_entry.unbind('<Return>')
    except ValueError:
        mb.showerror(
            title="Ошибка ввода!", 
            message="Убедись в том, что ты ввёл все данные верно!"
        )

def update_ui(attempts, message):
    attempts_entry.config(state=tk.NORMAL)
    attempts_entry.delete(0, tk.END)
    attempts_var.set(str(attempts))
    attempts_entry.config(state=tk.DISABLED)
    message_text.config(state=tk.NORMAL)
    message_text.delete("1.0", tk.END)
    message_text.insert("1.0", message)
    message_text.config(state=tk.DISABLED)

def on_enter(event):
    play_game()

root = tk.Tk()
root.title("Угадай-ка!")
root.geometry("305x130")
root.resizable(width=False, height=False)

number_var = tk.StringVar()
attempts_var = tk.StringVar()

menubar = tk.Menu(root)
helpmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Справка", menu=helpmenu)
menubar.add_command(label="Новая игра", command=restart_game)
helpmenu.add_command(label="Инструкция", command=show_help)
helpmenu.add_command(label="Правила игры", command=show_rules)
root.config(menu=menubar)

attempts_label = tk.Label(root, text="У тебя осталось попыток: ")
attempts_label.grid(row=2, column=0, sticky=tk.NW, padx=10, pady=5)

guess_label = tk.Label(root, text="Думаю, ты загадал число:")
guess_label.grid(row=3, column=0, sticky=tk.NW, padx=10, pady=5)

message_text = tk.Text(width=35, height=3)
message_text.grid(row=1, column=0, padx=10, pady=5, sticky=tk.NW)
message_text.insert("1.0", random.choice(greeting_messages))
message_text.config(state=tk.DISABLED)

attempts_entry = tk.Entry(root, width=10, justify=tk.CENTER, textvariable=attempts_var)
attempts_entry.config(disabledbackground="white", disabledforeground="black", state=tk.DISABLED)
attempts_entry.grid(row=2, column=0, sticky=tk.NW, padx=230, pady=5)
attempts_var.set(str(attempts_left))

number_entry = tk.Entry(root, width=10, justify=tk.CENTER, textvariable=number_var)
number_entry.grid(row=3, column=0, sticky=tk.NW, padx=230, pady=5)
number_entry.configure(disabledbackground="white", disabledforeground="black")
number_entry.focus()
number_entry.bind('<Return>', on_enter)

root.mainloop()
