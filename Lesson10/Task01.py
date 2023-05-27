# Создайте класс окружность.
# 📌 Класс должен принимать радиус окружности при создании экземпляра.
# 📌 У класса должно быть два метода, возвращающие длину окружности и её площадь.
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def CircumferenceLength(self):
        return self.radius * 2 * math.pi

    def Square(self):
        return math.pi * self.radius ** 2


if __name__ == '__main__':
    c1 = Circle(2)
    c2 = Circle(6)
    print(f'{c1.CircumferenceLength()= :f} , {c1.Square()= :f}')
    print(f'{c2.CircumferenceLength()= :f} , {c2.Square()= :f}')
