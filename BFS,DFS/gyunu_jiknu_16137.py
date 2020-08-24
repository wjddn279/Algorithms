import sys
sys.stdin = open("input.txt")

def prin(a):
    for i in a:
        print(*i)
    print()

from _collections import deque

def bfs(i,j,a):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    if a == 1:
        matrix[i][j] = M
    queue = deque()
    # x, y, cnt, flag(이전에 오작교 건넜냐 아니냐)
    queue.append((0,0,0,0))
    visited[0][0] = 1
    while queue:
        x,y,cnt,flag = queue.popleft()
        for k in range(4):
            nx,ny = x+dx[k],y+dy[k]
            if iswall(nx,ny) and visited[nx][ny] == 0:
                if nx == N-1 and ny == N-1:
                    if a == 1:
                        matrix[i][j] = 0
                    return cnt+1
                if matrix[nx][ny] == 1:
                    queue.append((nx,ny,cnt+1,0))
                    visited[nx][ny] = 1
                elif matrix[nx][ny] > 1 and flag == 0:
                    if (cnt+1)%matrix[nx][ny] == 0:
                        queue.append((nx, ny, cnt + 1,1))
                        visited[nx][ny] = 1
                    else:
                        queue.append((x, y, cnt + 1,0))

    if a == 1:
        matrix[i][j] = 0
    return -1

def iswall(x,y):
    if x < 0 or y < 0:
        return False
    elif x >= N or y >= N :
        return False
    else:
        return True

# N * N 행렬, M : 새로 만들어지는 오작교의 주기
global N,M
N, M = map(int,input().split())
# 0: 건널 수 없는 절벽, 1: 이동할 수 있는 일반적인 땅, 2이상의 수: 오작교
matrix = [list(map(int,input().split())) for _ in range(N)]
cliff = [[0 for _ in range(N)] for _ in range(N)]
# 100 * 100
dx = [0,0,-1,1]
dy = [1,-1,0,0]

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 0:
            row,col = 0,0
            for k in range(0,2,1):
                nx,ny = i + dx[k], j + dy[k]
                if iswall(nx,ny):
                    if matrix[nx][ny] != 1:
                        row = 1
            for k in range(2,4,1):
                nx,ny = i + dx[k], j + dy[k]
                if iswall(nx,ny):
                    if matrix[nx][ny] != 1:
                        col = 1
            if row + col == 1:
                cliff[i][j] = 1
            elif row + col == 0:
                cliff[i][j] = 1

result = 98765421
for i in range(N):
    for j in range(N):
        if cliff[i][j]:
            temp = bfs(i,j,1)
            if temp != -1:
                result = min(result,temp)

if result !=  98765421:
    print(result)
else:
    print(bfs(0,0,0))



