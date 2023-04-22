# Улучшаем задачу 2.
# Добавьте возможность запуска функции «угадайки» из модуля в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.


from random import randint

__all__ = ['game']


def game(min_limit=0, max_limit=1000, count=8):
    '''Угадываем число'''

    print(f'Угадайте число в диапазоне от {min_limit} до {max_limit}.')
    num = randint(min_limit, max_limit + 1)
    search_num = None
    while search_num != num:
        search_num = int(input(f"Угадайте число, у Вас {count} попыток: "))
        print([["Загаданное число меньше", "Загаданное число больше"][search_num < num], "Угадали!"][search_num == num])
        count -= 1
        if count == 0:
            print("Увы, попыток больше нет!")
            return False
    return True
