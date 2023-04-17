# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os

path = "C:/Users/1/Documents/Файлы Outlook/krial11@rambler.ru.pst"


def path_out(my_path):
    my_path, filename = os.path.split(my_path)
    name, extension = os.path.splitext(filename)
    return my_path, name, extension


print(path_out(path))
