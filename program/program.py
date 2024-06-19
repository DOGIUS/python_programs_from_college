from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from os import listdir
from os.path import isfile, join
import os
from functools import partial
import re

def requestWindow(): # окно регистрации
    global request
    def register_reg():  # считывание данных при регистрации
        requests_files = [f for f in listdir("requests") if isfile(join("requests", f))]
        request_number = 1
        for i in requests_files:
            request_number += 1
        try:
            full_name = ent_fcs.get()
            phone_number = ent_phonenumber.get()
            reason = txt_reason.get("1.0","end-1c")
            category = cmbbox_type.get()
            split_name = full_name.split()
            last_name = split_name[0]
            first_name = split_name[1]
            patronymic = split_name[2] if len(split_name) > 2 else ""
            tmp_username = last_name + "_" + first_name + "_" + patronymic
            FCs = []
            group = []
            if not full_name or not phone_number or not category or len(reason) == 0:
                showerror("Ошибка", "Заполните все поля")
                return
            else:
                with open(f"requests/{request_number}.txt", "a", encoding="utf-8") as file:
                    file.write(f"Заявка №{request_number}\n")
                    file.write(f"ФИО: {full_name}\n")
                    file.write(f"Номер телефона: {phone_number}\n")
                    file.write(f"Категория услуги: {category}\n")
                    file.write(f"Описание заявки: {reason}\n")
                    file.write("-------------------------------\n")
                ent_fcs.delete(0, END)
                ent_phonenumber.delete(0, END)
                cmbbox_type.delete(0, END)
                txt_reason.delete(1.0, END)
                showinfo("Сообщение", "Заявка была успешно зарегистрирована")
        except:
            showerror("Ошибка", "Введите данные корректно")
    tp_req = Tk()
    request = Toplevel()
    request.title("Регистрация")
    request.state("zoomed")
    request.config(background="floralwhite")
    lbl_request = Label(request, font="Arial 40" ,text="Ваша заявка", borderwidth=5, relief="ridge",background="snow").place(x=813, y=270)
    lbl_fcs = Label(request, text="ФИО:",font="Arial 15",background="floralwhite", borderwidth=3, relief="groove").place(x=670, y=380)
    ent_fcs = Entry(request, font="Arial 15", width=40,borderwidth=5, background="snow", relief="groove")
    ent_fcs.place(x=750,y=380)
    lbl_phonenumber = Label(request, text="Номер телефона:", font="Arial 15",background="floralwhite", borderwidth=3, relief="groove").place(x=560, y=450)
    ent_phonenumber = Entry(request, font="Arial 15", width=40, borderwidth=5, background="snow", relief="groove")
    ent_phonenumber.place(x=750, y=450)
    lbl_type = Label(request, text="Категория услуги:", font="Arial 15", background="floralwhite", borderwidth=3, relief="groove").place(x=560, y=520)
    variants = ["Обслуживание или замена оборудования", "Проверка оборудования на наличие неисправностей",
                "Другое (подробнее в описании заявки)"]
    cmbbox_type = ttk.Combobox(request, font="Arial 15", background="snow", width=38, height=6, values=variants)
    cmbbox_type.place(x=753, y=523)
    lbl_reason = Label(request, text="Описание заявки:", font="Arial 15", background="floralwhite", borderwidth=3, relief="groove").place(x=560, y=592)
    txt_reason = Text(request, font="Arial 15", background="snow", borderwidth=5, relief="groove", width=40, height=6)
    txt_reason.place(x=750, y=595)
    btn_register = Button(request, text="Зарегистрировать заявку", font="Arial 15", width=23, borderwidth=2, relief="groove", command=register_reg, background="snow")
    btn_register.place(x=837, y=781)
    btn_itog_prepod_svodka = Button(request, text="Посмотреть все заявки", font="Trebuchet 15", borderwidth=3,
                                    relief="groove", background="snow", command=listrequestsWindow)
    btn_itog_prepod_svodka.place(x=867, y=30)
    tp_req.withdraw()
    request.mainloop()
