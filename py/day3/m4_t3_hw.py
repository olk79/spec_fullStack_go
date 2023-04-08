"""
Задача №3
Дана строка. Необходимо посчитать количество вхождений каждого символа.
Пример:
In: Hello, Python1.
Out:
H: 1
e: 1
h: 1
l: 2
o: 2
,: 1
P: 1
y: 1
t: 1
n: 1
1: 1
 : 1
.: 1
"""

in_str = input('Введите строку: ')
unique = []
for el in in_str:
    if el not in unique:
        unique.append(el)
        print(f'{unique[unique.index(el)]}: {in_str.count(el)}')




