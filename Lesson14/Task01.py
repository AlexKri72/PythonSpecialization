# Создайте функцию, которая удаляет из текста все символы кроме букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре.

import re


def checkstr(text: str):
    """Удаляет из текста все символы, кроме пробелов и букв латинского алфавита."""

    regex = re.compile('[^a-zA-Z ]')

    return regex.sub('', text).lower()


if __name__ == '__main__':
    print(checkstr('Daily0 1Mai%l tal"ks o&f t$*he cou@ntry bфиecoming'))
