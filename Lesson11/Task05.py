# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.


class Rectangle:
    def __init__(self, hight=None, width=None):
        """Инициализация парамтров прямоугольника- высота и ширина."""
        self.hight = hight
        self.width = width if width else hight

    def perimeter(self):
        """Функция возвращает периметр прямоугольника."""
        return (self.hight + self.width) * 2

    def square(self):
        """Функция возвращает площадь прямоугольника."""
        return self.hight * self.width

    def __add__(self, other):
        """Сложение прямоугольников"""
        new_perimetr = self.perimeter() + other.perimeter()
        hight = self.hight + other.hight
        width = new_perimetr / 2 - hight
        return Rectangle(hight, width)

    def __sub__(self, other):
        """Вычитание прямоугольников."""
        perimetr = abs(self.perimeter() - other.perimeter())
        hight = abs(self.hight + other.hight)
        width = abs(perimetr / 2 - hight)
        return Rectangle(hight, width)

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
