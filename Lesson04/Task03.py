# Функция получает на вход строку из двух чисел через пробел.
# Сформируйте словарь, где ключом будет символ из Unicode, а значением — целое число.
# Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно.
def dict1(txt):
    """Формируем словарь символов по возрастаниию"""

    minimum, maximum = sorted([int(i) for i in txt.split()])
    return {chr(i): i for i in range(minimum, maximum + 1)}


print(dict1('14 13'))
