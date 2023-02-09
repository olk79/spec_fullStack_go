'''
Задача №1
Вход:
Пользователь должен ввести 'правильный' пароль, состоящий из:
цифр, букв латинского алфавита(строчные и прописные) и
специальных символов  special = '_!@#$%^&'.
Всего 4 набора различных символов.
В пароле обязательно должен быть хотя бы один символ из каждого набора.
Длина пароля от 8(мин) до 15(макс) символов включительно.
Максимальное количество попыток ввода неправильного пароля - 5.
Каждый раз выводим номер попытки.
Желательно выводить пояснение, почему пароль не принят и что нужно исправить.

* Добавить проверку, что в пароле только символы из 4-х наборов.

Как вариант:
check_password('some string') -> tuple[bool, str]
(True, reasons)
(False, reasons)


Оформить решения в виде модуля

import string as st
st.digits
st.ascii_lowercase
st.ascii_uppercase
special = '_!@#$%^&'

Выход:
пароль подходит / не подходит

Пример:
пароль подходит -> o58anuahaunH!
пароль подходит -> aaaAAA111!!!
пароль не подходит -> saucacAusacu8
'''

import string as st


def login_check(psw: str) -> tuple:
    """
    Function for testing of passwords.
    Min password length = 8.
    Max password length = 15
    Specail symbols are required
    Status - True if password is good
    """
    status = False
    dig = st.digits
    lat_l = st.ascii_lowercase
    lat_u = st.ascii_uppercase
    spec = '_!@#$%^&'
    dsc = ["Ура! отличный пароль!",
           "Пароль не соотвествует требованиям длины 8 - 15",
           "Отсутсвуют цифры", "Отсутсвуют буквы", "Отсутвуют заглавные буквы",
           "Отсутсвуют спец символы"]

    err = [i > 1 for i in range(6)]

    descr = []

    if not 8 <= len(psw) <= 15:
        err = [False for i in range(6)]
        err[1] = True
    else:
        for el in psw:
            if err[2] and dig.count(el):
                err[2] = False
            elif err[3] and lat_l.count(el):
                err[3] = False
            elif err[4] and lat_u.count(el):
                err[4] = False
            elif err[5] and spec.count(el):
                err[5] = False

            if status := not any(err):
                break

    descr = [dsc[i] for i in range(len(dsc)) if err[i]]

    if len(descr) == 0:
        descr.append(dsc[0])

    return status, *descr


if __name__ == "__main__":

    attempts = 5
    badpass = True

    while badpass and attempts:
        if attempts:
            res = login_check(input("Введите надёжный пароль: "))
            badpass = not res[0]
            attempts -= 1
            print(*res, sep=" | ")
            if badpass:
                print("Осталось - ", str(attempts))
