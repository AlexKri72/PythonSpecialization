# Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции
from random import randint, uniform


def safe_text(str_count: int, file_name: str):
    '''Записываем в файл случайные числа.'''

    with open(file_name, 'a', encoding='UTF-8') as file:
        for i in range(str_count):
            file.writelines(f'{randint(-1000, 1001):>5}|{uniform(-1000, 1000):.3f}\n')


safe_text(5, 'Task01.txt')
