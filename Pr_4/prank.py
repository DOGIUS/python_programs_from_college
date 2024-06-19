from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from functools import partial
import os
import json
from os import listdir
from os.path import isfile, join
from prettytable import PrettyTable
from tkinter import filedialog
with open("Lecture №1/Lecture №1.txt", "r", encoding="utf-8") as file1:
    lines1 = [line.rstrip() for line in file1]
with open("Lecture №1/Test_qw.txt", "r" , encoding="utf-8") as file2:
    lines2 = [line.rstrip() for line in file2]
with open("Lecture №2/Lecture №2.txt", "r", encoding="utf-8") as file3:
    lines3 = [line.rstrip() for line in file3]
with open("Lecture №2/Test_qw.txt", "r", encoding="utf-8") as file4:
    lines4 = [line.rstrip() for line in file4]
with open("Lecture №3/Lecture №3.txt", "r", encoding="utf-8") as file5:
    lines5 = [line.rstrip() for line in file5]
with open("Lecture №3/Test_qw.txt", "r", encoding="utf-8") as file6:
    lines6 = [line.rstrip() for line in file6]
with open("final_test.txt", "r", encoding="utf-8") as file7:
    lines7 = [line.rstrip() for line in file7]
# кнопки закрытия окон
def on_closing_for_textbookWindow():
    textbook.destroy()
    registerWindow()
def on_closing_for_themesWindow():
    themes.destroy()
    textbookWindow(g)
def on_closing_for_lectureWindow():
    lecture.destroy()
    themesWindow(themes_titles=saved_theme[0])
    saved_theme.clear()
def on_closing_for_practicalWindow():
    practical.destroy()
    themesWindow(themes_titles=saved_theme[0])
    saved_theme.clear()
def on_closing_for_testWindow():
    test.destroy()
    themesWindow(themes_titles=saved_theme[0])
    saved_theme.clear()
def on_closing_for_itogWindow():
    itog.destroy()
    themesWindow(themes_titles=saved_theme[0])
    saved_theme.clear()
def on_closing_for_usersWindow():
    users.destroy()
    textbookWindow(g)
def on_closing_for_final_itogWindow():
    final_itog.destroy()
    textbookWindow(g)
# кнопки навигации (назад)
def lecture_to_themes():
    lecture.destroy()
    themesWindow(themes_titles=saved_theme[0])
    saved_theme.clear()
def practical_to_lecture():
    practical.destroy()
    lectureWindow(themes_titles=saved_theme[0])
    saved_theme.clear()
def test_to_practical():
    test.destroy()
    practicalWindow(themes_titles=saved_theme[0])
    saved_theme.clear()
def itog_to_test():
    itog.destroy()
    testWindow(themes_titles=saved_theme[0])
    saved_theme.clear()
def users_to_textbook():
    users.withdraw()
    textbookWindow(g)
def final_test_to_textbook():
    final_test.destroy()
    textbookWindow(g)
# кнопки навигации (вперёд)
def lecture_to_practical():
    lecture.withdraw()
    practicalWindow(themes_titles=saved_theme[0])
    saved_theme.clear()
def practical_to_test():
    practical.destroy()
    testWindow(themes_titles=saved_theme[0])
    saved_theme.clear()
def test_to_itog():
    test.withdraw()
    itogWindow(themes_titles=saved_theme[0])
    saved_theme.clear()

def registerWindow(): # окно регистрации
    global ent_fcs, ent_group, register
    def regis():  # считывание данных при регистрации
        global FCs, group, usernaming, split_name
        FCs = []
        group = []
        try:
            full_name = ent_fcs.get()
            split_name = full_name.split()
            group_name = ent_group.get()
            last_name = split_name[0]
            first_name = split_name[1]
            patronymic = split_name[2] if len(split_name) > 2 else ""
            FCs.append(last_name)
            FCs.append(first_name)
            FCs.append(patronymic)
            group.append(ent_group.get())
            str_full_name = last_name + " " + first_name + " " + patronymic
            str_group_name = group_name
            usernaming = last_name + "_" + first_name + "_" + patronymic
            data = {str_full_name: str_group_name}
            print(data)
            with open("userdata.txt", "a") as file:
                file.write(json.dumps(data) + "\n")
        except:
            showerror(title="Ошибка", message="Неправильный формат данных")
    def enter():
        global g, data, tmp_username_and_pass, username, password
        username = ent_fcs.get()
        password = ent_group.get()
        FCs = []
        group = []
        full_name = ent_fcs.get()
        split_name = full_name.split()
        group_name = ent_group.get()
        last_name = split_name[0]
        first_name = split_name[1]
        patronymic = split_name[2] if len(split_name) > 2 else ""
        FCs.append(last_name)
        FCs.append(first_name)
        FCs.append(patronymic)
        group.append(ent_group.get())
        with open("userdata.txt", "r", encoding='ansi') as file:
            for line in file:
                data = json.loads(line)
                if username in data and data[username] == password:
                    showinfo(title="Сообщение", message="Успешная авторизация")
                    # tmp_username_and_pass = "_" + last_name + "_" + first_name + "_" + patronymic + "_" + password
                    tmp_username_and_pass = last_name + "" + first_name + "" + patronymic + "" + password
                    if "d d d" in data and data[username] == "d":
                        g = 1
                    else:
                        g = 2
                    textbookWindow(g)
                    return
            showerror(title="Ошибка", message="Такого пользователя нет или неправильный формат данных ")
    tp_reg = Tk()
    register = Toplevel()
    register.title("Регистрация")
    register.geometry("400x280+700+350")
    register.config(background="floralwhite")
    register.resizable(False, False)
    lbl_registration = Label(register, font="Arial 15" ,text="Регистрация", borderwidth=5, relief="ridge",background="snow").place(x=150, y=14)
    img_registration = PhotoImage(file="Registration/4230537-business-group-team_115034.png")
    img_registration_lbl = Label(register,image=img_registration,background="floralwhite").place(x=110,y=14)
    lbl_fcs = Label(register, text="ФИО:",font="Arial",background="floralwhite").place(x=57, y=71)
    ent_fcs = ttk.Entry(register, font="Arial", width=25)
    ent_fcs.place(x=110,y=71)
    lbl_group = Label(register, text="Группа:", font="Arial",background="floralwhite").place(x=43, y=120)
    ent_group = ttk.Entry(register, font="Arial", width=25)
    ent_group.place(x=110, y=121)
    btn_regis = Button(register, text="Зарегистрировать", font="Arial", width=16, borderwidth=2, relief="groove", command=regis, background="snow")
    btn_regis.place(x=35, y=170)
    btn_enter = Button(register,text="Войти", font="Arial", width=16, borderwidth=2, relief="groove", command=enter,background="snow")
    btn_enter.place(x=210, y=170)
    lbl_note = Label(register, text="Пожалуйста, вводите данные в правильном формате. Например:\n ФИО: Иванов Иван Иванович, Группа: ИСП-20.",background="floralwhite").place(x=17, y=220)
    tp_reg.withdraw()
    register.mainloop()
