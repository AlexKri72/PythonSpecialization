# Доработайте прошлую задачу добавив декоратор "wraps" в каждый из декораторов.


import random
import json
from functools import wraps


def multy_start(count):
    '''Декоратор. Запускает игру несколько раз.'''

    def one(func):
        cache = []

        @wraps(func)
        def two(*args, **kwargs):
            for _ in range(count):
                cache.append(func(*args, **kwargs))
            return cache

        return two

    return one


def safe_parameters_to_json(func):
    '''Декоратор. Записывает входные параметры и результат игры в файл.'''

    @wraps(func)
    def two(*args, **kwargs):
        file_name = f'{__file__[:-3]}.json'  # называем json файл также, как и основной
        result = func(*args)
        my_dict = {}
        my_dict['arguments'] = [[*args]]
        my_dict['result'] = [result]
        for key, value in kwargs.items():
            my_dict[key] = value
        with open(file_name, 'a', encoding='utf-8') as f:
            json.dump(my_dict, open(file_name, 'a', encoding='utf-8'), indent=2, ensure_ascii=False)
        return result

    return two


def control_parameters(func):
    '''Декоратор. Проверяет входные параметры на валидность.'''

    @wraps(func)
    def wrapper(num: int, count: int):
        num = num if 1 <= num <= 100 else random.randint(1, 100)
        count = count if 1 <= count <= 10 else random.randint(1, 10)
        return func(num, count)

    return wrapper


@multy_start(random.randint(1, 6))
@control_parameters
@safe_parameters_to_json
def game(num: int, count: int):
    '''Игра-угадайка. Нужно за определенное количество попыток угадать загаданное число.'''

    print(f'Загадано число {num}, нужно угадать за {count} попыток.')
    for i in range(1, count + 1):
        print(f"Попытка номер {i} ")
        user_num = int(input("Введите число от 1 до 100:  "))
        if user_num == num:
            print("Молодец, угадал!")
            return 'Вы выиграли!'
        elif user_num < num:
            print("Ваше число меньше")
        else:
            print("Ваше число больше")
        return 'Вы проиграли!'


if __name__ == '__main__':
    game(random.randint(-200, 201), random.randint(-20, 21))
