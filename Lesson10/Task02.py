# Создайте класс прямоугольник.
# 📌 Класс должен принимать длину и ширину при создании экземпляра.
# 📌 У класса должно быть два метода, возвращающие периметр и площадь.
# 📌 Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.


class Rectangle:
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b if b else a

    def perimeter(self):
        return (self.a + self.b) * 2

    def square(self):
        return self.a * self.b


if __name__ == '__main__':
    r1 = Rectangle(2, 3)
    r2 = Rectangle(2)
    print(f'{r1.perimeter()= } , {r1.square()= }')
    print(f'{r2.perimeter()= } , {r2.square()= }')
