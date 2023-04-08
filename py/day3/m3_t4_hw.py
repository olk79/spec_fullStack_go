"""
Задача №1.
Вывести на экран две буквы 'E' и 'N',
с учетом масштабируемости(можно менять количество строк для вывода >= 7)
******
*
*
******
*
*
******

**      *
* *     *
*  *    *
*   *   *
*    *  *
*     * *
*      **

"""

size = int(input("Введите количество строк вывода буквы: "))

if size < 7:
    size = 7

scale_e = size - 1
scale_n = size + 2
e_gap_size = (size - 3) // 2
n_gap_size = (scale_n - 3)

# Печать буквы E
print(' ')
for i in range(3):
    print('*' * scale_e)
    if i < 2:
        for x in range(e_gap_size):
            print('*')

# Печать буквы N
print(' ')
for i in range(size):
    print('*', ' ' * i, '*', ' ' * (n_gap_size - i), '*', sep='')







