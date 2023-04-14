# Напишите функцию для транспонирования матрицы

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def tranpose(matr):
    '''Траспонируем матрицу'''

    return [[matr[i][j] for i in range(len(matr))] for j in range(len(matr[0]))]


def print_matrix(m):
    '''Красиво печатаем матрицу'''

    [print(*i) for i in m]


print('Исходная матрица:')
print_matrix(matrix)

print('Транспонированная матрица:')
print_matrix(tranpose(matrix))
