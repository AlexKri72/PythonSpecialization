import logging
from Homework01_exception import UserValueError,UserTypeStrError

class Rectangle:
    logging.basicConfig(
        filename='Homework01.log',
        filemode='w',
        encoding='utf-8',
        format='{asctime} {levelname:<8} функция "{funcName}()" строка {lineno:>3d} : {msg}',
        style='{',
        level=logging.INFO)
    global logger
    logger = logging.getLogger(__name__)


    def __init__(self, hight=None, width=None):
        """Инициализация параметров прямоугольника - высота и ширина."""

        logger.info(f'Для инициализации передан прямоугольник с параметрами: higth = {hight} , width = {width}.')
        if isinstance(hight, int | float):
            if 0 < hight:
                self.hight = hight
            else:
                logger.error(f'Параметр "{hight}" должен быть больше нуля!')
                raise UserValueError(hight)
        else:
            logger.error(f'Параметр "{hight}" должен быть числом!')
            raise UserTypeStrError(hight)
        if not width:
            self.width = hight
        else:
            if isinstance(width, int | float):
                if 0 < width:
                    self.width = width
                else:
                    logger.error(f'Параметр "{width}" должен быть больше нуля!')
                    raise UserValueError(width)
            else:
                logger.error(f'Параметр "{width}" должен быть числом!')
                raise UserTypeStrError(width)

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
    print('Первый : ', Rectangle(2, 3))
    print('Второй : ', Rectangle(2))
    # print('Третий : ', Rectangle('a2', 3)) #Homework01_exception.UserTypeStrError: Значение a2 должно быть числом!
    # print('Четвертый : ', Rectangle(-2)) #Homework01_exception.UserValueError: Значение -2 должно быть больше нуля!