def textbookWindow(g): # окно со списком тем
    global textbook, themes_titles, titles
    textbook = Tk()
    textbook.state('zoomed')
    textbook.config(background="floralwhite")
    lbl_textbook = Label(textbook,text=f'Учебник "Компьютер и его ПО"', font="Trebuchet 50", borderwidth=9, relief="groove", background="snow").place(x=10,y=10)
    i = 65
    titles = ["История развития вычислительной техники", "Программное обеспечение компьютера", "Прикладное программное обеспечение"] # здесь потом будут все темы для прохождения
    for themes_titles in titles: # распаковка кнопок из списка titles
        i += 45
        btn_themes_titles = Button(textbook,text=f'Тема "{themes_titles}"', font="Trebuchet 15", borderwidth=3, relief="groove", background="snow",command= partial(themesWindow,themes_titles))
        btn_themes_titles.place(x=10, y=i)
    btn_textbook_final_test = Button(textbook, text="Перейти к конечному тестированию", font="Trebuchet 15", borderwidth=3, relief="groove", background="snow", command= final_testWindow).place(x=10,y=245)
    btn_textbook_to_register = Button(textbook, text="Перейти обратно к регистрации", font="Trebuchet 15", borderwidth=3, relief="groove", background="snow", command=lambda:(textbook.destroy(),registerWindow())).place(x=10,y=290)
    if g == 1:
        def usersWindow():
            global users, data
            def sort_file_text():
                datas = []
                svodka_files = [f for f in listdir("svodka") if isfile(join("svodka", f))]
                for filename in svodka_files:
                    file_path = os.path.abspath(f"svodka/{filename}")
                    with open(f"{file_path}", 'r', encoding="utf-8") as file:
                        data = file.read().split('\n')[0:7]
                        datas.append(data)
                    with open(f"{file_path}", 'r', encoding="utf-8") as file:
                        data = file.read().split('\n')[7:14]
                        datas.append(data)
                    with open(f"{file_path}", 'r', encoding="utf-8") as file:
                        data = file.read().split('\n')[14:21]
                        datas.append(data)
                        datas.sort()
                    with open(file_path, 'w', encoding="utf-8") as file:
                        for line in datas:
                            for line1 in line:
                                if line1.strip() and not line1.isspace():
                                    file.write("%s\n" % line1)
            sort_file_text()
            def users_statistics_file(filename):
                file_path = os.path.abspath(f"svodka/{filename}")
                os.system(f"{file_path}")
                return
            def users_statistics_table(filename):
                def user_statistics_table_save():
                    filepath = filedialog.asksaveasfilename(filetypes=[("Text File","*.txt")], title="Выберите папку и напишите название файла для сохранения")
                    if filepath != "":
                        text = txt_users_table.get("1.0", END)
                        with open(f"{filepath}.txt", "w") as file:
                            file.write(text)
                file_path = os.path.abspath(f"svodka/{filename}")
                with open(f'{file_path}', 'r', encoding="UTF-8") as file:
                    data = [line.strip() for line in file]
                    print(data)
                    columns = ["Название", "Номер + Ответ"]
                    table_users = PrettyTable()
                    table_users.clear()
                    if len(data) <= 7:
                        i = 0
                        table_users.add_column(columns[0],[data[i]])
                        table_users.add_column(columns[1],[data[i+1]])
                        for i in range(5):
                            table_users.add_row(["",data[i+2]])
                    elif len(data) >=7 and len(data) <= 14:
                        i = 0
                        table_users.add_column(columns[0], [data[i]])
                        table_users.add_column(columns[1], [data[i + 1]])
                        for i in range(5):
                            table_users.add_row(["", data[i + 2]])
                        i = 7
                        table_users.add_row([data[i], data[i+1]])
                        for i in range(5):
                            table_users.add_row(["", data[i + 2]])
                    elif len(data) >= 14:
                        i = 0
                        a = 0
                        b = 0
                        table_users.add_column(columns[0], [data[i]])
                        table_users.add_column(columns[1], [data[i + 1]])
                        for i in range(5):
                            table_users.add_row(["", data[i + 2]])
                        for j in range(2):
                            a += 7
                            b += 7
                            table_users.add_row([data[a], data[a + 1]])
                            for b in range(5):
                                table_users.add_row(["", data[b + 2]])

                txt_users_table = Text(users, background="snow",width=40,height=22)
                txt_users_table.place(x=1050,y=10)
                txt_users_table.insert(END, str(table_users))
                txt_users_table["state"] = DISABLED
                btn_users_table_save = Button(users, text="Сохранить таблицу",font="Trebuchet 11", borderwidth=3, relief="groove", background="snow", command=user_statistics_table_save)
                btn_users_table_save.place(x=1050, y=375)
            def groups_statistics_file(filename):
                file_path = os.path.abspath(f"groups/{filename}")
                os.system(f"{file_path}")
                return
            users = Toplevel()
            users.state('zoomed')
            users.title("Пользователи")
            users.config(background="floralwhite")
            with open("userdata.txt", "r",  encoding='ansi') as file:
                i = 45
                j = 45
                h = 45
                keys_var = []
                values_var = []
                svodka_files = [f for f in listdir("svodka") if isfile(join("svodka", f))]
                groups_files = [f for f in listdir("groups") if isfile(join("groups", f))]
                for user in file:
                    data = json.loads(user)
                lbl_users_note1 = Label(users, text="Сводки с баллами для пользователя:",font="Trebuchet 11", borderwidth=3, relief="groove", background="snow").place(x=10,y=10)
                for filename in svodka_files:
                    if ".txt" in filename:
                        filename_changed = filename.replace(".txt","")
                    btn_users_view = Button(users, text=f"Пользователь {filename_changed}", font="Trebuchet 11", borderwidth=3, relief="groove", background="snow", command=lambda name=filename: users_statistics_file(name))
                    btn_users_view.place(x=10,y=i)
                    i += 35
                lbl_users_note2 = Label(users, text="Сведения в таблице:",font="Trebuchet 11", borderwidth=3, relief="groove", background="snow").place(x=430,y=10)
                for filename in svodka_files:
                    if ".txt" in filename:
                        filename_changed = filename.replace(".txt","")
                    btn_users_view = Button(users, text=f"Пользователь {filename_changed}", font="Trebuchet 11", borderwidth=3, relief="groove", background="snow", command=lambda name=filename: users_statistics_table(name))
                    btn_users_view.place(x=430, y=j)
                    j += 35
                lbl_users_note3 = Label(users, text="Группы:",font="Trebuchet 11", borderwidth=3, relief="groove", background="snow").place(x=850,y=10)
                for filename in groups_files:
                    if ".txt" in filename:
                        filename_changed = filename.replace(".txt","")
                    btn_users_view = Button(users, text=f"Группа {filename_changed}", font="Trebuchet 11", borderwidth=3, relief="groove", background="snow", command=lambda name=filename: groups_statistics_file(name))
                    btn_users_view.place(x=850, y=h)
                    h += 35
                textbook.destroy()
                btn_home = Button(users, text="Назад на главную", font="Trebuchet 15", borderwidth=3, relief="groove", background="snow", command=users_to_textbook).place(x=873, y=957)
            users.protocol("WM_DELETE_WINDOW", on_closing_for_usersWindow)
        textbook.title("Режим просмотра: Преподаватель")
        btn_itog_prepod_svodka = Button(textbook, text="Посмотреть всех пользователей", font="Trebuchet 15", borderwidth=3, relief="groove", background="snow", command=usersWindow)
        btn_itog_prepod_svodka.place(x=1595, y=10)
    elif g == 2:
        textbook.title("Режим просмотра: Студент")
    register.destroy()
    textbook.protocol("WM_DELETE_WINDOW", on_closing_for_textbookWindow)
    textbook.mainloop()

