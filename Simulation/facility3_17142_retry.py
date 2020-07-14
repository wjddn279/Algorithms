import sys
sys.stdin = open("facility3_17142.txt")

def prin(a):
    for i in range(len(a)):
        print(*a[i])
    print()

from itertools import combinations
from _collections import deque

def iswall(x,y):
    if x < 0 or y < 0:
        return False
    elif x >= N or y >= N:
        return False
    elif mat[x][y] == '-':
        return False
    else:
        return True

def bfs(comb,resu,count):
    num = 0
    max_val = 0
    queue = deque(comb)
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for com in comb:
        mat[com[0]][com[1]] = 0
    while queue:
        x,y = queue.popleft()
        if num == count:
            break
        if visited[x][y] == resu:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if iswall(nx,ny):
                if mat[nx][ny] == -1 and visited[nx][ny] == 0:
                    queue.append((nx,ny))
                    visited[nx][ny] = visited[x][y]+1
                    max_val = max(max_val, visited[nx][ny])
                    num += 1
                elif mat[nx][ny] == '*' and visited[nx][ny] == 0:
                    queue.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1
    if num < count :
        return resu
    else:
        fl[0] = True
        return max_val

# N : N * N 행렬 , M : 3개의 바이러스를 활성화
global N
N,M = map(int,input().split())
mat = [list(map(int,input().split())) for _ in range(N)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
virus = []
count = 0
for i in range(N):
    for j in range(N):
        if mat[i][j] == 1:
            mat[i][j] = '-'
        if mat[i][j] == 2:
            mat[i][j] = '*'
            virus.append((i,j))
        if mat[i][j] == 0:
            mat[i][j] = -1
            count += 1
result = 987654321
fl = [False]
combs = list(combinations(virus, M))
for comb in combs:
    result = bfs(comb,result,count)
if fl[0]:
    print(result)
else:
    print(-1)



