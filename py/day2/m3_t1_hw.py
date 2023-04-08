"""
Задача №3
Дано слово из символов(латинские буквы + цифры), других нет.
Нужно вывести новой строкой только цифры, если они есть или
написать, что их нет.
Пример:
In: 'antuh1ouou21au3'
Out: 1213

In: 'sauhsauhasnhuasnhu'
Out: 'no digits'

Подсказки, что использовать:
while,индексация для элементов строки или for, str.isdigit()
"""
word = input("Введите слово используя латинские буквы и цифры: ")
res = ''

for el in word:
    if str(el).isdigit():
        res += el
if len(res):
    print(res)
else:
    print('no digits')