def final_testWindow():
    global final_test, var7, var8, var9, var10, var11, var12
    def final_itog_to_final_test():
        final_itog.destroy()
        final_testWindow()
    def final_test_to_itog():
        global final_itog
        final_itog = Tk()
        final_itog.state('zoomed')
        final_itog.title(f'Итоги итогового теста"')
        final_itog.config(background="floralwhite")
        c1 = 0
        n1 = 0
        prav_lst = []
        if var7.get() == "8":
            c1 += 1
            prav = "1"
            prav_lst.append(prav)
        else:
            n1 += 1
            prav = "0"
            prav_lst.append(prav)
        if var8.get() == "ENIAC":
            c1 += 1
            prav = "1"
            prav_lst.append(prav)
        else:
            n1 += 1
            prav = "0"
            prav_lst.append(prav)
        if var9.get() == "50-е":
            c1 += 1
            prav = "1"
            prav_lst.append(prav)
        else:
            n1 += 1
            prav = "0"
            prav_lst.append(prav)
        if var10.get() == "Access":
            c1 += 1
            prav = "1"
            prav_lst.append(prav)
        else:
            n1 += 1
            prav = "0"
            prav_lst.append(prav)
        if var11.get() == "Windows, Mac OS, Linux":
            c1 += 1
            prav = "1"
            prav_lst.append(prav)
        else:
            n1 += 1
            prav = "0"
            prav_lst.append(prav)
        if var12.get() == "Многозадачность":
            c1 += 1
            prav = "1"
            prav_lst.append(prav)
        else:
            n1 += 1
            prav = "0"
            prav_lst.append(prav)
        if ent_test_qw7_1.get().capitalize() == "Android":
            c1 += 1
            prav = "1"
            prav_lst.append(prav)
        else:
            n1 += 1
            prav = "0"
            prav_lst.append(prav)
        lbl_itog_test_pod = Label(final_itog,  text=f"Вы ответили правильно на \n{c1} вопрос(-ов) и \nна {n1} вопросов неправильно",  borderwidth=3, relief="groove", background="snow", font="Arial 12").place(x=10, y=298)
        pravil = [f"1) 8 ({prav_lst[0]})", f"2) ENIAC ({prav_lst[1]})", f"3) 50-e ({prav_lst[2]})", f"4) Access ({prav_lst[3]})", f"5) Windows, Mac, Linux ({prav_lst[4]})", f"6) Многозадачность ({prav_lst[5]})", f"7) Android ({prav_lst[6]})"]
        lbl_itog_test_pravil = Label(final_itog, text="Правильные ответы на тест: (1 или 0)", background="snow",
                                         font="Arial 12").place(x=10, y=365)
        i = 390
        for string in pravil:
            lbl_itog_test_var = Label(final_itog, text=string, background="snow", font="Arial 11").place(x=10, y=i)
            i += 25
        lbl_itog_title = Label(final_itog, text=f'Итоги', font="Trebuchet 50", borderwidth=9, relief="groove",
                                   background="snow").place(x=10, y=10)
        lbl_itog_test = Label(final_itog, text="Итоги теста: ", borderwidth=3, relief="groove", background="snow",
                                  font="Arial 18").place(x=10, y=255)
        btn_home = Button(final_itog, text="Назад на главную", font="Trebuchet 15", borderwidth=3,
                              relief="groove", background="snow", command=on_closing_for_final_itogWindow).place(x=873, y=957)
        btn_test_to_practical = Button(final_itog, text="Перейти обратно к тестовой части", font="Trebuchet 15",
                                           borderwidth=3, relief="groove", background="snow",
                                           command=final_itog_to_final_test).place(x=10, y=957)
        final_test.destroy()
        final_itog.protocol("WM_DELETE_WINDOW", on_closing_for_final_itogWindow)
        final_itog.mainloop()
    def countdown(s):
        global bro
        if s == 0:
            dosrochno()
            return
        lbl_test_timer.config(text=f'Время таймера: {str(s)}')
        s -= 1
        bro = lbl_test_timer.after(1000, lambda: countdown(s))
    def dosrochno():
        btn_final_test_to_itog = Button(final_test, text="Перейти к итогам", font="Trebuchet 15", borderwidth=3, relief="groove", background="snow", command=final_test_to_itog).place(x=1736, y=957)
        lbl_test_timer.after_cancel(bro)
        btn_test_dosrochno.destroy()
        rbtn_test_qw1_1["state"] = DISABLED
        rbtn_test_qw1_2["state"] = DISABLED
        rbtn_test_qw1_3["state"] = DISABLED
        rbtn_test_qw1_4["state"] = DISABLED
        rbtn_test_qw2_1["state"] = DISABLED
        rbtn_test_qw2_2["state"] = DISABLED
        rbtn_test_qw2_3["state"] = DISABLED
        rbtn_test_qw2_4["state"] = DISABLED
        rbtn_test_qw3_1["state"] = DISABLED
        rbtn_test_qw3_2["state"] = DISABLED
        rbtn_test_qw3_3["state"] = DISABLED
        rbtn_test_qw3_4["state"] = DISABLED
        rbtn_test_qw4_1["state"] = DISABLED
        rbtn_test_qw4_2["state"] = DISABLED
        rbtn_test_qw4_3["state"] = DISABLED
        rbtn_test_qw4_4["state"] = DISABLED
        rbtn_test_qw5_1["state"] = DISABLED
        rbtn_test_qw5_2["state"] = DISABLED
        rbtn_test_qw5_3["state"] = DISABLED
        rbtn_test_qw5_4["state"] = DISABLED
        rbtn_test_qw6_1["state"] = DISABLED
        rbtn_test_qw6_2["state"] = DISABLED
        rbtn_test_qw6_3["state"] = DISABLED
        rbtn_test_qw6_4["state"] = DISABLED
        ent_test_qw7_1["state"] = DISABLED
    final_test = Toplevel()
    final_test.state('zoomed')
    final_test.title("Итотоговый тест по модулю")
    final_test.config(background="floralwhite")
    lbl_textbook = Label(final_test, text=f'Итоговый тест по модулю', font="Trebuchet 50", borderwidth=9, relief="groove", background="snow").place(x=10, y=10)
    btn_home = Button(final_test, text="Назад на главную", font="Trebuchet 15", borderwidth=3, relief="groove", background="snow", command=final_test_to_textbook).place(x=873, y=957)
    btn_test_dosrochno = Button(final_test, text="Завершить досрочно", font="Trebuchet 15", borderwidth=3, relief="groove", background="snow", command=dosrochno)
    btn_test_dosrochno.place(x=1700, y=957)
    frm_test = ttk.Frame(final_test, borderwidth=3, relief="groove", width=1898, height=829)
    frm_test.place(x=12, y=117)
    lbl_test_timer_info = Label(frm_test, text='Переход к итогам появится после завершения таймера \nили после нажатия на кнопку "Завершить досрочно"', font="Arial 11").place(x=1300, y=30)
    lbl_test_timer = Label(frm_test, text='Время таймера: ', font="Arial 12")
    lbl_test_timer.place(x=1300, y=5)
    countdown(20)
    # 1
    qw1_1 = "8"
    qw1_2 = "7"
    qw1_3 = "3"
    qw1_4 = "5"
    var7 = StringVar(value=" ")
    rbtn_test_qw1_1 = Radiobutton(frm_test, font="Arial 12", text=qw1_1, value=qw1_1, variable=var7)
    rbtn_test_qw1_1.place(x=5, y=40)
    rbtn_test_qw1_2 = Radiobutton(frm_test, font="Arial 12", text=qw1_2, value=qw1_2, variable=var7)
    rbtn_test_qw1_2.place(x=45, y=40)
    rbtn_test_qw1_3 = Radiobutton(frm_test, font="Arial 12", text=qw1_3, value=qw1_3, variable=var7)
    rbtn_test_qw1_3.place(x=5, y=60)
    rbtn_test_qw1_4 = Radiobutton(frm_test, font="Arial 12", text=qw1_4, value=qw1_4, variable=var7)
    rbtn_test_qw1_4.place(x=45, y=60)
    # 2
    qw2_1 = "ENIAC"
    qw2_2 = "Macintosh"
    qw2_3 = "IBM"
    qw2_4 = "Урал-1"
    var8 = StringVar(value=" ")
    rbtn_test_qw2_1 = Radiobutton(frm_test, font="Arial 12", text=qw2_1, value=qw2_1, variable=var8)
    rbtn_test_qw2_1.place(x=5, y=160)
    rbtn_test_qw2_2 = Radiobutton(frm_test, font="Arial 12", text=qw2_2, value=qw2_2, variable=var8)
    rbtn_test_qw2_2.place(x=82, y=160)
    rbtn_test_qw2_3 = Radiobutton(frm_test, font="Arial 12", text=qw2_3, value=qw2_3, variable=var8)
    rbtn_test_qw2_3.place(x=5, y=180)
    rbtn_test_qw2_4 = Radiobutton(frm_test, font="Arial 12", text=qw2_4, value=qw2_4, variable=var8)
    rbtn_test_qw2_4.place(x=82, y=180)
    # 3
    qw3_1 = "50-е"
    qw3_2 = "30-е"
    qw3_3 = "40-е"
    qw3_4 = "20-е"
    var9 = StringVar(value=" ")
    rbtn_test_qw3_1 = Radiobutton(frm_test, font="Arial 12", text=qw3_1, value=qw3_1, variable=var9)
    rbtn_test_qw3_1.place(x=5, y=280)
    rbtn_test_qw3_2 = Radiobutton(frm_test, font="Arial 12", text=qw3_2, value=qw3_2, variable=var9)
    rbtn_test_qw3_2.place(x=67, y=280)
    rbtn_test_qw3_3 = Radiobutton(frm_test, font="Arial 12", text=qw3_3, value=qw3_3, variable=var9)
    rbtn_test_qw3_3.place(x=5, y=300)
    rbtn_test_qw3_4 = Radiobutton(frm_test, font="Arial 12", text=qw3_4, value=qw3_4, variable=var9)
    rbtn_test_qw3_4.place(x=67, y=300)
    # 4
    qw4_1 = "Excel"
    qw4_2 = "Word"
    qw4_3 = "Access"
    qw4_4 = "Notepad"
    var10 = StringVar(value=" ")
    rbtn_test_qw4_1 = Radiobutton(frm_test, font="Arial 12", text=qw4_1, value=qw4_1, variable=var10)
    rbtn_test_qw4_1.place(x=5, y=400)
    rbtn_test_qw4_2 = Radiobutton(frm_test, font="Arial 12", text=qw4_2, value=qw4_2, variable=var10)
    rbtn_test_qw4_2.place(x=85, y=400)
    rbtn_test_qw4_3 = Radiobutton(frm_test, font="Arial 12", text=qw4_3, value=qw4_3, variable=var10)
    rbtn_test_qw4_3.place(x=5, y=425)
    rbtn_test_qw4_4 = Radiobutton(frm_test, font="Arial 12", text=qw4_4, value=qw4_4, variable=var10)
    rbtn_test_qw4_4.place(x=85, y=425)
    # 5
    qw5_1 = "iOS, Mac OS, Android"
    qw5_2 = "Windows, Mac OS, Linux"
    qw5_3 = "Windows Phone, Linux, Mac OS"
    qw5_4 = "Windows, iOS, Linux"
    var11 = StringVar(value=" ")
    rbtn_test_qw5_1 = Radiobutton(frm_test, font="Arial 12", text=qw5_1, value=qw5_1, variable=var11)
    rbtn_test_qw5_1.place(x=5, y=520)
    rbtn_test_qw5_2 = Radiobutton(frm_test, font="Arial 12", text=qw5_2, value=qw5_2, variable=var11)
    rbtn_test_qw5_2.place(x=5, y=545)
    rbtn_test_qw5_3 = Radiobutton(frm_test, font="Arial 12", text=qw5_3, value=qw5_3, variable=var11)
    rbtn_test_qw5_3.place(x=210, y=520)
    rbtn_test_qw5_4 = Radiobutton(frm_test, font="Arial 12", text=qw5_4, value=qw5_4, variable=var11)
    rbtn_test_qw5_4.place(x=5, y=570)
    # 6
    qw6_1 = "Мегазадачность"
    qw6_2 = "Многопоточность"
    qw6_3 = "Мультипоточность"
    qw6_4 = "Многозадачность"
    var12 = StringVar(value=" ")
    rbtn_test_qw6_1 = Radiobutton(frm_test, font="Arial 12", text=qw6_1, value=qw6_1, variable=var12)
    rbtn_test_qw6_1.place(x=5, y=640)
    rbtn_test_qw6_2 = Radiobutton(frm_test, font="Arial 12", text=qw6_2, value=qw6_2, variable=var12)
    rbtn_test_qw6_2.place(x=5, y=690)
    rbtn_test_qw6_3 = Radiobutton(frm_test, font="Arial 12", text=qw6_3, value=qw6_3, variable=var12)
    rbtn_test_qw6_3.place(x=5, y=665)
    rbtn_test_qw6_4 = Radiobutton(frm_test, font="Arial 12", text=qw6_4, value=qw6_4, variable=var12)
    rbtn_test_qw6_4.place(x=170, y=640)
    # 7
    lbl_test_qw7_1 = Label(frm_test, text="Ответ: ", font="Arial 12").place(x=5, y=760)
    ent_test_qw7_1 = Entry(frm_test, font="Arial 12")
    ent_test_qw7_1.place(x=60, y=760)
    i = 5
    for string in lines7:
        lbl_test_qw = Label(frm_test, text=string, borderwidth=3, relief="groove", font="Arial 15").place(x=5, y=i)
        i += 120
    textbook.withdraw()
def themesWindow(themes_titles): # окно с темой
    global themes, saved_theme
    themes = Tk()
    themes.state('zoomed')
    themes.title(f'Тема: "{themes_titles}"')
    themes.config(background="floralwhite")
    saved_theme = []
    saved_theme.append(str(themes_titles))
    lbl_themes_main_title = Label(themes, text=f'Тема: "{themes_titles}"', font="Trebuchet 50", borderwidth=9, relief="groove", background="snow").place(x=10, y=10)
    btn_lecture = Button(themes,text="1) Лекция",font="Trebuchet 15",borderwidth=3, relief="groove", background="snow", command=partial(lectureWindow,themes_titles)).place(x=10,y=110)
    btn_practical = Button(themes, text="2) Практическое задание", font="Trebuchet 15", borderwidth=3, relief="groove", background="snow", command=partial(practicalWindow,themes_titles)).place(x=10, y=155)
    btn_test = Button(themes, text="3) Тест по теме", font="Trebuchet 15", borderwidth=3, relief="groove", background="snow", command=partial(testWindow,themes_titles)).place(x=10, y=200)
    btn_nazad = Button(themes, text="Перейти обратно к списку тем", font="Trebuchet 15", borderwidth=3, relief="groove", background="snow", command= on_closing_for_themesWindow).place(x=10,y=245)
    themes.protocol("WM_DELETE_WINDOW", on_closing_for_themesWindow)
    textbook.destroy()
    themes.mainloop()
