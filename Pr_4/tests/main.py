import tkinter as tk
from tkinter import messagebox
import json

# Функция для сохранения данных пользователя в файл
def save_data(username, password):
    data = {username: password}

    with open("userdata.txt", "a") as file:
        file.write(json.dumps(data) + "\n")
# Функция для проверки данных пользователя при входе
def login(username, password):
    with open("userdata.txt", "r") as file:
        for line in file:
            data = json.loads(line)
            if username in data and data[username] == password:
                messagebox.showinfo("Успех", "Вы успешно вошли в систему")
                return
        messagebox.showerror("Ошибка", "Неверное имя пользователя или пароль")
# Создание основного окна
root = tk.Tk()
root.title("Авторизация")

# Фрейм для регистрации
register_frame = tk.Frame(root)
register_frame.pack(pady=20)

# Элементы для регистрации
username_label = tk.Label(register_frame, text="Имя пользователя:")
username_label.grid(row=0, column=0)
username_entry = tk.Entry(register_frame)
username_entry.grid(row=0, column=1)

password_label = tk.Label(register_frame, text="Пароль:")
password_label.grid(row=1, column=0)
password_entry = tk.Entry(register_frame, show="*")
password_entry.grid(row=1, column=1)

register_button = tk.Button(register_frame, text="Регистрация", command=lambda: save_data(username_entry.get(), password_entry.get()))
register_button.grid(row=2, column=1)

# Фрейм для входа
login_frame = tk.Frame(root)
login_frame.pack(pady=20)

# Элементы для входа
login_username_label = tk.Label(login_frame, text="Имя пользователя:")
login_username_label.grid(row=0, column=0)
login_username_entry = tk.Entry(login_frame)
login_username_entry.grid(row=0, column=1)

login_password_label = tk.Label(login_frame, text="Пароль:")
login_password_label.grid(row=1, column=0)
login_password_entry = tk.Entry(login_frame, show="*")
login_password_entry.grid(row=1, column=1)

login_button = tk.Button(login_frame, text="Вход", command=lambda: login(login_username_entry.get(), login_password_entry.get()))
login_button.grid(row=2, column=1)

root.mainloop()
