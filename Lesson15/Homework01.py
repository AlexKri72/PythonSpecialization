# Возьмите любые 1-3 задачи из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной информации.
# Также реализуйте возможность запуска из командной строки с передачей параметров.
from Homework01_Rectangle import Rectangle
import argparse


if __name__ == '__main__':
    print('Первый : ', Rectangle(2, 3))
    print('Второй : ', Rectangle(2))
    print('Третий : ', Rectangle('a2', 3)) #Homework01_exception.UserTypeStrError: Значение a2 должно быть числом!
    # print('Четвертый : ', Rectangle(-2)) #Homework01_exception.UserValueError: Значение -2 должно быть больше нуля!

    parser= argparse.ArgumentParser(description='Получаем строку с данными')
    parser.add_argument('-higth',type=int, default=None)
    parser.add_argument('-width',type=int, default=None)
    args=parser.parse_args()

    # Для запуска из командной строки:
    # python ./Lesson15/Homework01.py -higth=5 -width=6 # Прямоугольник со сторонами 5 и 6, его периметр равен 22, его площадь равна 30.
    # print(Rectangle(args.higth,args.width))


