import sys
sys.stdin = open("input.txt")



from _collections import deque

def prin():
    for i in range(N):
        for j in range(M):
            if matrix[i][j]:
                print((result[i][j]+1)%10, end="")
            else:
                print(0, end="")
        print()
def iswall(x,y):
    if x < 0 or y < 0 : return False
    elif x >= N or y >= M : return False
    else : return True

def bfs(x,y):
    stack = {}
    cnt = 1
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if iswall(nx,ny):
                if matrix[nx][ny]:
                    stack[(nx,ny)] = 0
                elif not visited[nx][ny]:
                    queue.append((nx,ny))
                    cnt += 1
                    visited[nx][ny] = 1
    for x,y in stack.keys():
        result[x][y] += cnt
    return cnt

global N,M
N, M = map(int,input().split())
matrix = [list(map(int,input())) for _ in range(N)]
result = [[0 for _ in range(M)] for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
for i in range(N):
    for j in range(M):
        if not matrix[i][j] and not visited[i][j]:
            bfs(i,j)
prin()