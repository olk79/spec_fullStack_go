"""
Задача №5
Написать программу, которая расшифрует строку,
используя набор букв из модуля string(string.ascii_lowercase),
Каждый символ - это две цифры.
Отсчет с 00 -> 'a', 01 -> 'b' и до 25 -> 'z',
26 - это пробел, он не входит в набор букв
Вход: строка из цифр. Выход: Текст.

Проверка работы программы выполняется через вторую строку.

* реализовать и расшифровку и зашифровку
"""
import string

code = '070411111426152419071413'

s_str = string.ascii_lowercase + ' '
lst = []
for i in range(0, len(code), 2):
    el = int(code[i:i + 2])
    lst.append(s_str[el])

print('decrypted - ', *lst, sep='')

c_lst = []
for i in lst:
    c_lst.append(f'{s_str.index(i):02}')

print('encrypted - ', *c_lst, sep='')
