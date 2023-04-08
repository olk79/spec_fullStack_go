"""
Задача №2
Написать программу для подсчета размера всех .py файлов в текущей папке.
*Оформить решение в виде функции с одним аргументом(расширение файлов).
"""
import os


def file_count(ext='.py') -> dict:

    out = {}
    # Список файлов и директорий
    for file in os.listdir(os.curdir):
        if os.path.splitext(file)[1] == ext:
            out.update({file: os.path.getsize(file)})

    return out


print(f'Размер файлов в байтах : {file_count()}')
