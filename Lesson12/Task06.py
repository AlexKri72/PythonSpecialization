# Изменяем класс прямоугольника.
# Заменяем пару декораторов проверяющих длину и ширину на дескриптор с валидацией размера.


class Valid:

    def __init__(self, min_value: float = None, max_value: float = None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param, value)

    def validate(self, value):
        if value is not None and value < self.min_value:
            raise ValueError(f'Bad lower level - {value}')
        if value is not None and value > self.max_value:
            raise ValueError(f'Bad upper level - {value}')


class Rectangle:
    _width = Valid(1, 100)
    _higth = Valid(1, 200)

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
    r3 = Rectangle(-3, 300)
    print(r3)
