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
    else: return True

def sol(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = [0,0]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if iswall(nx,ny):
                temp = visited[x][y][:]
                if matrix[nx][ny] == 'n':
                        temp[1] += 1
                elif matrix[nx][ny] == 'g':
                        temp[0] += 1
                if visited[nx][ny][0] > temp[0] or (visited[nx][ny][0] == temp[0] and visited[nx][ny][1] > temp[1]):
                    queue.append((nx, ny))
                    visited[nx][ny] = temp

global N,M
N, M = map(int,input().split())
matrix = [list(input()) for _ in range(N)]
visited = [[[float('inf'),float('inf')] for _ in range(M)] for _ in range(N)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
for x in range(N):
    for y in range(M):
        if matrix[x][y] == 'g':
            for i in range(4):
                nx,ny = x+dx[i],y+dy[i]
                if iswall(nx,ny) and matrix[nx][ny] != 'F' and matrix[nx][ny] != 'S' and matrix[nx][ny] != 'g':
                    matrix[nx][ny] = 'n'
        elif matrix[x][y] == 'S':
            start = (x,y)
        elif matrix[x][y] == 'F':
            end = (x,y)
sol(start[0],start[1])
print(*visited[end[0]][end[1]])
