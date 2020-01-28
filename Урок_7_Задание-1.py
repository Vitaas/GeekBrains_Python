'''Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы. Подсказка: матрица —
система некоторых математических величин, расположенных в виде прямоугольной схемы. Примеры матриц вы найдете
в методичке. Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса
Matrix (двух матриц). Результатом сложения должна быть новая матрица. Подсказка: сложение элементов матриц
выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой
строки второй матрицы и т.д.'''

class Matrix:
    def __init__(self, matrix_1, matrix_2):
        self.matrix = [matrix_1, matrix_2]

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, list)) for list in self.matrix])

    def __add__(self, other):
        for i in range(len(self.matrix_1)):
            for j in range(len(self.matrix_2[0])):
                return Matrix(self.matrix_1[i][j] + other.matrix_1[i][j], self.matrix_2[i][j] + other.matrix_2[i][j])

my_matrix = Matrix([1, 2, 3], [1, 1, 1])
print(my_matrix)

