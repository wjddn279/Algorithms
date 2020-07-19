import sys
sys.stdin = open("let_miro_escape_17090.txt")

def prin(a):
    for i in range(len(a)):
        print(*a[i])
    print()

from _collections import deque

def iswall(x,y):
    if x < 0 or y < 0:
        return False
    elif x >= N or y >= M:
        return False
    else:
        return True

def bfs(x,y):
    cnt = 0
    step = []
    while iswall(x,y) and visited[x][y] == 0:
        visited[x][y] = 1
        step.append((x,y))
        nx = x + dx[matrix[x][y]]
        ny = y + dy[matrix[x][y]]
        x,y = nx,ny
        cnt += 1
    if not iswall(x,y):
        return cnt
    elif visited[x][y] == 1:
        # 처음이면
        if (x,y) in step:
            for i,j in step:
                visited[i][j] = -1
            return 0
        else:
            return cnt
    elif visited[x][y] == -1:
        for i, j in step:
            visited[i][j] = -1
        return 0

global N,M
N, M = map(int,input().split())
matrix = [list(input()) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
# U : (-1,0) R : (0,1) D : (1,0) L : (0,-1)
dx = [-1,0,1,0]
dy = [0,1,0,-1]

for i in range(N):
    for j in range(M):
        var = matrix[i][j]
        if var =='U':
            matrix[i][j] = 0
        elif var =='R':
            matrix[i][j] = 1
        elif var =='D':
            matrix[i][j] = 2
        else:
            matrix[i][j] = 3
prin(matrix)
result = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            result += bfs(i,j)
print(result)
