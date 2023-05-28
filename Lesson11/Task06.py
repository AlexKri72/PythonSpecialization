# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения

class Rectangle:
    def __init__(self, hight=None, width=None):
        """Инициализация параметров прямоугольника - высота и ширина."""
        self.hight = hight
        self.width = width if width else hight

    def perimeter(self):
        """Метод возвращает результат вычисления периметра прямоугольника."""
        return (self.hight + self.width) * 2

    def square(self):
        """Метод возвращает результат вычисления площади прямоугольника."""
        return self.hight * self.width

    def __add__(self, other):
        """Складывает два прямоугольника и возвращает результат в виде третьего."""
        new_perimetr = self.perimeter() + other.perimeter()
        hight = self.hight + other.hight
        width = new_perimetr / 2 - hight
        return Rectangle(hight, width)

    def __sub__(self, other):
        """Вычитает два прямоугольника и возвращает результат  в виде третьего."""
        perimetr = abs(self.perimeter() - other.perimeter())
        hight = abs(self.hight + other.hight)
        width = abs(perimetr / 2 - hight)
        return Rectangle(hight, width)

    def __eq__(self, other):
        """Сравнивает два прямоугольника на равенство."""
        return self.square() == other.square()

    def __lt__(self, other):
        """Сравнивает меньше ли первый прямоугольник второго."""
        return self.square() < other.square()

    def __ge__(self, other):
        """Сравнивает меньше ли первый прямоугольник второго или равен ему."""
        return self.square() <= other.square()

    def __str__(self):
        """Формируем удобный для клиента вывод информации об экземпляре класса."""
        return f'Прямоугольник со сторонами {self.hight} и {self.width}, его периметр равен {self.perimeter()}, его площадь равна {self.square()}.'


if __name__ == '__main__':
    r1 = Rectangle(2, 3)
    r2 = Rectangle(2)
    print('Первый : ', r1)
    print('Второй : ', r2)

    print('Сумма прямоугольников : ', r1 + r2)
    print('Разность прямоугольников : ', r1 - r2)
    print('Разность прямоугольников : ', r2 - r1)

    # Все шесть операций сравнения:
    print(f'r1 == r2 : {r1 == r2}')
    print(f'r1 != r2 : {r1 != r2}')
    print(f'r1 < r2 : {r1 < r2}')
    print(f'r1 > r2 : {r1 > r2}')
    print(f'r1 <= r2 : {r1 <= r2}')
    print(f'r1 >= r2 : {r1 >= r2}')
