def prin(a):
    for i in a:
        print(*i)
    print()

def rotate():
    new_matrix = [[0] * len(matrix) for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            new_matrix[len(matrix)-j-1][i] = matrix[i][j]
    return new_matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
prin(matrix)
matrix = rotate()
prin(matrix)