def lectureWindow(themes_titles): # окно с лекцией
    global lecture, txt_lecture_view
    lecture = Toplevel()
    lecture.state('zoomed')
    lecture.title(f'Лекция к теме "{themes_titles}"')
    lecture.config(background="floralwhite")
    lbl_lecture_title = Label(lecture, text=f'"{themes_titles}"', font="Trebuchet 50", borderwidth=9, relief="groove", background="snow").place(x=10,y=10)
    txt_lecture_view = Text(lecture, font="Trebuchet 14",borderwidth=3, relief="groove", background="snow", width=172, height=37) # 172 37
    txt_lecture_view.place(x=12,y=117)
    txt_lecture_view.yview_scroll(number=1, what="units")
    if themes_titles == titles[0]:
        i = 1.0
        for string in lines1:
            txt_lecture_view.insert(i, string)
            txt_lecture_view.insert(END, "\n")
            i += 1
            # print(string, i)
            if i == 18:
                evm1_image = PhotoImage(file="Lecture №1/first_evm.png")
                txt_lecture_view.image_create(18.0, image=evm1_image)
            if i == 22:
                evm2_image = PhotoImage(file="Lecture №1/second_evm.png")
                txt_lecture_view.image_create(22.0, image=evm2_image)
            if i == 27:
                evm3_image = PhotoImage(file="Lecture №1/third_evm.png")
                txt_lecture_view.image_create(27.0, image=evm3_image)
        file1.close()
    elif themes_titles == titles[1]:
        i = 1.0
        for string in lines3:
            txt_lecture_view.insert(i, string)
            txt_lecture_view.insert(END, "\n")
            i += 1
            print(string, i)
            if i == 6:
                pic1_image = PhotoImage(file="Lecture №2/first_picture.png")
                txt_lecture_view.image_create(6.0, image=pic1_image)
            if i == 22:
                pic2_image = PhotoImage(file="Lecture №2/second_picture.png")
                txt_lecture_view.image_create(22.0, image=pic2_image)
            if i == 29:
                pic3_image = PhotoImage(file="Lecture №2/third_picture.png")
                txt_lecture_view.image_create(29.0, image=pic3_image)
            if i == 33:
                pic4_image = PhotoImage(file="Lecture №2/fourth_picture.png")
                txt_lecture_view.image_create(33.0, image=pic4_image)
        file3.close()
    elif themes_titles == titles[2]:
        i = 1.0
        for string in lines5:
            txt_lecture_view.insert(i, string)
            txt_lecture_view.insert(END, "\n")
            i += 1
            print(string, i)
            if i == 17:
                pic1_image = PhotoImage(file="Lecture №3/first_pic.png")
                txt_lecture_view.image_create(17.0, image=pic1_image)
        file5.close()
    txt_lecture_view["state"] = DISABLED
    btn_lecture_to_themes = Button(lecture, text="Перейти обратно к странице темы", font="Trebuchet 15", borderwidth=3, relief="groove", background="snow", command=lecture_to_themes).place(x=10,y=957)
    btn_home = Button(lecture, text="Перейти на главную страницу темы", font="Trebuchet 15", borderwidth=3,relief="groove", background="snow", command=on_closing_for_lectureWindow).place(x=793,y=957)
    btn_lecture_to_practical = Button(lecture, text="Перейти к практической части", font="Trebuchet 15", borderwidth=3, relief="groove", background="snow", command=lecture_to_practical).place(x=1620,y=957)
    lecture.protocol("WM_DELETE_WINDOW", on_closing_for_lectureWindow)
    themes.withdraw()
    lecture.mainloop()
