import sys
sys.stdin = open("input.txt")

def prin(a):
    for i in a:
        print(i)

from _collections import deque

def iswall(x,y):
    if x < 0 or y < 0: return False
    elif x >= N or y >= M: return False
    else: return True

def solve():
    visited = [[float('inf') for _ in range(M)] for _ in range(N)]
    queue = deque()
    # 벽 뿌순 횟수
    queue.append((0,0,0))
    visited[0][0] = 0
    while queue:
        x,y,cnt = queue.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if iswall(nx,ny):
                if matrix[nx][ny] == 0 and visited[nx][ny] > cnt:
                    queue.append((nx,ny,cnt))
                    visited[nx][ny] = cnt
                elif matrix[nx][ny] != 0 and visited[nx][ny] > cnt + 1:
                    queue.append((nx,ny,cnt+1))
                    visited[nx][ny] = cnt+1
    return visited[N-1][M-1]

global N,M
M,N = map(int,input().split())
matrix = [list(map(int,input())) for _ in range(N)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
print(solve())