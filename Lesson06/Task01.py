# Вспомните какие модули вы уже проходили на курсе.
# Создайте файл, в котором вы импортируете встроенные в модуль функции под псевдонимами.

import random as rnd
from time import sleep as sl
from sys import path as p
from decimal import Decimal as dc

print(rnd.randint(1, 100))
sl(1)
print(p)
print(dc(2))