def practicalWindow(themes_titles): # окно с практическим заданием
    global practical, canvas, img1, img2, lbl_practical_minigame_check_solution, area1, area2
    # мини игра -----------
    practical = Toplevel()
    practical.state('zoomed')
    practical.title(f'Практическое задание к теме "{themes_titles}"')
    practical.config(background="floralwhite")
    canvas_practical = Canvas(practical, width=1891, height=820, borderwidth=3, relief="groove", background="snow")
    canvas_practical.place(x=10, y=115)
    if themes_titles == titles[0]:
        def check_solution():
            coords1 = canvas_practical.coords(img1)
            coords2 = canvas_practical.coords(img2)
            coords3 = canvas_practical.coords(img3)
            if (coords1[0] == 575 and coords1[1] == 200) and (coords2[0] == 955 and coords2[1] == 200) and (coords3[0] == 1335 and coords3[1] == 200):
                lbl_practical_minigame_check_solution.config(text="Правильно!")
            else:
                lbl_practical_minigame_check_solution.config(text="Неправильно. Попробуй еще раз!")
            print(canvas_practical.coords(img1), canvas_practical.coords(img2), canvas_practical.coords(img3))
        # Функции для перемещения картинок
        def move_img1(event):
            canvas_practical.coords(img1, event.x, event.y)
        def release_img1(event):
            if canvas_practical.coords(img1) >= [515, 0] and canvas_practical.coords(img1) <= [896, 0]:
                canvas_practical.coords(img1, 575, 200)
            elif canvas_practical.coords(img1) >= [897, 0] and canvas_practical.coords(img1) <= [1277, 0]:
                canvas_practical.coords(img1, 955, 200)
            elif canvas_practical.coords(img1) >= [1278,0] and canvas_practical.coords(img1) <= [1654, 0]:
                canvas_practical.coords(img1, 1335, 200)
        def move_img2(event):
            canvas_practical.coords(img2, event.x, event.y)
        def release_img2(event):
            if canvas_practical.coords(img2) >= [515, 0] and canvas_practical.coords(img2) <= [896, 0]:
                canvas_practical.coords(img2, 575, 200)
            elif canvas_practical.coords(img2) >= [897, 0] and canvas_practical.coords(img2) <= [1277, 0]:
                canvas_practical.coords(img2, 955, 200)
            elif canvas_practical.coords(img2) >= [1278,0] and canvas_practical.coords(img2) <= [1654, 0]:
                canvas_practical.coords(img2, 1335, 200)
        def move_img3(event):
            canvas_practical.coords(img3, event.x, event.y)
        def release_img3(event):
            if canvas_practical.coords(img3) >= [515, 0] and canvas_practical.coords(img3) <= [896, 0]:
                canvas_practical.coords(img3, 575, 200)
            elif canvas_practical.coords(img3) >= [897, 0] and canvas_practical.coords(img3) <= [1277, 0]:
                canvas_practical.coords(img3, 955, 200)
            elif canvas_practical.coords(img3) >= [1278,0] and canvas_practical.coords(img3) <= [1654, 0]:
                canvas_practical.coords(img3, 1335, 200)
        # -- Мини игра --
        area1 = canvas_practical.create_rectangle(400, 50, 750, 380, fill="white")
        area2 = canvas_practical.create_rectangle(780, 50, 1130, 380, fill="white")
        area3 = canvas_practical.create_rectangle(1160, 50, 1510, 380, fill="white")
        evm1_image = PhotoImage(file="Lecture №1/first_evm.png")
        evm2_image = PhotoImage(file="Lecture №1/second_evm.png")
        evm3_image = PhotoImage(file="Lecture №1/third_evm.png")
        img1 = canvas_practical.create_image(950, 600, image=evm1_image)
        img2 = canvas_practical.create_image(575, 600, image=evm2_image)
        img3 = canvas_practical.create_image(1330, 600, image=evm3_image)
        canvas_practical.tag_bind(img1, "<B1-Motion>", move_img1)
        canvas_practical.tag_bind(img2, "<B1-Motion>", move_img2)
        canvas_practical.tag_bind(img3, "<B1-Motion>", move_img3)
        canvas_practical.tag_bind(img1, "<ButtonRelease-1>", release_img1)
        canvas_practical.tag_bind(img2, "<ButtonRelease-1>", release_img2)
        canvas_practical.tag_bind(img3, "<ButtonRelease-1>", release_img3)
        button = Button(practical, text="Проверить", font="Arial 15", borderwidth=3, relief="groove", background="snow",command=check_solution)
        button.place(x=1720,y=830)
        lbl_practical_minigame_check_solution = Label(practical, text="", font="Arial 12", background="snow")
        lbl_practical_minigame_check_solution.place(x=1650,y=880)
        lbl_practical_minigame_area1 = Label(practical, text="ЭВМ первого поколения.", background="snow", font="Arial 12").place(x=490,y=500)
        lbl_practical_minigame_area2 = Label(practical, text="ЭВМ второго поколения.", background="snow", font="Arial 12").place(x=870,y=500)
        lbl_practical_minigame_area3 = Label(practical, text="ЭВМ третьего поколения.", background="snow", font="Arial 12").place(x=1250,y=500)
    elif themes_titles == titles[1]:
        def check_solution():
            coords1 = canvas_practical.coords(img1)
            coords2 = canvas_practical.coords(img2)
            coords3 = canvas_practical.coords(img3)
            if (coords1[0] == 575 and coords1[1] == 200) and (coords2[0] == 955 and coords2[1] == 200) and (
                    coords3[0] == 1335 and coords3[1] == 200):
                lbl_practical_minigame_check_solution.config(text="Правильно!")
            else:
                lbl_practical_minigame_check_solution.config(text="Неправильно. Попробуй еще раз!")
            print(canvas_practical.coords(img1), canvas_practical.coords(img2), canvas_practical.coords(img3))
        # Функции для перемещения картинок
        def move_img1(event):
            canvas_practical.coords(img1, event.x, event.y)
        def release_img1(event):
            if canvas_practical.coords(img1) >= [515, 0] and canvas_practical.coords(img1) <= [896, 0]:
                canvas_practical.coords(img1, 575, 200)
            elif canvas_practical.coords(img1) >= [897, 0] and canvas_practical.coords(img1) <= [1277, 0]:
                canvas_practical.coords(img1, 955, 200)
            elif canvas_practical.coords(img1) >= [1278, 0] and canvas_practical.coords(img1) <= [1654, 0]:
                canvas_practical.coords(img1, 1335, 200)
        def move_img2(event):
            canvas_practical.coords(img2, event.x, event.y)
        def release_img2(event):
            if canvas_practical.coords(img2) >= [515, 0] and canvas_practical.coords(img2) <= [896, 0]:
                canvas_practical.coords(img2, 575, 200)
            elif canvas_practical.coords(img2) >= [897, 0] and canvas_practical.coords(img2) <= [1277, 0]:
                canvas_practical.coords(img2, 955, 200)
            elif canvas_practical.coords(img2) >= [1278, 0] and canvas_practical.coords(img2) <= [1654, 0]:
                canvas_practical.coords(img2, 1335, 200)
        def move_img3(event):
            canvas_practical.coords(img3, event.x, event.y)
        def release_img3(event):
            if canvas_practical.coords(img3) >= [515, 0] and canvas_practical.coords(img3) <= [896, 0]:
                canvas_practical.coords(img3, 575, 200)
            elif canvas_practical.coords(img3) >= [897, 0] and canvas_practical.coords(img3) <= [1277, 0]:
                canvas_practical.coords(img3, 955, 200)
            elif canvas_practical.coords(img3) >= [1278, 0] and canvas_practical.coords(img3) <= [1654, 0]:
                canvas_practical.coords(img3, 1335, 200)
        # -- Мини игра --
        area1 = canvas_practical.create_rectangle(400, 50, 750, 380, fill="white")
        area2 = canvas_practical.create_rectangle(780, 50, 1130, 380, fill="white")
        area3 = canvas_practical.create_rectangle(1160, 50, 1510, 380, fill="white")
        prakt1_image = PhotoImage(file="Lecture №2/prakt_1.png")
        prakt2_image = PhotoImage(file="Lecture №2/prakt_2.png")
        prakt3_image = PhotoImage(file="Lecture №2/prakt_3.png")
        img1 = canvas_practical.create_image(950, 600, image=prakt1_image)
        img2 = canvas_practical.create_image(575, 600, image=prakt2_image)
        img3 = canvas_practical.create_image(1340, 600, image=prakt3_image)
        canvas_practical.tag_bind(img1, "<B1-Motion>", move_img1)
        canvas_practical.tag_bind(img2, "<B1-Motion>", move_img2)
        canvas_practical.tag_bind(img3, "<B1-Motion>", move_img3)
        canvas_practical.tag_bind(img1, "<ButtonRelease-1>", release_img1)
        canvas_practical.tag_bind(img2, "<ButtonRelease-1>", release_img2)
        canvas_practical.tag_bind(img3, "<ButtonRelease-1>", release_img3)
        button = Button(practical, text="Проверить", font="Arial 15", borderwidth=3, relief="groove", background="snow",command=check_solution)
        button.place(x=1720, y=830)
        lbl_practical_minigame_check_solution = Label(practical, text="", font="Arial 12", background="snow")
        lbl_practical_minigame_check_solution.place(x=1650, y=880)
        lbl_practical_minigame_area1 = Label(practical, text="Системное ПО.", background="snow", font="Arial 12").place(x=525, y=500)
        lbl_practical_minigame_area2 = Label(practical, text="Системы программирования", background="snow", font="Arial 12").place(x=855, y=500)
        lbl_practical_minigame_area3 = Label(practical, text="Прикладное ПО.", background="snow", font="Arial 12").place(x=1290, y=500)
    elif themes_titles == titles[2]:
        def check_solution():
            vib1_check_sol = ['Графические редакторы', 'Игры', 'СУБД', 'Текстовые процессоры', 'Текстовые редакторы', 'Электронные таблицы']
            vib2_check_sol = ['Геоинформационные системы', 'Интегрированные пакеты', 'СУБД информационных систем']
            vib1.sort()
            vib2.sort()
            if vib1 == vib1_check_sol and vib2 == vib2_check_sol:
                lbl_practical_minigame_check_solution.config(text="Правильно!")
            else:
                lbl_practical_minigame_check_solution.config(text="Неправильно. Попробуй еще раз!")
            print(vib1,vib2)
        def append1_ppo():
            lstbox_practical_cop_select = lstbox_practical_cop.get(lstbox_practical_cop.curselection())
            vib1.append(lstbox_practical_cop_select)
            lstbox_practical_vib1.insert(END, lstbox_practical_cop_select)
            lstbox_practical_cop.delete(lstbox_practical_cop.curselection()[0])
        def append2_ppo():
            lstbox_practical_cop_select = lstbox_practical_cop.get(lstbox_practical_cop.curselection())
            vib2.append(lstbox_practical_cop_select)
            lstbox_practical_vib2.insert(END, lstbox_practical_cop_select)
            lstbox_practical_cop.delete(lstbox_practical_cop.curselection()[0])
        ppo = ["Текстовые редакторы", "Текстовые процессоры", "Электронные таблицы",
               "СУБД", "Графические редакторы", "Игры", "СУБД информационных систем",
               "Интегрированные пакеты", "Геоинформационные системы"]
        vib1 = []
        vib2 = []
        ppo_var = Variable(value=ppo)
        vib1_var = Variable(value=vib1)
        vib2_var = Variable(value=vib2)
        lstbox_practical_cop = Listbox(canvas_practical, listvariable=ppo_var, font="Arial 12", width=26)
        lstbox_practical_cop.place(x=860, y=400)
        btn_practical_vib1 = Button(canvas_practical, text="Добавить в ППО общего назначения", font="Arial 12", background="snow", borderwidth=3, relief="groove", command=append1_ppo)
        btn_practical_vib1.place(x=665, y=650)
        btn_practical_vib1 = Button(canvas_practical, text="Добавить в ППО специального назначения", font="Arial 12", background="snow", borderwidth=3, relief="groove", command=append2_ppo)
        btn_practical_vib1.place(x=1000, y=650)
        lstbox_practical_vib1 = Listbox(canvas_practical, listvariable=vib1_var, font="Arial 12", width=26)
        lstbox_practical_vib2 = Listbox(canvas_practical, listvariable=vib2_var, font="Arial 12", width=26)
        lstbox_practical_vib1.place(x=695, y=170)
        lstbox_practical_vib2.place(x=1040, y=170)
        lbl_practical_vib1 = Label(canvas_practical, text="ППО общего назначения", background="snow", font="Arial 12").place(x=720,y=135)
        lbl_practical_vib1 = Label(canvas_practical, text="ППО специального назначения", background="snow", font="Arial 12").place(x=1045, y=135)
        button = Button(practical, text="Проверить", font="Arial 15", borderwidth=3, relief="groove", background="snow", command=check_solution)
        button.place(x=1720, y=830)
        lbl_practical_minigame_check_solution = Label(practical, text="", font="Arial 12", background="snow")
        lbl_practical_minigame_check_solution.place(x=1650, y=880)
    lbl_practical_title = Label(practical, text=f'Практическое задание', font="Trebuchet 50", borderwidth=9,relief="groove", background="snow").place(x=10, y=10)
    btn_practical_to_lecture = Button(practical, text="Перейти обратно к лекции", font="Trebuchet 15", borderwidth=3, relief="groove", background="snow", command=practical_to_lecture).place(x=10,y=957)
    btn_home = Button(practical, text="Перейти на главную страницу темы", font="Trebuchet 15", borderwidth=3, relief="groove", background="snow", command=on_closing_for_practicalWindow).place(x=793, y=957)
    btn_practical_to_test = Button(practical, text="Перейти к тестовой части", font="Trebuchet 15", borderwidth=3, relief="groove", background="snow", command=practical_to_test).place(x=1660, y=957)
    themes.withdraw()
    practical.protocol("WM_DELETE_WINDOW", on_closing_for_practicalWindow)
    practical.mainloop()
