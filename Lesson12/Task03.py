# Создайте класс-генератор.
# Экземпляр класса должен генерировать факториал числа в диапазоне от start до stop с шагом step.
#   -Если переданы два параметра, считаем step=1.
#   -Если передан один параметр, также считаем start=1.
from math import factorial


class FactGenerator:
    def __init__(self, *args):
        self.start, self.stop, self.step = 1, 1, 1
        match args:
            case (stop, ):
                self.stop = stop
            case (start, stop):
                self.start, self.stop = start, stop
            case (start, stop, step):
                self.start, self.stop, self.step = start, stop, step
            case _:
                raise AttributeError('None attribute!')
        self.data_list = [*range(self.start, self.stop + 1, self.step)]

    def __iter__(self):
        return self

    def __next__(self):
        if self.data_list:
            return factorial(self.data_list.pop(0))
        raise StopIteration


if __name__ == '__main__':
    [print(i, end=' ') for i in FactGenerator(5, 16, 2)]
    print()
    [print(i, end=' ') for i in FactGenerator(6, 16)]
    print()
    [print(i, end=' ') for i in FactGenerator(16)]
