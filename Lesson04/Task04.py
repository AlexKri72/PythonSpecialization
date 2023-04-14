# Функция получает на вход список чисел.
# Отсортируйте его элементы in place без использования встроенных в язык сортировок.
# Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.
def bubble_sort(numbers):
    """Пузырьковая сортировка списка чисел"""

    length = len(numbers)
    for _ in range(length):
        for j in range(length - 1):
            if numbers[j + 1] < numbers[j]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


print('Result: ', bubble_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]))
