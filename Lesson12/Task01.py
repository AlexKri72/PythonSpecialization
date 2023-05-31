# Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
#   -Экземпляр должен запоминать последние k значений.
#   -Параметр k передаётся при создании экземпляра.
#   -Добавьте метод для просмотра ранее вызываемых значений и их факториалов.
import math


class Factorial:

    def __init__(self):
        self.archive = {}

    def __call__(self, num, k):
        k = k if k < num else num
        self.archive[num] = math.factorial(num)
        my_dict = {}
        for i in range(num - 1, num - 1 - k, -1):
            my_dict[i] = math.factorial(i)
        return f'Факториал числа {num} равен {math.factorial(num)}, {my_dict}'

    def get_archive(self):
        print('Архив запросов:')
        return [print(key, ":", value) for key, value in self.archive.items()]


if __name__ == '__main__':
    f = Factorial()
    print(f(10, 3))
    print(f(12, 2))
    print(f(4, 10))
    print(f(8, 3))
    print(f.get_archive())
