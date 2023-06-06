# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним тесты.
# 2-5 тестов на задачу в трёх вариантах:
#   ○ doctest,
#   ○ unittest,
#   ○ pytest.

import unittest
from Homework01_Matrix import Matrix

matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[2, 3, 4], [5, 6, 7], [8, 9, 10]])
matrix_3 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

class TestMatrix(unittest.TestCase):
    def test(self):
        self.assertEqual(matrix_1 < matrix_2,True)
        self.assertEqual(matrix_1 > matrix_2,False)
        self.assertEqual(matrix_1 == matrix_3,True)
        self.assertEqual(matrix_1 == matrix_2,False)
        self.assertEqual(matrix_1 + matrix_2,[[3, 5, 7], [9, 11, 13], [15, 17, 19]])
        self.assertEqual(matrix_1 * matrix_2,[[36, 42, 48], [81, 96, 111], [126, 150, 174]])

if __name__=='__main__':
    unittest.main(verbosity=2)