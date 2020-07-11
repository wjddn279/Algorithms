import sys
sys.stdin = open("junan.txt")

def prin(a):
    for i in range(len(a)):
        print(*a[i])
    print()

from _collections import deque

def wall(x,y):
    if x < 0 or y < 0:
        return False
    elif x >= N or y >= M:
        return False
    else:
        return True

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[x][y] = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if wall(nx,ny):
                if visited[nx][ny] == 0:
                    if matrix[nx][ny] == '1':
                        matrix[nx][ny] = '0'
                        visited[nx][ny] = 1
                    elif matrix[nx][ny] == '#':
                        return False
                    elif matrix[nx][ny] == '0':
                        queue.append((nx,ny))
                        visited[nx][ny] = 1
    return True

global N,M
N, M = map(int,input().split())
x_start,y_start,x_end,y_end = map(int,input().split())
matrix = [list(input()) for _ in range(N)]
# x_start, y_start : 주난 위치, # x_end, y_end : 범인 위치
dx = [0,0,-1,1]
dy = [1,-1,0,0]
flag = True
result = 0
while flag:
    flag = bfs(x_start-1,y_start-1)
    result += 1
print(result)