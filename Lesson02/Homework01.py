'''Напишите программу, которая получает целое
число и возвращает его шестнадцатеричное
строковое представление. Функцию hex
используйте для проверки своего результата.'''

import random


def Hex_transformation(num, mod=16):
    result = ''
    while num:
        temp = num % mod if (num % mod) < 10 else chr(num % mod + 87)
        result = str(temp) + result
        num //= 16
    return result


a: int = random.randint(1, 1001)
print(f'Задано число {a} \nРезультат преобразования в шестнадцатиричное: 0x{Hex_transformation(a)}')
print(f'Проверка преобразования в шестнадцатиричное: {hex(a)}')
