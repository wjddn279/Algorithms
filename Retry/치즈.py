import sys
sys.stdin = open("input.txt")

def prin(a):
    for i in a:
        print(i)
    print()

from _collections import deque

def iswall(x,y):
    if x < 0 or y < 0 : return False
    elif x >= N or y >= M: return False
    else: return True

def start(x,y):
    next = []
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if iswall(nx,ny):
                if matrix[nx][ny]:
                    touch[nx][ny] -= 1
                    if touch[nx][ny] == 2:
                        next.append((nx,ny))
                        matrix[nx][ny] = 0
                elif not visited[nx][ny]:
                    queue.append((nx,ny))
                    visited[nx][ny] = 1
    return next

def goday(queue):
    queue = deque(queue)
    next = []
    while queue:
        x,y = queue.popleft()
        matrix[x][y] = 0
        visited[x][y] = 1
        temp = start(x,y)
        if temp:
            next += temp
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if iswall(nx,ny):
                if matrix[nx][ny]:
                    touch[nx][ny] -= 1
                    if touch[nx][ny] == 2:
                        next.append((nx,ny))
                        matrix[nx][ny] = 0
    return next

global N,M
N, M = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
touch = [[4 for _ in range(M)] for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
queue = start(0,0)
answer = 0
while True:
    print(queue)
    prin(visited)
    if queue:
        answer += 1
        queue = goday(queue)
    else:
        break
print(answer)