# Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, который она возвращает.
# При повторном вызове файл должен расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой функции.
import json
import os.path
import random


def one(func):
    def two(*args, **kwargs):
        file_name = f'{func.__name__}.json'
        result = func(*args)
        with open(file_name, 'r', encoding='utf-8') as f:
            if 0 < os.path.getsize(file_name):
                my_dict = json.load(f)
                print(my_dict)
                my_dict['arguments'].append([*args])
                my_dict['result'].append(result)
                print(my_dict)
            else:
                my_dict = {}
                my_dict['arguments'] = [[*args]]
                my_dict['result'] = [result]

        for key, value in kwargs.items():
            my_dict[key] = value
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(my_dict, open(file_name, 'a', encoding='utf-8'), indent=2)
        return result

    return two


@one
def three(a, b):
    return a + b


if __name__ == '__main__':
    print(three(random.randint(1, 11), random.randint(1, 11)))
