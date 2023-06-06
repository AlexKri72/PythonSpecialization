# Напишите для задачи 1 тесты pytest.
# Проверьте следующие варианты:
#   -возврат строки без изменений
#   -возврат строки с преобразованием регистра без потери символов
#   -возврат строки с удалением знаков пунктуации
#   -возврат строки с удалением букв других алфавитов
#   -возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
import pytest
from Task01 import checkstr

def test():
    assert checkstr('daily mail talks of the country becoming') == 'daily mail talks of the country becoming', 'Ошибка тест 1'
    assert checkstr(
        'DAILY MAIL Talks oF THE coUNtry beCOMing') == 'daily mail talks of the country becoming', 'Ошибка тест 2'
    assert checkstr(
        'daily "mail"; talks, of% the country becoming') == 'daily mail talks of the country becoming', 'Ошибка тест 3'
    assert checkstr(
        'daily maiлl taфиlks oмаf thАЗe coТИмuntry becoming') == 'daily mail talks of the country becoming', 'Ошибка тест 4'
    assert checkstr(
        'daily "mail"% t#al@ks of ?t*h\/Азe ;coтимuntry, becoming') == 'daily mail talks of the country becoming', 'Ошибка тест 5'


if __name__=='__main__':
    pytest.main([-v])