import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt

def show_chart():
    file_path = filedialog.askopenfilename()
    with open(file_path, 'r', encoding="utf-8") as file:
        data = file.read().split('\n')[1:7]
        print(f"data: {data}")
        values = [int(item.split(')')[1]) for item in data if item != '']
        print(f"values: {values}")
        plt.plot(range(1, len(values)+1), values, marker='o')
        plt.xlabel('Номер вопроса')
        plt.ylabel('Баллы')
        plt.title('График успеваемости группы')
        plt.show()

root = tk.Tk()
root.title('График успеваемости группы')

btn = tk.Button(root, text='Показать график', command=show_chart)
btn.pack()
btn = tk.Button(root, text='Отсортировать файл', command=sort_file_text)

root.mainloop()

