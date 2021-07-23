class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix])

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or \
                False in [len(self.matrix[i]) == len(other.matrix[i]) for i in range(len(self.matrix))]:
            raise Exception('To add 2 matrix, they both must have the same amount of rows and columns')
        return [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix))]
                for i in range(len(self.matrix))]


m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = Matrix([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]])

print(f'Первая матрица\n{m1}\n\nВторая матрица\n{m2}\n\nРезультат суммирования матриц\n{m1 + m2}')
