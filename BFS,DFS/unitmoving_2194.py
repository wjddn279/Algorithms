import sys
sys.stdin = open("unitmoving.txt")

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
    elif matrix[x][y] == 1:
        return False
    else:
        return True

def wallcheck(nx,ny,A,B):
    if wall(nx,ny):
        if visited[nx][ny] == 1:
            return 1
    for i in range(A):
        for j in range(B):
            if wall(nx+i,ny+j) == 0:
                return 1
    return 3

def bfs(x,y,A,B,x_end,y_end):
    queue = deque()
    queue.append((x,y,0))
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    visited[x][y] = 1
    while queue:
        x,y,cnt = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx,ny) == (x_end,y_end):
                return cnt+1
            chk = wallcheck(nx,ny,A,B)
            if chk == 3:
                visited[nx][ny] = 1
                queue.append((nx,ny,cnt+1))
    return -1
# N x M : 전체 행렬 A X B : 유닛 크기 K : 장애물 줄수

global N,M
N, M, A, B, K = map(int,input().split())
matrix = [[0 for _ in range(M)] for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

for i in range(K):
    x,y = map(int,input().split())
    matrix[x-1][y-1] = 1
# 시작점의 위치와 도착점의 위치는 제일 왼쪽 제일 위 한점만 주어진다.
x_start, y_start = map(int, input().split())
x_end, y_end = map(int, input().split())

print(bfs(x_start-1,y_start-1,A,B,x_end-1,y_end-1))
# 1: 벽 2: 현재 드라군 위치 3: 도착할 드라군 위치
