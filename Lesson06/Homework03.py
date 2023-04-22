# Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

from random import shuffle


def random_state():
    '''Формируем случайную расстановку ферзей'''

    x = list(range(1, 9))
    shuffle(x)
    return x


def queen(quantity):
    '''Подбираем расстановки ферзей.'''

    n = 8
    count = 0
    result = []
    while count < quantity:
        x = random_state()
        y = random_state()
        for i in range(n):
            for j in range(i + 1, n):
                if [i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                    continue
        result.append([tuple(i) for i in zip(x, y)])
        count += 1

    return result


print('\nПолучаем следующие  расстановки ферзей: \n', '-' * 50)
[print(i) for i in queen(4)]
