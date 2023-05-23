# Напишите следующие функции:
#   ○ Нахождение корней квадратного уравнения
#   ○ Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
#   ○ Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
#   ○ Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
import csv
import json
import random
from functools import wraps


def read_from_csv(file_name):
    '''Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.'''

    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with open(file_name, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                for num, row in enumerate(reader):
                    if num == 0:
                        continue
                    args = [complex(i) for i in row]
                    yield (row, func(*args, **kwargs))

        return wrapper

    return deco


def write_to_json(func):
    '''Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.'''

    json_file = []
    file_name = f'{__file__[:-3]}.json'

    def wrapper(*args, **kwargs):

        for key, result in func(*args, **kwargs):
            if result:
                my_dict = {'arguments': key, 'result': str(result)}
                json_file.append(my_dict)
                with open(file_name, 'w', encoding='utf-8') as f:
                    json.dump(json_file, f, indent=2)
        return

    return wrapper


def csv_generation():
    '''Генерируем файл с тремя случайными числами в каждой строке.'''

    with open(f'{__file__[:-3]}.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['a', 'b', 'c'])
        for i in range(random.randint(100, 1001)):
            writer.writerow([random.randint(-1000, 1001), random.randint(-1000, 1001), random.randint(-1000, 1001)])


@write_to_json
@read_from_csv(f'{__file__[:-3]}.csv')
def quadratic(a: complex, b: complex, c: complex):
    '''Нахождение корней квадратного уравнения.'''

    if a != 0:
        discr: complex = b * b - 4 * a * c
        x1: complex = (-b + discr ** 0.5) / (2 * a)
        x2: complex = (-b - discr ** 0.5) / (2 * a)
        return x1, x2
    else:
        return None


if __name__ == '__main__':
    csv_generation()
    quadratic()
