# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.


def queen():
    n = 8
    x = []
    y = []
    print('Введите 8 строк (координаты ферзей), в каждой строке 2 координаты, разделенных пробелом. ')
    print('Одна координата - одна цифра от 1 до 8 :')
    for i in range(n):
        new_x, new_y = [int(s) for s in input().split()]
        x.append(new_x)
        y.append(new_y)

    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                return False
    return True


(print('Верная расстановка!') if queen() else print('Ферзи бьют друг друга!'))
