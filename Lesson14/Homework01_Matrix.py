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
        """Метод проверяет равенство двух матриц."""
        if isinstance(other, Matrix):
            if self.height == other.height and self.length == other.length:
                result = []
                for i in range(self.length):
                    for j in range(self.height):
                        result.append(self.matrix[i][j] == other.matrix[i][j])
                return all(result)
        return False

    def __lt__(self, other):
        """Метод проверяет меньше ли первая матрица относительно второй."""
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
                return result

    def __mul__(self, other):
        """Метод возвращает результат умножения двух матриц."""
        if isinstance(other, Matrix):
            if self.height == other.length:
                result = [[sum(a * b for a, b in zip(self_row, other_col))
                           for other_col in zip(*other.matrix)]
                          for self_row in self.matrix]
            elif self.length == other.height:
                result = [[sum(a * b for a, b in zip(self_col, other_row))
                           for self_col in zip(*self.matrix)]
                          for other_row in other.matrix]
            return result
        return False

    def __str__(self):
        """Формируем удобный для клиента вывод матрицы"""
        return "\n".join(str(i) for i in self.matrix)


