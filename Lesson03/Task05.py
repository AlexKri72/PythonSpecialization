#   Создайте вручную список с повторяющимися целыми числами.
#   Сформируйте список с порядковыми номерами нечётных элементов исходного списка.
#   Нумерация начинается с единицы.
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 12, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list1)
print([i + 1 for i in range(len(list1)) if list1[i] % 2 != 0])
