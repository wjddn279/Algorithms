import sys
sys.stdin = open("input.txt")

def prin(a):
    for i in a:
        print(i)
    print()

from _collections import deque

def iswall(x,y):
    if x < 0 or y < 0 : return False
    elif x >= N or y >= N : return False
    else : return True

def inner(x,y,cnt):
    queue = deque()
    queue.append((x,y))
    matrix[x][y] = cnt
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if iswall(nx,ny):
                if matrix[nx][ny] == 1:
                    queue.append((nx,ny))
                    matrix[nx][ny] = cnt
                if matrix[nx][ny] == 0:
                    visit[x][y] = 1

def setting():
    cnt = 2
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                inner(i,j,cnt)
                cnt += 1

def dis(ax,ay,answer):
    me = matrix[ax][ay]
    distance = float('inf')
    queue = deque()
    queue.append((ax,ay,1))
    visited[ax][ay] = 1
    while queue:
        x,y,cnt = queue.popleft()
        if cnt == answer:
            return cnt
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if iswall(nx,ny) and cnt<visited[nx][ny]:
                if matrix[nx][ny] == me:
                    queue.append((nx,ny,cnt))
                    visited[nx][ny] = cnt
                elif matrix[nx][ny] == 0:
                    queue.append((nx, ny, cnt+1))
                    visited[nx][ny] = cnt+1
                else:
                    distance = min(distance,visited[x][y])
                    visited[nx][ny] = cnt+1
    return distance-1

global N
N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
# 분리 집합
visit = [[0 for _ in range(N)] for _ in range(N)]
setting()
answer = float('inf')
queue = deque()
for i in range(N):
    for j in range(N):
        if visit[i][j]:
            queue.append((i,j))

