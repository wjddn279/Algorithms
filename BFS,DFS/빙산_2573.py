# 10시 35분

import sys
sys.stdin = open("../input.txt")

def prin(a):
    for i in a:
        print(*i)
from _collections import deque

def iswall(x,y):
    if x < 0 or y < 0: return False
    elif x >= N or y >= M: return False
    else: return True

def search(i,j):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = 1
    step = []
    while queue:
        x,y = queue.popleft()
        temp = 0
        for k in range(4):
            nx,ny = x+dx[k],y+dy[k]
            if iswall(nx,ny):
                if matrix[nx][ny] == 0:
                    temp += 1
                elif matrix[nx][ny] and not visited[nx][ny]:
                    queue.append((nx,ny))
                    visited[nx][ny] = 1
        if matrix[x][y] - temp > 0:
            matrix[x][y] -= temp
        else:
            step.append((x,y))
    for x,y in step:
        matrix[x][y] = 0

def rotate():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and matrix[i][j]:
                cnt += 1
                search(i, j)
    return cnt
global N,M
N, M = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
time = -1
cnt = 1
while cnt == 1:
    time += 1
    visited = [[0 for _ in range(M)] for _ in range(N)]
    cnt = rotate()
if cnt == 0:
    print(0)
else:
    print(time)