import sys
sys.stdin = open("input.txt")

def prin(a):
    for i in a:
        print(i)
    print()

from _collections import deque

def iswall(x,y):
    if x < 0 or y < 0 : return False
    elif x >= N or y >= M : return False
    elif matrix[x][y] != '.' : return False
    else: return True

def search():
    q,ji = deque(),deque()
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 'J':
                matrix[i][j] = '.'
                ji.append((i,j))
            if matrix[i][j] == 'F':
                q.append((i,j))
    return q,ji

def move_fire():
    next = deque()
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if iswall(nx,ny):
                next.append((nx,ny))
                visited[nx][ny] = 1
                matrix[nx][ny] = 'F'
    return next

def move_jihoon():
    jihoon = deque()
    while ji:
        x,y = ji.popleft()
        if x == N - 1 or y == M - 1 or x == 0 or y == 0:
            return True, 0
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if iswall(nx,ny) and not visited[nx][ny]:
                jihoon.append((nx,ny))
                visited[nx][ny] = 1
    return False,jihoon

global N,M
N, M = map(int,input().split())
matrix = [list(input()) for _ in range(N)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
queue,ji = search()
visited = [[0 for _ in range(M)] for _ in range(N)]
cnt = 0
Flag = False
while ji:
    cnt += 1
    queue = move_fire()
    Flag, ji = move_jihoon()
    if Flag:
        print(cnt)
if not Flag:
    print('IMPOSSIBLE')
