import sys
sys.stdin = open("conquer_14950.txt")

def prin(a):
    for i in a:
        print(*i)
    print()

from _collections import deque

def search():
    fire = deque()
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 'F':
                matrix[i][j] = '#'
                fire.append((i,j))
            elif matrix[i][j] == 'J':
                man = (i,j)
    return fire,man

def iswall(x,y):
    if x < 0 or y < 0: return False
    elif x >= N or y >= M: return False
    elif matrix[x][y] == '#': return False
    else: return True

def bfs(x,y):
    if x == N-1 or y == M-1 or x == 0 or y == 0:
        return 1
    queue = deque()
    queue.append((x,y,0))
    criteria = 0
    visited[x][y] = 1
    while queue:
        x,y,cnt = queue.popleft()
        if cnt == criteria:
            length = len(fire)
            for k in range(length):
                xf,yf = fire.popleft()
                for i in range(4):
                    nxf,nyf = xf+dx[i],yf+dy[i]
                    if iswall(nxf,nyf):
                        matrix[nxf][nyf] = '#'
                        fire.append((nxf,nyf))
            criteria += 1
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if iswall(nx,ny) and not visited[nx][ny]:
                if nx == N-1 or nx == 0 or ny == 0 or ny == M-1:
                    return cnt++2
                queue.append((nx,ny,cnt+1))
                visited[nx][ny] = 1
    return 'IMPOSSIBLE'


global N,M
N, M = map(int,input().split())
matrix = [list(input()) for _ in range(N)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
visited = [[0 for _ in range(M)] for _ in range(N)]
fire,man = search()
print(bfs(man[0],man[1]))