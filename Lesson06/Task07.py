# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY и возвращает истину,
# если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# И весь период действует григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

import calendar

__all__ = ['calend']


def calend(date: str) -> bool:
    """проверяем существование введенной даты"""

    try:
        day, month, year = map(int, date.split('.'))
    except ValueError:
        print('Неправильно введены данные!')
        return False
    if 1 <= year <= 9999:
        if month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31:
            return True
        elif month in [4, 6, 9, 11] and 1 <= day <= 30:
            return True
        elif month == 2 and 1 <= day <= 28 + _leap_year(year):
            return True
    else:
        return False


def _leap_year(year):
    """проверка года на високосность"""

    return calendar.isleap(year)
