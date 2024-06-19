from tkinter import *
from tkinter import filedialog
def sort_file_text():
    datas = []
    file_path = filedialog.askopenfilename()
    with open(file_path, 'r', encoding="utf-8") as file:
        data = file.read().split('\n')[0:7]
        datas.append(data)
    with open(file_path, 'r', encoding="utf-8") as file:
        data = file.read().split('\n')[7:14]
        datas.append(data)
    with open(file_path, 'r', encoding="utf-8") as file:
        data = file.read().split('\n')[14:21]
        datas.append(data)
        datas.sort()
    # with open(file_path, 'a', encoding="utf-8") as file:
    #     file.writelines(" ")
    with open(file_path, 'w', encoding="utf-8") as file:
        for line in datas:
            for line1 in line:
                file.write("%s\n" % line1)


root = Tk()
btn = Button(root, text='Отсортировать файл', command=sort_file_text)
btn.pack()



root.mainloop()