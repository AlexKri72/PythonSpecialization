# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним тесты.
# 2-5 тестов на задачу в трёх вариантах:
#   ○ doctest,
#   ○ unittest,
#   ○ pytest.

import pytest
from Homework01_Matrix import Matrix


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[2, 3, 4], [5, 6, 7], [8, 9, 10]])
matrix_3 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

def test_matrix():
    assert matrix_1 < matrix_2 ,'Ошибка в тесте 1'
    assert not matrix_1 > matrix_2 ,'Ошибка в тесте 2'
    assert matrix_1 == matrix_3 ,'Ошибка в тесте 3'
    assert matrix_1 + matrix_2 == [[3, 5, 7], [9, 11, 13], [15, 17, 19]] ,'Ошибка в тесте 4'
    assert matrix_1 * matrix_2 == [[36, 42, 48], [81, 96, 111], [126, 150, 174]] ,'Ошибка в тесте 5'

if __name__=='__main__':
    pytest.main([-v])