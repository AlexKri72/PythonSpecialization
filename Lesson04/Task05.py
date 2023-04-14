# Функция принимает на вход три списка одинаковой длины:
#   имена str,
#   ставка int,
#   премия str с указанием процентов вида «10.25%».
# Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии.
from pprint import pprint


def premia(names, cash, percent):
    """Рассчитываем сумму премии."""

    return {name: money / 100 * perc for name, money, perc in zip(names, cash, (float(i[:-1]) for i in percent))}


lst1 = ['Alex', 'Alexandr', 'Alexey', 'Sasha']
lst2 = [55_000, 48_000, 64_000, 86_000]
lst3 = ['10.25%', '9.86%', '12.64%', '36.86%']

pprint(premia(lst1, lst2, lst3))
