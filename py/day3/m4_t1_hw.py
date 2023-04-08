"""
Задача №1.
Программа получает на вход последовательность целых чисел N(от 2 до 10).

Вам нужно определить вид последовательности:
 - возрастающая
 - убывающая
 - случайная
 - постоянная

В качестве ответа следуют выдать прописными латинскими буквами тип последовательности:
1. ASCENDING (строго возрастающая)
2. WEAKLY ASCENDING (нестрого возрастающая, то есть неубывающая)
3. DESCENDING (строго убывающая)
4. WEAKLY DESCENDING (нестрого убывающая, то есть невозрастающая)
5. CONSTANT (постоянная)
6. RANDOM (случайная)

Примеры входных и выходных данных:
In: 9 4 2 -1  Out: DESCENDING
In: 3 8 8 11  Out: WEAKLY ASCENDING
In: 2 -1 7    Out: RANDOM
In: 5 5 5 5   Out: CONSTANT
"""


def serial_test(ser: list):
    out = ''
    lst = []
    length = len(ser) - 1

    for i in range(length):
        if ser[i] < ser[i + 1]:
            lst.append(1)
        elif ser[i] > ser[i + 1]:
            lst.append(0)
        else:
            lst.append(None)

    if lst.count(True) == length:
        out = 'ASCENDING'
    elif lst.count(None) == length:
        out = 'CONSTANT'
    elif lst.count(False) == length:
        out = 'DESCENDING'
    elif lst.count(True) and lst.count(None) and not lst.count(False):
        out = 'WEAKLY ASCENDING'
    elif lst.count(False) and lst.count(None) and not lst.count(True):
        out = 'WEAKLY DESCENDING'
    elif lst.count(False) and lst.count(True):
        out = 'RANDOM'

    return out


series_dsc = [9, 4, 2, -1, -2]
series_asc = [-1, 4, 8, 12, 15]
series_cns = [5, 5, 5, 5, 5]
series_asc_w = [9, 12, 12, 13]
series_dsc_w = [9, 4, 4, -1]
series_rnd = [9, 10, 4, 20]


print(serial_test(series_dsc))
print(serial_test(series_asc))
print(serial_test(series_cns))
print(serial_test(series_asc_w))
print(serial_test(series_dsc_w))
print(serial_test(series_rnd))