def testWindow(themes_titles):  # окно с тестом
    global test, var1, var2, var3, var4, var5, var6, ent_test_qw3_1, lbl_test_timer
    test = Toplevel()
    test.state('zoomed')
    test.title(f'Тест по теме "{themes_titles}"')
    test.config(background="floralwhite")
    def countdown(s):
        global bro
        if s == 0:
            dosrochno()
            return
        lbl_test_timer.config(text=f'Время таймера: {str(s)}')
        s -= 1
        bro = lbl_test_timer.after(1000, lambda: countdown(s))
    def dosrochno():
        btn_test_to_itog = Button(test, text="Перейти к итогам", font="Trebuchet 15", borderwidth=3, relief="groove", background="snow", command=test_to_itog).place(x=1736, y=957)
        lbl_test_timer.after_cancel(bro)
        btn_test_dosrochno.destroy()
        rbtn_test_qw1_1["state"] = DISABLED
        rbtn_test_qw1_2["state"] = DISABLED
        rbtn_test_qw1_3["state"] = DISABLED
        rbtn_test_qw1_4["state"] = DISABLED
        rbtn_test_qw2_1["state"] = DISABLED
        rbtn_test_qw2_2["state"] = DISABLED
        rbtn_test_qw2_3["state"] = DISABLED
        rbtn_test_qw2_4["state"] = DISABLED
        rbtn_test_qw4_1["state"] = DISABLED
        rbtn_test_qw4_2["state"] = DISABLED
        rbtn_test_qw4_3["state"] = DISABLED
        rbtn_test_qw4_4["state"] = DISABLED
        rbtn_test_qw5_1["state"] = DISABLED
        rbtn_test_qw5_2["state"] = DISABLED
        rbtn_test_qw5_3["state"] = DISABLED
        rbtn_test_qw5_4["state"] = DISABLED
        rbtn_test_qw6_1["state"] = DISABLED
        rbtn_test_qw6_2["state"] = DISABLED
        rbtn_test_qw6_3["state"] = DISABLED
        rbtn_test_qw6_4["state"] = DISABLED
        if themes_titles == titles[1]:
            ent_test_qw3_1["state"] = DISABLED
        else:
            rbtn_test_qw3_1["state"] = DISABLED
            rbtn_test_qw3_2["state"] = DISABLED
            rbtn_test_qw3_3["state"] = DISABLED
            rbtn_test_qw3_4["state"] = DISABLED
    lbl_test_title = Label(test, text=f'Тест', font="Trebuchet 50", borderwidth=9, relief="groove", background="snow").place(x=10, y=10)
    btn_test_to_practical = Button(test, text="Перейти обратно к практической части", font="Trebuchet 15", borderwidth=3,relief="groove", background="snow", command=test_to_practical).place(x=10,y=957)
    btn_home = Button(test, text="Перейти на главную страницу темы", font="Trebuchet 15", borderwidth=3,relief="groove", background="snow", command=on_closing_for_testWindow).place(x=793,y=957)
    btn_test_dosrochno = Button(test, text="Завершить досрочно", font="Trebuchet 15", borderwidth=3, relief="groove", background="snow", command=dosrochno)
    btn_test_dosrochno.place(x=1700, y=957)
    frm_test = ttk.Frame(test, borderwidth=3, relief="groove", width=1898, height=829)
    frm_test.place(x=12, y=117)
    lbl_test_timer_info = Label(frm_test, text='Переход к итогам появится после завершения таймера \nили после нажатия на кнопку "Завершить досрочно"', font="Arial 11").place(x=1300,y=30)
    lbl_test_timer = Label(frm_test, text='Время таймера: ', font="Arial 12")
    lbl_test_timer.place(x=1300, y=5)
    i = 5
    countdown(10)
    if themes_titles == titles[0]:
        for string in lines2:
            lbl_test_qw = Label(frm_test, text=string, borderwidth=3, relief="groove", font="Arial 15").place(x=5, y=i)
            i += 120
        file2.close()
        # 1
        qw1_1 = "8"
        qw1_2 = "7"
        qw1_3 = "3"
        qw1_4 = "5"
        var1 = StringVar(value=" ")
        rbtn_test_qw1_1 = Radiobutton(frm_test, font="Arial 12", text=qw1_1, value=qw1_1, variable=var1)
        rbtn_test_qw1_1.place(x=5,y=40)
        rbtn_test_qw1_2 = Radiobutton(frm_test, font="Arial 12", text=qw1_2, value=qw1_2, variable=var1)
        rbtn_test_qw1_2.place(x=45, y=40)
        rbtn_test_qw1_3 = Radiobutton(frm_test, font="Arial 12", text=qw1_3, value=qw1_3, variable=var1)
        rbtn_test_qw1_3.place(x=5, y=60)
        rbtn_test_qw1_4 = Radiobutton(frm_test, font="Arial 12", text=qw1_4, value=qw1_4, variable=var1)
        rbtn_test_qw1_4.place(x=45, y=60)
        # 2
        qw2_1 = "6"
        qw2_2 = "3"
        qw2_3 = "4"
        qw2_4 = "5"
        var2 = StringVar(value=" ")
        rbtn_test_qw2_1 = Radiobutton(frm_test, font="Arial 12", text=qw2_1, value=qw2_1, variable=var2)
        rbtn_test_qw2_1.place(x=5, y=160)
        rbtn_test_qw2_2 = Radiobutton(frm_test, font="Arial 12", text=qw2_2, value=qw2_2, variable=var2)
        rbtn_test_qw2_2.place(x=45, y=160)
        rbtn_test_qw2_3 = Radiobutton(frm_test, font="Arial 12", text=qw2_3, value=qw2_3, variable=var2)
        rbtn_test_qw2_3.place(x=5, y=180)
        rbtn_test_qw2_4 = Radiobutton(frm_test, font="Arial 12", text=qw2_4, value=qw2_4, variable=var2)
        rbtn_test_qw2_4.place(x=45, y=180)
        # 3
        qw3_1 = "50-е"
        qw3_2 = "30-е"
        qw3_3 = "40-е"
        qw3_4 = "20-е"
        var3 = StringVar(value=" ")
        rbtn_test_qw3_1 = Radiobutton(frm_test, font="Arial 12", text=qw3_1, value=qw3_1, variable=var3)
        rbtn_test_qw3_1.place(x=5, y=280)
        rbtn_test_qw3_2 = Radiobutton(frm_test, font="Arial 12", text=qw3_2, value=qw3_2, variable=var3)
        rbtn_test_qw3_2.place(x=67, y=280)
        rbtn_test_qw3_3 = Radiobutton(frm_test, font="Arial 12", text=qw3_3, value=qw3_3, variable=var3)
        rbtn_test_qw3_3.place(x=5, y=300)
        rbtn_test_qw3_4 = Radiobutton(frm_test, font="Arial 12", text=qw3_4, value=qw3_4, variable=var3)
        rbtn_test_qw3_4.place(x=67, y=300)
        # 4
        qw4_1 = "30-е"
        qw4_2 = "20-е"
        qw4_3 = "60-е"
        qw4_4 = "50-е"
        var4 = StringVar(value=" ")
        rbtn_test_qw4_1 = Radiobutton(frm_test, font="Arial 12", text=qw4_1, value=qw4_1, variable=var4)
        rbtn_test_qw4_1.place(x=5, y=400)
        rbtn_test_qw4_2 = Radiobutton(frm_test, font="Arial 12", text=qw4_2, value=qw4_2, variable=var4)
        rbtn_test_qw4_2.place(x=67, y=400)
        rbtn_test_qw4_3 = Radiobutton(frm_test, font="Arial 12", text=qw4_3, value=qw4_3, variable=var4)
        rbtn_test_qw4_3.place(x=5, y=420)
        rbtn_test_qw4_4 = Radiobutton(frm_test, font="Arial 12", text=qw4_4, value=qw4_4, variable=var4)
        rbtn_test_qw4_4.place(x=67, y=420)
        # 5
        qw5_1 = "ENIAC"
        qw5_2 = "Macintosh"
        qw5_3 = "IBM"
        qw5_4 = "Урал-1"
        var5 = StringVar(value=" ")
        rbtn_test_qw5_1 = Radiobutton(frm_test, font="Arial 12", text=qw5_1, value=qw5_1, variable=var5)
        rbtn_test_qw5_1.place(x=5, y=520)
        rbtn_test_qw5_2 = Radiobutton(frm_test, font="Arial 12", text=qw5_2, value=qw5_2, variable=var5)
        rbtn_test_qw5_2.place(x=82, y=520)
        rbtn_test_qw5_3 = Radiobutton(frm_test, font="Arial 12", text=qw5_3, value=qw5_3, variable=var5)
        rbtn_test_qw5_3.place(x=5, y=540)
        rbtn_test_qw5_4 = Radiobutton(frm_test, font="Arial 12", text=qw5_4, value=qw5_4, variable=var5)
        rbtn_test_qw5_4.place(x=82, y=540)
        # 6
        qw6_1 = "IBM PC"
        qw6_2 = "микроЭВМ"
        qw6_3 = "EC ЭВМ"
        qw6_4 = "ничего из перечисленного"
        var6 = StringVar(value=" ")
        rbtn_test_qw6_1 = Radiobutton(frm_test, font="Arial 12", text=qw6_1, value=qw6_1, variable=var6)
        rbtn_test_qw6_1.place(x=5, y=640)
        rbtn_test_qw6_2 = Radiobutton(frm_test, font="Arial 12", text=qw6_2, value=qw6_2, variable=var6)
        rbtn_test_qw6_2.place(x=98, y=640)
        rbtn_test_qw6_3 = Radiobutton(frm_test, font="Arial 12", text=qw6_3, value=qw6_3, variable=var6)
        rbtn_test_qw6_3.place(x=5, y=660)
        rbtn_test_qw6_4 = Radiobutton(frm_test, font="Arial 12", text=qw6_4, value=qw6_4, variable=var6)
        rbtn_test_qw6_4.place(x=98, y=660)
    elif themes_titles == titles[1]:
        for string in lines4:
            lbl_test_qw = Label(frm_test, text=string, borderwidth=3, relief="groove", font="Arial 15").place(x=5, y=i)
            i += 120
        file4.close()
        # 1
        qw1_1 = "6"
        qw1_2 = "4"
        qw1_3 = "3"
        qw1_4 = "5"
        var1 = StringVar(value=" ")
        rbtn_test_qw1_1 = Radiobutton(frm_test, font="Arial 12", text=qw1_1, value=qw1_1, variable=var1)
        rbtn_test_qw1_1.place(x=5,y=40)
        rbtn_test_qw1_2 = Radiobutton(frm_test, font="Arial 12", text=qw1_2, value=qw1_2, variable=var1)
        rbtn_test_qw1_2.place(x=45, y=40)
        rbtn_test_qw1_3 = Radiobutton(frm_test, font="Arial 12", text=qw1_3, value=qw1_3, variable=var1)
        rbtn_test_qw1_3.place(x=5, y=60)
        rbtn_test_qw1_4 = Radiobutton(frm_test, font="Arial 12", text=qw1_4, value=qw1_4, variable=var1)
        rbtn_test_qw1_4.place(x=45, y=60)
        # 2
        qw2_1 = "iOS, Mac OS, Android"
        qw2_2 = "Windows, Mac OS, Linux"
        qw2_3 = "Windows Phone, Linux, Mac OS"
        qw2_4 = "Windows, iOS, Linux"
        var2 = StringVar(value=" ")
        rbtn_test_qw2_1 = Radiobutton(frm_test, font="Arial 12", text=qw2_1, value=qw2_1, variable=var2)
        rbtn_test_qw2_1.place(x=5, y=160)
        rbtn_test_qw2_2 = Radiobutton(frm_test, font="Arial 12", text=qw2_2, value=qw2_2, variable=var2)
        rbtn_test_qw2_2.place(x=5, y=185)
        rbtn_test_qw2_3 = Radiobutton(frm_test, font="Arial 12", text=qw2_3, value=qw2_3, variable=var2)
        rbtn_test_qw2_3.place(x=210, y=160)
        rbtn_test_qw2_4 = Radiobutton(frm_test, font="Arial 12", text=qw2_4, value=qw2_4, variable=var2)
        rbtn_test_qw2_4.place(x=5, y=210)
        # 3
        lbl_test_qw3_1 = Label(frm_test, text="Ответ: ", font="Arial 12").place(x=5, y=280)
        ent_test_qw3_1 = Entry(frm_test, font="Arial 12")
        ent_test_qw3_1.place(x=60, y=282)
        # 4
        qw4_1 = "Поток"
        qw4_2 = "Задача"
        qw4_3 = "Процесс"
        qw4_4 = "Обработка"
        var4 = StringVar(value=" ")
        rbtn_test_qw4_1 = Radiobutton(frm_test, font="Arial 12", text=qw4_1, value=qw4_1, variable=var4)
        rbtn_test_qw4_1.place(x=5, y=400)
        rbtn_test_qw4_2 = Radiobutton(frm_test, font="Arial 12", text=qw4_2, value=qw4_2, variable=var4)
        rbtn_test_qw4_2.place(x=5, y=450)
        rbtn_test_qw4_3 = Radiobutton(frm_test, font="Arial 12", text=qw4_3, value=qw4_3, variable=var4)
        rbtn_test_qw4_3.place(x=5, y=425)
        rbtn_test_qw4_4 = Radiobutton(frm_test, font="Arial 12", text=qw4_4, value=qw4_4, variable=var4)
        rbtn_test_qw4_4.place(x=95, y=400)
        # 5
        qw5_1 = "Мегазадачность"
        qw5_2 = "Многопоточность"
        qw5_3 = "Мультипоточность"
        qw5_4 = "Многозадачность"
        var5 = StringVar(value=" ")
        rbtn_test_qw5_1 = Radiobutton(frm_test, font="Arial 12", text=qw5_1, value=qw5_1, variable=var5)
        rbtn_test_qw5_1.place(x=5, y=520)
        rbtn_test_qw5_2 = Radiobutton(frm_test, font="Arial 12", text=qw5_2, value=qw5_2, variable=var5)
        rbtn_test_qw5_2.place(x=5, y=570)
        rbtn_test_qw5_3 = Radiobutton(frm_test, font="Arial 12", text=qw5_3, value=qw5_3, variable=var5)
        rbtn_test_qw5_3.place(x=5, y=545)
        rbtn_test_qw5_4 = Radiobutton(frm_test, font="Arial 12", text=qw5_4, value=qw5_4, variable=var5)
        rbtn_test_qw5_4.place(x=170, y=520)
        # 6
        qw6_1 = "алгоритм Хаффмана"
        qw6_2 = "алгоритм Хоффмана"
        qw6_3 = "алгоритм Альберта"
        qw6_4 = "алгоритм Эндрю"
        var6 = StringVar(value=" ")
        rbtn_test_qw6_1 = Radiobutton(frm_test, font="Arial 12", text=qw6_1, value=qw6_1, variable=var6)
        rbtn_test_qw6_1.place(x=5, y=640)
        rbtn_test_qw6_2 = Radiobutton(frm_test, font="Arial 12", text=qw6_2, value=qw6_2, variable=var6)
        rbtn_test_qw6_2.place(x=5, y=665)
        rbtn_test_qw6_3 = Radiobutton(frm_test, font="Arial 12", text=qw6_3, value=qw6_3, variable=var6)
        rbtn_test_qw6_3.place(x=5, y=690)
        rbtn_test_qw6_4 = Radiobutton(frm_test, font="Arial 12", text=qw6_4, value=qw6_4, variable=var6)
        rbtn_test_qw6_4.place(x=5, y=715)
    elif themes_titles == titles[2]:
        for string in lines6:
            lbl_test_qw = Label(frm_test, text=string, borderwidth=3, relief="groove", font="Arial 15").place(x=5, y=i)
            i += 120
        file6.close()
        # 1
        qw1_1 = "3"
        qw1_2 = "2"
        qw1_3 = "5"
        qw1_4 = "4"
        var1 = StringVar(value=" ")
        rbtn_test_qw1_1 = Radiobutton(frm_test, font="Arial 12", text=qw1_1, value=qw1_1, variable=var1)
        rbtn_test_qw1_1.place(x=5, y=45)
        rbtn_test_qw1_2 = Radiobutton(frm_test, font="Arial 12", text=qw1_2, value=qw1_2, variable=var1)
        rbtn_test_qw1_2.place(x=45, y=45)
        rbtn_test_qw1_3 = Radiobutton(frm_test, font="Arial 12", text=qw1_3, value=qw1_3, variable=var1)
        rbtn_test_qw1_3.place(x=5, y=70)
        rbtn_test_qw1_4 = Radiobutton(frm_test, font="Arial 12", text=qw1_4, value=qw1_4, variable=var1)
        rbtn_test_qw1_4.place(x=45, y=70)
        # 2
        qw2_1 = "СУБД информационных систем, Интегрированные пакеты"
        qw2_2 = "Интегрированные системы (офис), Интегрированные пакеты"
        qw2_3 = "Игры, Геоинформационные системы"
        qw2_4 = "Текстовый редактор, Электронная таблица"
        var2 = StringVar(value=" ")
        rbtn_test_qw2_1 = Radiobutton(frm_test, font="Arial 12", text=qw2_1, value=qw2_1, variable=var2)
        rbtn_test_qw2_1.place(x=5, y=160)
        rbtn_test_qw2_2 = Radiobutton(frm_test, font="Arial 12", text=qw2_2, value=qw2_2, variable=var2)
        rbtn_test_qw2_2.place(x=460, y=160)
        rbtn_test_qw2_3 = Radiobutton(frm_test, font="Arial 12", text=qw2_3, value=qw2_3, variable=var2)
        rbtn_test_qw2_3.place(x=5, y=185)
        rbtn_test_qw2_4 = Radiobutton(frm_test, font="Arial 12", text=qw2_4, value=qw2_4, variable=var2)
        rbtn_test_qw2_4.place(x=5, y=210)
        # 3
        qw3_1 = "Notepad, Excel"
        qw3_2 = "Word, NotePad"
        qw3_3 = "Excel, Lotus"
        qw3_4 = "Access, Lotus"
        var3 = StringVar(value=" ")
        rbtn_test_qw3_1 = Radiobutton(frm_test, font="Arial 12", text=qw3_1, value=qw3_1, variable=var3)
        rbtn_test_qw3_1.place(x=5, y=280)
        rbtn_test_qw3_2 = Radiobutton(frm_test, font="Arial 12", text=qw3_2, value=qw3_2, variable=var3)
        rbtn_test_qw3_2.place(x=140, y=280)
        rbtn_test_qw3_3 = Radiobutton(frm_test, font="Arial 12", text=qw3_3, value=qw3_3, variable=var3)
        rbtn_test_qw3_3.place(x=5, y=305)
        rbtn_test_qw3_4 = Radiobutton(frm_test, font="Arial 12", text=qw3_4, value=qw3_4, variable=var3)
        rbtn_test_qw3_4.place(x=5, y=330)
        # 4
        qw4_1 = "Excel"
        qw4_2 = "Word"
        qw4_3 = "Access"
        qw4_4 = "Notepad"
        var4 = StringVar(value=" ")
        rbtn_test_qw4_1 = Radiobutton(frm_test, font="Arial 12", text=qw4_1, value=qw4_1, variable=var4)
        rbtn_test_qw4_1.place(x=5, y=405)
        rbtn_test_qw4_2 = Radiobutton(frm_test, font="Arial 12", text=qw4_2, value=qw4_2, variable=var4)
        rbtn_test_qw4_2.place(x=85, y=405)
        rbtn_test_qw4_3 = Radiobutton(frm_test, font="Arial 12", text=qw4_3, value=qw4_3, variable=var4)
        rbtn_test_qw4_3.place(x=5, y=430)
        rbtn_test_qw4_4 = Radiobutton(frm_test, font="Arial 12", text=qw4_4, value=qw4_4, variable=var4)
        rbtn_test_qw4_4.place(x=85, y=430)
        # 5
        qw5_1 = "Из векторов"
        qw5_2 = "Из пикселей"
        qw5_3 = "Из растров"
        qw5_4 = "Из фракталов"
        var5 = StringVar(value=" ")
        rbtn_test_qw5_1 = Radiobutton(frm_test, font="Arial 12", text=qw5_1, value=qw5_1, variable=var5)
        rbtn_test_qw5_1.place(x=5, y=520)
        rbtn_test_qw5_2 = Radiobutton(frm_test, font="Arial 12", text=qw5_2, value=qw5_2, variable=var5)
        rbtn_test_qw5_2.place(x=125, y=520)
        rbtn_test_qw5_3 = Radiobutton(frm_test, font="Arial 12", text=qw5_3, value=qw5_3, variable=var5)
        rbtn_test_qw5_3.place(x=5, y=545)
        rbtn_test_qw5_4 = Radiobutton(frm_test, font="Arial 12", text=qw5_4, value=qw5_4, variable=var5)
        rbtn_test_qw5_4.place(x=5, y=570)
        # 6
        qw6_1 = "Word, Excel, PowerPoint, Outlook"
        qw6_2 = "PowerPoint, Excel, WinRa"
        qw6_3 = "Lotus, Excel, PowerPoint"
        qw6_4 = "ничего из перечисленного"
        var6 = StringVar(value=" ")
        rbtn_test_qw6_1 = Radiobutton(frm_test, font="Arial 12", text=qw6_1, value=qw6_1, variable=var6)
        rbtn_test_qw6_1.place(x=5, y=640)
        rbtn_test_qw6_2 = Radiobutton(frm_test, font="Arial 12", text=qw6_2, value=qw6_2, variable=var6)
        rbtn_test_qw6_2.place(x=5, y=665)
        rbtn_test_qw6_3 = Radiobutton(frm_test, font="Arial 12", text=qw6_3, value=qw6_3, variable=var6)
        rbtn_test_qw6_3.place(x=5, y=690)
        rbtn_test_qw6_4 = Radiobutton(frm_test, font="Arial 12", text=qw6_4, value=qw6_4, variable=var6)
        rbtn_test_qw6_4.place(x=5, y=715)
    themes.withdraw()
    test.protocol("WM_DELETE_WINDOW", on_closing_for_testWindow)
    test.mainloop()
