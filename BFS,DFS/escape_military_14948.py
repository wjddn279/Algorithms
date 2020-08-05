import sys
sys.stdin = open("escape_military_14948.txt")

def prin(a):
    for i in a:
        print(*i)
    print()

from _collections import deque

def iswall(x,y):
    if x < 0 or y < 0 : return False
    elif x >= N or y >= M :return False
    else: return True
def bfs(xs,ys,xe,ye):
    queue = deque()
    queue.append((xs,ys,matrix[xs][ys],0))
    visited[xs][ys][0] = matrix[xs][ys]
    while queue:
        x,y,val,k = queue.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if iswall(nx,ny):
                temp = max(val,matrix[nx][ny])
                if visited[nx][ny][k] > temp:
                    queue.append((nx,ny,temp,k))
                    visited[nx][ny][k] = temp
                if k == 0:
                    nnx,nny = nx+dx[i],ny+dy[i]
                    if iswall(nnx,nny):
                        temp = max(val,matrix[nnx][nny])
                        if visited[nnx][nny][1] > temp:
                            queue.append((nnx,nny,temp,1))
                            visited[nnx][nny][1] = temp
    return min(visited[xe][ye][0],visited[xe][ye][1])

global N,M
N, M = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
visited = [[[9876543210,9876543210] for _ in range(M)] for _ in range(N)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
print(bfs(0,0,N-1,M-1))
