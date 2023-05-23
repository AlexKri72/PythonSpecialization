# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функцию- угадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами из диапазонов.
import random

from typing import Callable


def one(func: Callable):
    def three(num, count):
        num = num if 1 <= num <= 100 else random.randint(1, 101)
        count = count if 1 <= count <= 10 else random.randint(1, 11)
        return func(num, count)

    return three


@one
def two(num, count):
    print(f'Загадано число {num}, нужно угадать за {count} попыток.')
    for i in range(1, count + 1):
        print(f"Попытка номер {i} ")
        user_num = int(input("Введите число от 1 до 100: "))
        if user_num == num:
            return 'Молодец, число угадано!'
        elif user_num < num:
            print("Ваше число меньше\n", '-' * 100)
        else:
            print("Ваше число больше\n", '-' * 100)
    return 'Попыток больше нет!'


if __name__ == '__main__':
    print(two(10, 50))
