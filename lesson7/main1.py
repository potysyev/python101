class Matrix:
    def __init__(self, matrix):
        j = []
        self.matrix_data = matrix
        self.row = len(matrix)
        for i in range(self.row):
            j.append(len(matrix[i]))
        if len(set(j)) > 1:
            raise RuntimeError("Column size is not constant")
        self.col = len(j)

    def __str__(self):
        output = ""
        for i in range(self.row):
            output = output + ('| ' + ' '.join([str(j) for j in self.matrix_data[i]]) + ' |\n')
        return output

    def __add__(self, other):
        result = self.matrix_data
        for i in range(self.row):
            for j in range(self.col):
                result[i][j] = self.matrix_data[i][j] + other.matrix_data[i][j]
        return Matrix(result)


matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[11, 22, 33], [44, 55, 66], [77, 88, 99]]

m1 = Matrix(matrix1)
m2 = Matrix(matrix2)
print(m1 + m2)
