# Доработаем задачу 1.
# Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл.
import json
from math import factorial
import os


class Factorial:

    def __init__(self):
        self.archive = {}

    def __call__(self, num, k):
        k = k if k < num else num
        self.archive[num] = factorial(num)
        my_dict = {}
        for i in range(num - 1, num - 1 - k, -1):
            my_dict[i] = factorial(i)
        return f'Факториал числа {num} равен {factorial(num)}, {my_dict}'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        file_name = f'{os.path.basename(__file__)[:-3]}.json'
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(self.archive, f, indent=2)

    def get_archive(self):
        print('Архив запросов:')
        return [print(key, ":", value) for key, value in self.archive.items()]


if __name__ == '__main__':
    with Factorial() as fact:
        print(fact(10, 3))
        print(fact.get_archive())
