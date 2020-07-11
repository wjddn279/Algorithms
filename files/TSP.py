import sys
sys.stdin = open("TSP.txt")

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
    elif matrix[x][y] == '#':
        return False
    else:
        return True

def search():
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == '0':
                start = (i,j)
                matrix[i][j] = '.'
                return start

def bfs(x,y):
    queue = deque()
    # x,y, 주운 열쇠, 방문기록
    queue.append((x,y,0,0))
    visited[x][y][0] = 1
    while queue:
        x,y,key,cnt = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if iswall(nx,ny) and visited[nx][ny][key] == 0:
                if matrix[nx][ny] == '1':
                    return cnt+1
                elif matrix[nx][ny] == '.' :
                    queue.append((nx,ny,key,cnt+1))
                    visited[nx][ny][key] = 1
                else:
                    # 소문자다 -> 열쇠다
                    if matrix[nx][ny].islower():
                        for i in range(len(keys)):
                            if matrix[nx][ny] == keys[i]:
                                next_key = key | (1<<i)
                                queue.append((nx, ny, next_key, cnt + 1))
                                visited[nx][ny][next_key] = 1
                                break
                    # 대문자다 -> 문이다
                    else:
                        for i in range(len(doors)):
                            if matrix[nx][ny] == doors[i]:
                                if key & (1<<i):
                                    queue.append((nx,ny,key,cnt+1))
                                    visited[nx][ny][key] = 1
    return -1
global N,M
N,M = map(int,input().split())
matrix = [list(input()) for _ in range(N)]
doors = ['A','B','C','D','E','F']
keys = ['a','b','c','d','e','f']
visited = [[[0 for _ in range(1<<6)] for _ in range(M)] for _ in range(N)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
start = search()
print(bfs(start[0],start[1]))
