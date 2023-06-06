# Напишите для задачи 1 тесты doctest.
# Проверьте следующие варианты:
#   -возврат строки без изменений
#   -возврат строки с преобразованием регистра без потери символов
#   -возврат строки с удалением знаков пунктуации
#   -возврат строки с удалением букв других алфавитов
#   -возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

import re


def checkstr(text: str):
    """
    Удаляет из текста все символы, кроме пробелов и букв латинского алфавита.
    >>> checkstr('daily mail talks of the country becoming')
    'daily mail talks of the country becoming'
    >>> checkstr('DAILY MAIL Talks oF THE coUNtry beCOMing')
    'daily mail talks of the country becoming'
    >>> checkstr('daily "mail"; talks, of% the country becoming')
    'daily mail talks of the country becoming'
    >>> checkstr('daily maiлl taфиlks oмаf thАЗe coТИмuntry becoming')
    'daily mail talks of the country becoming'
    >>> checkstr('daily "mail"% t#al@ks of ?t*h\/Азe ;coтимuntry, becoming')
    'daily mail talks of the country becoming'
    """

    regex = re.compile('[^a-zA-Z ]')

    return regex.sub('', text).lower()


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
