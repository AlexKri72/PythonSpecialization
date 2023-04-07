# Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру.
# Диаметр не превышает 1000 у.е.
# Точность вычислений должна составлять не менее 42 знаков после запятой.
import decimal, random, math

decimal.getcontext().prec = 42

d = decimal.Decimal(random.uniform(1, 1001))
print('Задан диаметр: ', d, 'единиц.')
print(
    f'Площадь круга: {decimal.Decimal(math.pi) * ((d / 2) ** 2)} единиц\nДлина окружности: {decimal.Decimal(math.pi) * d} единиц')
