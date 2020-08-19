import sys
sys.stdin = open("input.txt")

def prin(a):
    for i in a:
        print(*i)
    print()

from copy import deepcopy

def Check(i, j, m, matrix):
    for x in range(i, i + m):
        for y in range(j, j + m):
            if matrix[x][y] == 0:
                return False
    return True


def Make(i, j, m ,matrix):
    for x in range(i, i + m):
        for y in range(j, j + m):
            matrix[x][y] = 0

def Reverse(i, j, m ,matrix):
    for x in range(i, i + m):
        for y in range(j, j + m):
            matrix[x][y] = 1

def solve(matrix,frequency):
    prin(matrix)
    print(frequency)
    for i in range(10):
        for j in range(10):
            if matrix[i][j] == 1:
                if i < 5 and j < 5 and frequency[5] < 5:
                    if Check(i, j, 5 ,matrix):
                        Make(i, j, 5, matrix)
                        frequency[5] += 1
                        solve(deepcopy(matrix),frequency[:])
                        frequency[5] -= 1
                        Reverse(i, j, 5, matrix)

                if i < 6 and j < 6 and frequency[4] < 5:
                    if Check(i, j, 4, matrix):
                        Make(i, j, 4, matrix)
                        frequency[4] += 1
                        solve(deepcopy(matrix),frequency[:])
                        frequency[4] -= 1
                        Reverse(i, j, 4, matrix)

                if i < 7 and j < 7 and frequency[3] < 5:
                    if Check(i, j, 3, matrix):
                        Make(i, j, 3, matrix)
                        frequency[3] += 1
                        solve(deepcopy(matrix),frequency[:])
                        frequency[3] -= 1
                        Reverse(i, j, 3, matrix)

                if i < 8 and j < 8 and frequency[2] < 5:
                    if Check(i, j, 2, matrix):
                        Make(i, j, 2, matrix)
                        frequency[2] += 1
                        solve(deepcopy(matrix),frequency[:])
                        frequency[2] -= 1
                        Reverse(i, j, 2, matrix)

                if i < 9 and j < 9 and frequency[1] < 5:
                    if Check(i, j, 1, matrix):
                        Make(i, j, 1, matrix)
                        frequency[1] += 1
                        solve(deepcopy(matrix),frequency[:])
                        frequency[1] -= 1
                        Reverse(i, j, 1, matrix)
    print(frequency)

mat = [list(map(int,input().split())) for _ in range(10)]
freq = [0 for _ in range(6)]
result = [987654321]
solve(deepcopy(mat),freq[:])
print(result[0])