'''Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение дробей.
Для проверки своего кода используйте модуль fractions.'''
from fractions import Fraction


def sum(a, b):
    print(a, '+', b, '= ', end='')
    a = [int(i) for i in a.split('/')]
    b = [int(i) for i in b.split('/')]

    out_result(a[0] * b[1] + b[0] * a[1], a[1] * b[1])


def mult(a, b):
    print(a, '*', b, '= ', end='')
    a = [int(i) for i in a.split('/')]
    b = [int(i) for i in b.split('/')]

    out_result(a[0] * b[0], a[1] * b[1])


def out_result(a, b):
    coef = gcd(a, b)
    print(f'{int(a / coef)}/{int(b / coef)}')


def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


a = input('Введите первую дробь в формате "a/b": ')
b = input('Введите вторую дробь в формате "a/b": ')

summa(a, b)
mult(a, b)
# Проверка
print('-' * 100, '\nЭто проверка модулем Fraction, заданы две дроби: ', a, b)
a = Fraction(a)
b = Fraction(b)
print(f'{a} + {b} = {a + b}\n{a} * {b} = {a * b}')
