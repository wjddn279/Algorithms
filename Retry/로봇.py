import sys
sys.stdin = open("input.txt")

def prin(a):
    for i in a:
        print(i)
    print()

from _collections import deque

def iswall(x,y):
    if x < 0 or y < 0: return False
    elif x >= N or y >= M: return False
    elif matrix[x][y] == 1: return False
    else: return True

def dir_change(d):
    if d == 1 : return 0
    elif d == 2 : return 2
    elif d == 3 : return 3
    elif d == 4 : return 1

def bfs(x,y,d,ex,ey,ed):
    queue = deque()
    queue.append((x,y,d,1))
    visited[x][y][d] = 1
    while queue:
        x,y,d,c = queue.popleft()
        # 방향 그대로 가기
        for k in range(1,4):
            nx,ny = x+k*dx[d],y+k*dy[d]
            if iswall(nx,ny):
                if not visited[nx][ny][d]:
                    queue.append((nx,ny,d,c+1))
                    visited[nx][ny][d] = c+1
            else:
                break
        # 우로 회전
        nd = (d+1)%4
        if not visited[x][y][nd]:
            queue.append((x,y,nd,c+1))
            visited[x][y][nd] = c+1
        nd = (d+3)%4
        if not visited[x][y][nd]:
            queue.append((x,y,nd,c+1))
            visited[x][y][nd] = c+1

        if visited[ex][ey][ed]:
            return visited[ex][ey][ed]-1


global N,M
N, M = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
sx,sy,sd = map(int,input().split())
ex,ey,ed = map(int,input().split())
sx,sy = sx-1,sy-1
ex,ey = ex-1,ey-1
sd,ed = dir_change(sd),dir_change(ed)
# 1 : 동 2: 서 3 : 남 4 : 북
# 동 북 서 남
dx = [0,-1,0,1]
dy = [1,0,-1,0]
visited = [[[0,0,0,0] for _ in range(M)] for _ in range(N)]
print(bfs(sx,sy,sd,ex,ey,ed))
