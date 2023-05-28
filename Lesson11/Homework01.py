# Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.

# Создайте класс Матрица. Добавьте методы для:
#   ○ вывода на печать,
#   ○ сравнения,
#   ○ сложения,
#   ○ *умножения матриц
class Matrix:
    """Создаем класс Матрица с методами работы с матрицами."""

    def __init__(self, matrix: list[list]):
        """Инициализируем парметры матрицы - данные, ширину и высоту."""
        self.matrix = matrix
        self.height = len(matrix)
        self.length = len(matrix[0])

    def __eq__(self, other):
        if isinstance(other, Matrix):
            if self.height == other.height and self.length == other.length:
                result = []
                for i in range(self.length):
                    for j in range(self.height):
                        result.append(self.matrix[i][j] == other.matrix[i][j])
                return all(result)
        return False

    def __lt__(self, other):
        if isinstance(other, Matrix):
            if self.height == other.height and self.length == other.length:
                result = []
                for i in range(self.length):
                    for j in range(self.height):
                        result.append(self.matrix[i][j] < other.matrix[i][j])
                return all(result)
        return False

    def __add__(self, other):
        """Метод возвращает результат сложения двух матриц."""
        if isinstance(other, Matrix):
            if self.height == other.height and self.length == other.length:
                result = [[] for i in range(self.length)]
                for i in range(self.length):
                    for j in range(self.height):
                        result[i].append(self.matrix[i][j] + other.matrix[i][j])
                return Matrix(result)

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.height == other.length:
                result = [[sum(a * b for a, b in zip(self_row, other_col))
                           for other_col in zip(*other.matrix)]
                          for self_row in self.matrix]
            elif self.length == other.height:
                result = [[sum(a * b for a, b in zip(self_col, other_row))
                           for self_col in zip(*self.matrix)]
                          for other_row in other.matrix]
            return Matrix(result)
        return False

    def __str__(self):
        """Формируем удобный для клиента вывод матрицы"""
        return "\n".join(str(i) for i in self.matrix)


if __name__ == '__main__':
    matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    matrix_2 = Matrix([[2, 3, 4], [5, 6, 7], [8, 9, 10]])
    matrix_3 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(matrix_1, matrix_2, sep='\n\n')
    print('matrix1 == matrix2 : ', matrix_1 == matrix_2)
    print('matrix1 == matrix3 : ', matrix_1 == matrix_3)
    print('matrix1 < matrix2 : ', matrix_1 < matrix_2)
    print('matrix1 > matrix 2 : ', matrix_1 > matrix_2)
    add_matrix = matrix_1 + matrix_2
    print('Сумма матриц: \n', add_matrix)
    mul_matrix = matrix_1 * matrix_2
    print('Произведение матриц: \n', mul_matrix)