def listrequestsWindow():
    global listreq, tmp_list_buttons
    def on_closing_listrequest_Window():
        listreq.destroy()
        requestWindow()
    def scroll(event):
        canvas.configure(scrollregion=canvas.bbox("all"), width=700, height=895)
    requests_files = [f for f in listdir("requests") if isfile(join("requests", f))]
    listreq = Tk()
    listreq.state('zoomed')
    listreq.title("Заявки")
    listreq.config(background="floralwhite")
    listreq.protocol("WM_DELETE_WINDOW", on_closing_listrequest_Window)
    frm_listreq = Frame(listreq, width=700, height=900, borderwidth=5, relief="groove")
    frm_listreq.place(x=10,y=100)
    canvas = Canvas(frm_listreq, width=200, height=200,background="snow")
    frame = Frame(canvas,background="snow")
    scrollbar = Scrollbar(frm_listreq, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left")
    canvas.create_window((0, 0), window=frame, anchor='nw')
    frame.bind("<Configure>", scroll)
    lbl_listreq = Label(listreq, font="Arial 40", text="Заявки пользователей", borderwidth=5, relief="ridge", background="snow").place(x=700, y=10)
    i = 10
    tmp_list = []
    tmp_list_buttons = []
    odobr = " - одобрена.txt"
    otkl = " - отклонена.txt"
    for filename in requests_files:
        if ".txt" in filename and len(filename) <= 5:
            filename_changed = filename.replace(".txt", "")
        if odobr in filename:
            filename_changed = filename.replace(f"{odobr}", "")
        if otkl in filename:
            filename_changed = filename.replace(f"{otkl}", "")
        tmp_list.append(int(filename_changed))
        tmp_list.sort()
    # requests_files.sort(key=lambda x: x.split()[1:1])
    for filename in requests_files:
        def atoi(filename):
            return int(filename) if filename.isdigit() else filename
        def natural_keys(filename):
            return [atoi(c) for c in re.split(r'(\d+)', filename)]
        requests_files.sort(key=natural_keys)
        # filename = str(filename) + ".txt"
        btn_request_view = Button(frame, text=f"Заявка №{filename.replace('.txt', '')}", font="Trebuchet 14", borderwidth=3, relief="groove", background="snow", command=lambda name=filename: listreq_statistics(name))
        btn_request_view.pack(anchor="nw",padx=4,pady=4)
        tmp_list_buttons.append(btn_request_view)
        i += 50
    def request_yes(filename):
        odobr = " - одобрена.txt"
        otkl = " - отклонена.txt"
        file_path = os.path.abspath(f"requests/{filename}")
        file_path1 = os.path.abspath("requests")
        listreq.withdraw()
        if ".txt" in filename and len(filename) <= 6:
            tmp_list_buttons[int(filename.replace('.txt', '')) - 1][
                "text"] = f"Заявка №{filename.replace('.txt', '')} - одобрена"
            var = tmp_list_buttons[int(filename.replace('.txt', '')) - 1]['text'][8:]
            os.rename(f"{file_path}", f"{file_path1}\\{var}.txt")
        if odobr in filename:
            tmp_list_buttons[int(filename.replace(f'{odobr}', '')) - 1][
                "text"] = f"Заявка №{filename.replace(f'{odobr}', '')} - одобрена"
            var = tmp_list_buttons[int(filename.replace(f'{odobr}', '')) - 1]["text"][8:]
            os.rename(f"{file_path}", f"{file_path1}\\{var}.txt")
        if otkl in filename:
            tmp_list_buttons[int(filename.replace(f'{otkl}', '')) - 1][
                "text"] = f"Заявка №{filename.replace(f'{otkl}', '')} - одобрена"
            var = tmp_list_buttons[int(filename.replace(f'{otkl}', '')) - 1]["text"][8:]
            os.rename(f"{file_path}", f"{file_path1}\\{var}.txt")
        listrequestsWindow()
    def request_no(filename):
        odobr = " - одобрена.txt"
        otkl = " - отклонена.txt"
        file_path = os.path.abspath(f"requests/{filename}")
        file_path1 = os.path.abspath("requests")
        listreq.withdraw()
        if ".txt" in filename and len(filename) <= 6:
            tmp_list_buttons[int(filename.replace('.txt', '')) - 1][
                "text"] = f"Заявка №{filename.replace('.txt', '')} - отклонена"
            var = tmp_list_buttons[int(filename.replace('.txt', '')) - 1]['text'][8:]
            os.rename(f"{file_path}", f"{file_path1}\\{var}.txt")
        if odobr in filename:
            tmp_list_buttons[int(filename.replace(f'{odobr}', '')) - 1][
                "text"] = f"Заявка №{filename.replace(f'{odobr}', '')} - отклонена"
            var = tmp_list_buttons[int(filename.replace(f'{odobr}', '')) - 1]["text"][8:]
            os.rename(f"{file_path}", f"{file_path1}\\{var}.txt")
        if otkl in filename:
            tmp_list_buttons[int(filename.replace(f'{otkl}', '')) - 1][
                "text"] = f"Заявка №{filename.replace(f'{otkl}', '')} - отклонена"
            var = tmp_list_buttons[int(filename.replace(f'{otkl}', '')) - 1]["text"][8:]
            os.rename(f"{file_path}", f"{file_path1}\\{var}.txt")
        listrequestsWindow()
    def listreq_statistics(filename):
        file_path = os.path.abspath(f"requests/{filename}")
        with open(f'{file_path}', 'r', encoding="UTF-8") as file:
            data = file.read()
        txt_listreq = Text(listreq, background="snow", width=40, height=22,font="Arial 15")
        txt_listreq.place(x=1050, y=100)
        txt_listreq.insert("1.0", data)
        txt_listreq["state"] = DISABLED
        btn_yes = Button(listreq, text="Одобрить заявку", font="Arial 15", width=15, borderwidth=2, relief="groove", background="snow", command= partial(request_yes,filename))
        btn_yes.place(x=1050, y=630)
        btn_no = Button(listreq, text="Отклонить заявку", font="Arial 15", width=15, borderwidth=2, relief="groove", background="snow", command= partial(request_no,filename))
        btn_no.place(x=1319, y=630)
    request.withdraw()
    listreq.mainloop()

requestWindow()
