import sys
from _collections import deque
import itertools
sys.stdin = open("input11.txt")

def wall(x,y):
    if x < 0 or y < 0:
        return False
    elif x >= len(matrix) or y >= len(matrix[0]):
        return False
    elif matrix[x][y] == '@':
        return False
    else:
        return True

def search():
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'D':
                dao = (i,j)
    return dao

def convert(a):
    if a == 'A':
        return (0,-1)
    elif a == 'D':
        return (0,1)
    elif a == 'W':
        return (-1,0)
    else:
        return (1,0)

def powerset(n,k,x,y):
    if k == n+1 or len(result) != 0:
        return 0
    elif k != 0 :
        dx, dy = convert(moving[k-1][subset[k-1]])
        nx, ny = x + dx, y + dy
        if wall(nx, ny):
            if matrix[nx][ny] == 'Z':
                result.append(subset[0:k])
                return 0
            else:
                x, y = nx, ny
        else:
            return 0
        if k < n+1:
            subset[k] = 1
            powerset(n,k+1,x,y)
            subset[k] = 0
            powerset(n,k+1,x,y)
    else:
        subset[k] = 1
        powerset(n,k+1,a,b)
        subset[k] = 0
        powerset(n,k+1,a,b)

H,W = map(int,input().split())
matrix = [list(input()) for _ in range(H)]
length = int(input())
moving = [list(input().split()) for _ in range(length)]
subset = [0 for _ in range(len(moving)+1)]
a,b = search()
result = []
powerset(len(moving),0,a,b)
per = ''
if len(result) == 0:
    print('NO')
else:
    print('YES')
    for i in result:
        for j in range(len(i)):
            per += moving[j][i[j]]
    print(per)

