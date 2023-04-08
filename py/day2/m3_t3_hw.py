"""
Задача №5
Строка из нескольких слов, не более 10.
Определите, сколько букв содержит самое длинное слово в строке.
Пример:
In: Как дела в учебе
Out: 5
"""
import string as st


words = input(
    "Введите строку из нескольких слов через пробел, не более 10: ")
ind = 0
puncts = st.punctuation

if (ind := words.find(' ')) > 0:
    tmp_word = ''
    rest_w = words[ind + 1:].strip(puncts)
    w_len = len(words[:ind].strip(puncts))
    while ' ' in rest_w:
        ind = rest_w.index(' ')
        tmp_word = rest_w[:ind].strip(puncts)
        if len(tmp_word) > w_len:
            w_len = len(tmp_word)
        rest_w = rest_w[ind + 1:]
    else:
        if len(rest_w) > 0 and len(rest_w) > w_len:
            w_len = len(rest_w)

    print(f'Количество букв в самом длинном слове: {w_len}')
else:
    print('В строке менее двух слов')
