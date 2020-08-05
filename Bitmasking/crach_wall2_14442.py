import sys
sys.stdin = open("crash_wall2.txt")

def prin(a):
    for i in a:
        print(*i)
    print()
from _collections import deque

def iswall(x,y):
    if x < 0 or y < 0: return False
    elif x >= N or y >= M: return False
    else: return True

def bfs(x_start,y_start,x_end,y_end):
    if x_start == x_end and y_start == y_end:
            return 1
    queue = deque()
    # x위치, y위치, 거리, 벽뚫은 횟수
    queue.append((x_start,y_start,1,0))
    visited[x_start][y_start] = visited[x_start][y_start] | (1<<0)
    while queue:
        x,y,cnt,k = queue.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if iswall(nx,ny):
                if (visited[nx][ny] & (1<<k)) == 0:
                    if nx == x_end and ny == y_end:
                        return cnt+1
                    if matrix[nx][ny] == 1 and k < K:
                        queue.append((nx,ny,cnt+1,k+1))
                        visited[nx][ny] = visited[nx][ny] | (1<<k+1)
                    elif matrix[nx][ny] == 0:
                        queue.append((nx,ny,cnt+1,k))
                        visited[nx][ny] = visited[nx][ny] | (1<<k)

    return -1
global N,M,K
N, M, K = map(int,input().split())
matrix = [list(map(int,input())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
print(bfs(0,0,N-1,M-1))