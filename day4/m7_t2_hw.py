"""
Задача №3
Написать функцию, которая находит все файлы заданного расширения и
перемещает(не копирует, а именно переносит) их в подпапку backup
относительно текущей директории.
Если папка backup есть, то мы ее используем, если нет, ее нужно создать.
"""
import os


def file_backup(ext='.txt') -> str:

    out = ''
    cur_dir = os.listdir(os.curdir)

    if not os.path.exists('backup'):
        os.mkdir('backup')
        out = 'Создана папка'

    for file in cur_dir:
        if os.path.splitext(file)[1] == ext:
            # ## Перемещение файла
            os.replace(file, os.path.join("backup", file))
            out = 'Файлы скопированы'

    return out


print(file_backup())
