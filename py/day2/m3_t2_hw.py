"""
Задача №4
Дана строка из двух слов. Поменяйте эти слова местами.
Пример:
In: 'Hello Python'
Out: 'Python Hello'

Используем str.index(), срезы.
! Списки еще не придумали !
"""

words = input("Введите строку из двух слов через пробел: ")
ind = 0

if (ind := words.find(' ')) > 0:
    word1 = words[:ind]
    word2 = words[ind + 1:]
    print(f'{word2} {word1}')
else:
    print('В строке менее двух слов')




