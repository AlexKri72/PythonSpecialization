# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой функции.
from typing import Callable


def one(count: int):
    def two(func: Callable):
        def three(*args, **kwargs):
            for i in range(1, count + 1):
                print(i, func(*args, **kwargs))

        return three

    return two


@one(6)
def func(txt: str):
    return txt.capitalize()


if __name__ == '__main__':
    func('Основная функция')
