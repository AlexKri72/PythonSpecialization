'''Напишите программу, которая получает целое
число и возвращает его шестнадцатеричное
строковое представление. Функцию hex
используйте для проверки своего результата.'''

import random


def Hex_transformation(num):
    dict = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    result = ''
    while num:
        temp = num % 16
        if 10 <= temp:
            result = dict[temp] + result
        else:
            result = str(temp) + result
        num //= 16
    return result


a: int = random.randint(1, 1001)
print(f'Задано число {a} \nРезультат преобразования в шестнадцатиричное: 0x{Hex_transformation(a)}')
print(f'Проверка преобразования в шестнадцатиричное: {hex(a)}')
