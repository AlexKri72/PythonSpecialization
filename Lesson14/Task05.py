# На семинарах по ООП был создан класс прямоугольник хранящий длину и ширину, а также вычисляющую периметр,
# площадь и позволяющий складывать и вычитать прямоугольники беря за основу периметр.
# Напишите 3-7 тестов unittest для данного класса.
from Task05_Rectangle import Rectangle

import unittest

class TestRectangle(unittest.TestCase):
    def test_1_square(self):
        self.assertEqual(Rectangle.square(Rectangle(2)),4)

    def test_2_perimeter(self):
        self.assertEqual(Rectangle.perimeter(Rectangle(2,3)),10)

    def test_3_sub(self):
        self.assertEqual(Rectangle(3,4)-Rectangle(2,3),Rectangle(1,1))

    def test_4_plus(self):
        self.assertEqual(Rectangle(3,4)+Rectangle(2,3),Rectangle(5,7))

if __name__=='__main__':
    unittest.main(verbosity=2)
