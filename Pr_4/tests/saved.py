def registerWindow(): # окно регистрации
    global ent_fcs, ent_group, register
        def regis():  # считывание данных при регистрации
        global FCs, group
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
        str_full_name = last_name + " " + first_name + " " + patronymic
        str_group_name = group_name
        data = {str_full_name: str_group_name}
        print(data)
        with open("users.pickle", "wb") as file:
            pickle.dump(data, file)
    def enter():
        username = ent_fcs.get()
        password = ent_group.get()
        try:
            with open("users.pickle", "rb") as file:
                data = pickle.load(file)
                if data.get(username) == password:
                    showinfo(title="Сообщение", message="Успешная авторизация")
                    if data.get("d d d") == "d":
                        g = 1
                    else:
                        g = 2
                    textbookWindow(g)
                else:
                    showerror(title="Ошибка", message="Неправильный формат данных")
        except FileNotFoundError:
            showerror(title="Ошибка", message="Нет такого зарегистрированного пользователя")
