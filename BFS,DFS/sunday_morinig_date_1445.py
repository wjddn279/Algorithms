import sys
sys.stdin = open("input.txt")
def prin(a):
    for i in a:
        print(*i)
    print()

from _collections import deque


def iswall(x,y):
    if x < 0 or y < 0: return False
    elif x >= N or y >= M : return False
    else: return True

def bfs(x,y):
    queue = deque()
    queue.append((x,y,[0,0]))
    visited[x][y] = [0,0]
    while queue:
        x, y, step = queue.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if iswall(nx,ny):
                temp = step[:]
                if matrix[nx][ny] == 'F':
                    if visited[nx][ny][0] > step[0] or (visited[nx][ny][0] == step[0] and visited[nx][ny][1] > step[1]):
                        visited[nx][ny] = temp
                        continue
                elif matrix[nx][ny] == 'a':
                        temp[1] += 1
                elif matrix[nx][ny] == 'g':
                        temp[0] += 1
                if visited[nx][ny][0] > temp[0] or (visited[nx][ny][0] == temp[0] and visited[nx][ny][1] > temp[1]):
                    queue.append((nx, ny, temp))
                    visited[nx][ny] = temp

global N,M
N, M = map(int,input().split())
matrix = [list(input()) for _ in range(N)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
visited = [[[5000,5000] for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 'F':
            arrive = (i,j)
        if matrix[i][j] == 'S':
            start = (i,j)
        if matrix[i][j] == 'g':
            for k in range(4):
                nx,ny = i + dx[k], j + dy[k]
                if 0<= nx < N and 0 <= ny < M:
                    if matrix[nx][ny] != 'F' and matrix[nx][ny] != 'S' and matrix[nx][ny] != 'g':
                        matrix[nx][ny] = 'a'

bfs(start[0],start[1])
print(*visited[arrive[0]][arrive[1]])