def itogWindow(themes_titles):
    global itog, pravil
    itog = Tk()
    itog.state('zoomed')
    itog.title(f'Итоги темы "{themes_titles}"')
    itog.config(background="floralwhite")
    prav_lst = []
    if themes_titles == titles[0]:
        c1 = 0
        n1 = 0
        lbl_itog_knowledge_pod1 = Label(itog, text="- Об этапах в развитии устройств вычислений;", borderwidth= 3, relief="groove", background="snow", font="Arial 12").place(x=10,y=155)
        lbl_itog_knowledge_pod2 = Label(itog, text="- О поколеняих ЭВМ;", borderwidth= 3, relief="groove", background="snow", font="Arial 12").place(x=10,y=188)
        lbl_itog_knowledge_pod3 = Label(itog, text="- О типах ЭВМ.", borderwidth=3, relief="groove", background="snow", font="Arial 12").place(x=10, y=221)
        if var1.get() == "8":
            c1 += 1
            prav = "1"
            prav_lst.append(prav)
        else:
            n1 += 1
            prav = "0"
            prav_lst.append(prav)
        if var2.get() == "4":
            c1 += 1
            prav = "1"
            prav_lst.append(prav)
        else:
            n1 += 1
            prav = "0"
            prav_lst.append(prav)
        if var3.get() == "50-е":
            c1 += 1
            prav = "1"
            prav_lst.append(prav)
        else:
            n1 += 1
            prav = "0"
            prav_lst.append(prav)
        if var4.get() == "60-е":
            c1 += 1
            prav = "1"
            prav_lst.append(prav)
        else:
            n1 += 1
            prav = "0"
            prav_lst.append(prav)
        if var5.get() == "ENIAC":
            c1 += 1
            prav = "1"
            prav_lst.append(prav)
        else:
            n1 += 1
            prav = "0"
            prav_lst.append(prav)
        if var6.get() == "микроЭВМ":
            c1 += 1
            prav = "1"
            prav_lst.append(prav)
        else:
            n1 += 1
            prav = "0"
            prav_lst.append(prav)
        lbl_itog_test_pod = Label(itog, text=f"Вы ответили правильно на \n{c1} вопрос(-ов) и \nна {n1} вопросов неправильно", borderwidth=3, relief="groove", background="snow", font="Arial 12").place(x=10, y=298)
        pravil = [f"1) 8 ({prav_lst[0]})", f"2) 4 ({prav_lst[1]})", f"3) 50-e ({prav_lst[2]})", f"4) 60-e ({prav_lst[3]})", f"5) ENIAC ({prav_lst[4]})", f"6) микроЭВМ ({prav_lst[5]})"]
        # данные о тесте записываются в файл
        with open(f"svodka/{tmp_username_and_pass}.txt", "a", encoding="utf-8") as file:
            file.write("Ответы на 1-ый тест:\n")
            i = 1
            for item in prav_lst:
                file.write(f"{i}) {item}")
                if item != "6) 0":
                    file.write("\n")
                i += 1
        with open(f"groups/{password}.txt", "a", encoding="utf-8") as file:
            file.write(f"Ответы на 1-ый тест: {username}\n")
            i = 1
            for item in prav_lst:
                file.write(f"{i}) {item}")
                if item != "6) 0":
                    file.write("\n")
                i += 1
    elif themes_titles == titles[1]:
        c1 = 0
        n1 = 0
        lbl_itog_knowledge_pod1 = Label(itog, text="- О структуре программного обеспечения;", borderwidth=3, relief="groove", background="snow", font="Arial 12").place(x=10, y=155)
        lbl_itog_knowledge_pod2 = Label(itog, text="- О системном программном обеспечении;", borderwidth=3, relief="groove", background="snow", font="Arial 12").place(x=10, y=188)
        lbl_itog_knowledge_pod3 = Label(itog, text="- Об алгоритме Хаффмана.", borderwidth=3, relief="groove", background="snow", font="Arial 12").place(x=10, y=221)
        if var1.get() == "3":
            c1 += 1
            prav = "1"
            prav_lst.append(prav)
        else:
            n1 += 1
            prav = "0"
            prav_lst.append(prav)
        if var2.get() == "Windows, Mac OS, Linux":
            c1 += 1
            prav = "1"
            prav_lst.append(prav)
        else:
            n1 += 1
            prav = "0"
            prav_lst.append(prav)
        if ent_test_qw3_1.get().capitalize() == "Android":
            c1 += 1
            prav = "1"
            prav_lst.append(prav)
        else:
            n1 += 1
            prav = "0"
            prav_lst.append(prav)
        if var4.get() == "Процесс":
            c1 += 1
            prav = "1"
            prav_lst.append(prav)
        else:
            n1 += 1
            prav = "0"
            prav_lst.append(prav)
        if var5.get() == "Многозадачность":
            c1 += 1
            prav = "1"
            prav_lst.append(prav)
        else:
            n1 += 1
            prav = "0"
            prav_lst.append(prav)
        if var6.get() == "алгоритм Хаффмана":
            c1 += 1
            prav = "1"
            prav_lst.append(prav)
        else:
            n1 += 1
            prav = "0"
            prav_lst.append(prav)
        lbl_itog_test_pod = Label(itog, text=f"Вы ответили правильно на \n{c1} вопрос(-ов) и \nна {n1} вопросов неправильно", borderwidth=3, relief="groove", background="snow", font="Arial 12").place(x=10, y=298)
        pravil = [f"1) 3 ({prav_lst[0]})", f"2) Windows, Mac OS, Linux ({prav_lst[1]})", f"3) Android ({prav_lst[2]})", f"4) Процесс ({prav_lst[3]})", f"5) Многозадачность ({prav_lst[4]})", f"6) алгоритм Хаффмана ({prav_lst[5]})"]
        # данные о тесте записываются в файл
        with open(f"svodka/{tmp_username_and_pass}.txt", "a", encoding="utf-8") as file:
            file.write("Ответы на 2-ой тест:\n")
            i = 1
            for item in prav_lst:
                file.write("%s\n" % f"{i}) {item}")
                i += 1
        with open(f"groups/{password}.txt", "a", encoding="utf-8") as file:
            file.write(f"Ответы на 2-ой тест: {username}\n")
            i = 1
            for item in prav_lst:
                file.write(f"{i}) {item}")
                if item != "6) 0":
                    file.write("\n")
                i += 1
    elif themes_titles == titles[2]:
        c1 = 0
        n1 = 0
        lbl_itog_knowledge_pod1 = Label(itog, text="- О понятии и классификации прикладного ПО;", borderwidth=3, relief="groove", background="snow", font="Arial 12").place(x=10, y=155)
        lbl_itog_knowledge_pod2 = Label(itog, text="- О ППО общего назначения;", borderwidth=3, relief="groove", background="snow", font="Arial 12").place(x=10, y=188)
        lbl_itog_knowledge_pod3 = Label(itog, text="- О пакете интегрированных программ Microsoft Office.", borderwidth=3, relief="groove", background="snow", font="Arial 12").place(x=10, y=221)
        if var1.get() == "3":
            c1 += 1
            prav = "1"
            prav_lst.append(prav)
        else:
            n1 += 1
            prav = "0"
            prav_lst.append(prav)
        if var2.get() == "Текстовый редактор, Электронная таблица":
            c1 += 1
            prav = "1"
            prav_lst.append(prav)
        else:
            n1 += 1
            prav = "0"
            prav_lst.append(prav)
        if var3.get() == "Excel, Lotus":
            c1 += 1
            prav = "1"
            prav_lst.append(prav)
        else:
            n1 += 1
            prav = "0"
            prav_lst.append(prav)
        if var4.get() == "Access":
            c1 += 1
            prav = "1"
            prav_lst.append(prav)
        else:
            n1 += 1
            prav = "0"
            prav_lst.append(prav)
        if var5.get() == "Из пикселей":
            c1 += 1
            prav = "1"
            prav_lst.append(prav)
        else:
            n1 += 1
            prav = "0"
            prav_lst.append(prav)
        if var6.get() == "Word, Excel, PowerPoint, Outlook":
            c1 += 1
            prav = "1"
            prav_lst.append(prav)
        else:
            n1 += 1
            prav = "0"
            prav_lst.append(prav)
        lbl_itog_test_pod = Label(itog, text=f"Вы ответили правильно на \n{c1} вопрос(-ов) и \nна {n1} вопросов неправильно", borderwidth=3, relief="groove", background="snow", font="Arial 12").place(x=10, y=298)
        pravil = [f"1) 3 ({prav_lst[0]})", f"2) Текстовый редактор, Электронная таблица ({prav_lst[1]})", f"3) Excel, Lotus ({prav_lst[2]})", f"4) Access ({prav_lst[3]})", f"5) Из пикселей ({prav_lst[4]})", f"6) Word, Excel, PowerPoint, Outlook ({prav_lst[5]})"]
        # данные о тесте записываются в файл
        with open(f"svodka/{tmp_username_and_pass}.txt", "a", encoding="utf-8") as file:
            file.write("Ответы на 3-ий тест:\n")
            i = 1
            for item in prav_lst:
                file.write("%s\n" % f"{i}) {item}")
                i += 1
        with open(f"groups/{password}.txt", "a", encoding="utf-8") as file:
            file.write(f"Ответы на 3-ий тест: {username}\n")
            i = 1
            for item in prav_lst:
                file.write(f"{i}) {item}")
                if item != "6) 0":
                    file.write("\n")
                i += 1
    lbl_itog_test_pravil = Label(itog, text="Правильные ответы на тест: (1 или 0)", background="snow", font="Arial 12").place(x=10, y=365)
    i = 390
    for string in pravil:
        lbl_itog_test_var = Label(itog, text=string, background="snow", font="Arial 11").place(x=10, y=i)
        i += 25
    lbl_itog_title = Label(itog, text=f'Итоги', font="Trebuchet 50", borderwidth=9, relief="groove", background="snow").place(x=10,y=10)
    lbl_itog_knowledge = Label(itog, text="Что мы узнали:", borderwidth=3, relief="groove", background="snow", font="Arial 18").place(x=10, y=112)
    lbl_itog_test = Label(itog, text="Итоги теста: ", borderwidth=3, relief="groove", background="snow", font="Arial 18").place(x=10, y=255)
    btn_home = Button(itog, text="Перейти на главную страницу темы", font="Trebuchet 15", borderwidth=3,relief="groove", background="snow", command=on_closing_for_itogWindow).place(x=793,y=957)
    btn_test_to_practical = Button(itog, text="Перейти обратно к тестовой части", font="Trebuchet 15", borderwidth=3,relief="groove", background="snow", command=itog_to_test).place(x=10,y=957)
    test.destroy()
    itog.protocol("WM_DELETE_WINDOW", on_closing_for_itogWindow)
    itog.mainloop()
registerWindow()
# textbookWindow()
