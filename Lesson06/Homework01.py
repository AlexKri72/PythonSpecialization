# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

from sys import argv
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


# добавляем возможность запуска в терминале с передачей даты на проверку
if __name__ == '__main__':
    (print('Дата корретная!') if calend(argv[1]) else print('Дата некорректная!'))
