# Функция получает на вход список чисел и два индекса.
# Вернуть сумму чисел между между переданными индексами.
# Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.
def list_sum(numbers, index_1, index_2):
    """Суммируем элементы списка от Индекс_1 до Индекс_2"""

    index_1 = index_1 if index_1 >= 0 else 0
    index_2 = index_2 if index_2 <= len(numbers) else len(numbers)
    result = 0
    for i in numbers[index_1:index_2 + 1]:
        result += i
    return result


print(list_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], -1, 2))
