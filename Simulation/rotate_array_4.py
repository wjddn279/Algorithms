import sys
sys.stdin = open("rotate_array_4.txt")
def prin(a):
    for i in range(len(a)):
        print(*a[i])
    print()

from itertools import permutations
from copy import deepcopy

def rotation(r,c,s):
    # 위칸:
    while s > 0:
        temp = matrix[r-s][c-s]
        for i in range(c-s+1,c+s+1):
            tem = matrix[r-s][i]
            matrix[r-s][i] = temp
            temp = tem
        # 오른쪽
        for i in range(r-s+1,r+s+1):
            tem = matrix[i][c+s]
            matrix[i][c+s] = temp
            temp = tem
        # 밑
        for i in range(c+s-1,c-s-1,-1):
            tem = matrix[r+s][i]
            matrix[r+s][i] = temp
            temp = tem

        # 왼쪽
        for i in range(r+s-1,r-s-1,-1):
            tem = matrix[i][c-s]
            matrix[i][c-s] = temp
            temp = tem

        s -= 1

def check_sum():
    result = 987654321
    for i in range(N):
        result = min(result,sum(matrix[i]))
    return result

global N
N, M, K = map(int,input().split())
mat = [list(map(int,input().split())) for _ in range(N)]
rotate = [list(map(int,input().split())) for _ in range(K)]
per_rotate = list(permutations(rotate,K))
result = 987654321
for rotate in per_rotate:
    matrix = deepcopy(mat)
    for r,c,s in rotate:
        rotation(r-1,c-1,s)
    result = min(result,check_sum())
print(result)
# 가장 왼쪽 윗칸이 (r-s,c-s) 오른쪽 아랫칸이 (r+s,c+s)
