# Создайте функцию генератор чисел Фибоначчи (см. Википедию).


def fibonacci(xterms):
    '''генератор чисел Фибоначчи'''

    x1, x2 = 0, 1
    for i in range(xterms):
        xth = x1 + x2
        x1, x2 = x2, xth
        yield xth


num_quantity = int(input('Сколько чисел Фибоначчи вывести: '))
fib = fibonacci(num_quantity)

[print(f'{i + 1:>4}) {next(fib):>10}') for i in range(num_quantity)]
