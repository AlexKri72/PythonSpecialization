# Напишите для задачи 1 тесты unittest.
# Проверьте следующие варианты:
#   -возврат строки без изменений
#   -возврат строки с преобразованием регистра без потери символов
#   -возврат строки с удалением знаков пунктуации
#   -возврат строки с удалением букв других алфавитов
#   -возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

from Task01 import checkstr
import unittest


class TestCaseName(unittest.TestCase):
    def test_metod(self):
        self.assertEqual(checkstr('daily mail talks of the country becoming'),
                         'daily mail talks of the country becoming')
        self.assertEqual(checkstr('DAILY MAIL Talks oF THE coUNtry beCOMing'),
                         'daily mail talks of the country becoming')
        self.assertEqual(checkstr('daily "mail"; talks, of% the country becoming'),
                         'daily mail talks of the country becoming')
        self.assertEqual(checkstr('daily maiлl taфиlks oмаf thАЗe coТИмuntry becoming'),
                         'daily mail talks of the country becoming')
        self.assertEqual(checkstr('daily "mail"% t#al@ks of ?t*h\/Азe ;coтимuntry, becoming'),
                         'daily mail talks of the country becoming')


if __name__ == '__main__':
    unittest.main(verbosity=2)
