"""
Задача №2
Задаем количество коробок от 0 до 2000.
Нужно вывести количество и слово короб<?> с правильным окончанием.
Пример :
In: 5
Out: 5 коробок

In: 1
Out: 1 коробка

In: 22
Out: 22 коробки

*Если решение универсальное, то будет работать правильно на любом количестве
"""
box_quantity = input("Введите количество коробок от 0 до 2000: ")
ending = 'ок'

if int(box_quantity) not in range(0, 2001):
    print("Вы ввели некоректное значение")
    exit()

if int(box_quantity[-1]) == 1 and int(box_quantity[-2:]) != 11:
    ending = 'ка'
elif int(box_quantity[-1]) in range(2, 5) and int(box_quantity[-2:]) not in range(12, 20):
    ending = 'ки'

print(f'У вас {box_quantity} короб{ending}!')
