# Доработаем прямоугольник и добавим экономию памяти для хранения свойств экземпляра без словаря __dict__.

class Rectangle:
    __slots__ = ('width', 'higth')

    def __init__(self, hight=None, width=None):
        """Инициализация парамтров прямоугольника- высота и ширина."""
        self._higth = hight
        self._width = width if width else hight

    @property
    def width(self):
        return self._width

    @property
    def higth(self):
        return self._higth

    @higth.setter
    def higth(self, val):
        if val <= 0:
            raise ValueError('Не может быть отрицательным значением!')
        self._higth = val

    @width.setter
    def width(self, val):
        if val <= 0:
            raise ValueError('Не может быть отрицательным значением!')
        self._width = val

    def perimeter(self):
        """Функция возвращает периметр прямоугольника."""
        return (self._higth + self._width) * 2

    def square(self):
        """Функция возвращает площадь прямоугольника."""
        return self.higth * self.width

    def __add__(self, other):
        """Сложение прямоугольников"""
        new_perimetr = self.perimeter() + other.perimeter()
        hight = self.higth + other.higth
        width = new_perimetr / 2 - hight
        return Rectangle(hight, width)

    def __sub__(self, other):
        """Вычитание прямоугольников."""
        perimetr = abs(self.perimeter() - other.perimeter())
        hight = abs(self.higth + other.higth)
        width = abs(perimetr / 2 - hight)
        return Rectangle(hight, width)

    def __str__(self):
        """Формируем удобный для клиента вывод информации об экземпляре класса."""
        return f'Прямоугольник со сторонами {self.higth} и {self.width}, его периметр равен {self.perimeter()}, его площадь равна {self.square()}.'


if __name__ == '__main__':
    r1 = Rectangle(2, 3)
    r2 = Rectangle(2)
    print('Первый : ', r1)
    print('Второй : ', r2)

    print('Сумма прямоугольников : ', r1 + r2)
    print('Разность прямоугольников : ', r1 - r2)
    print('Разность прямоугольников : ', r2 - r1)
    r1.width = 4
    r1.higth = 8
    print(r1)
