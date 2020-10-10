import sys
sys.stdin = open("input.txt")

def prin(a):
    for i in a:
        print(i)
    print()

from _collections import deque

def iswall(x,y):
    if x < 0 or y < 0 : return False
    elif x >= N or y >= N : return False
    elif matrix[x][y] == '1' : return False
    else: return True

def search(alpha):
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == alpha:
                if iswall(i,j+1) and iswall(i,j+2):
                    if matrix[i][j+1] == alpha and matrix[i][j+2] == alpha:
                        return (i,j,0)
                if iswall(i+1,j) and iswall(i+2,j):
                    if matrix[i+1][j] == alpha and matrix[i+2][j] == alpha:
                        return (i,j,1)

def check(x,y,d):
    if d == 0:
        if iswall(x,y) and iswall(x,y+1) and iswall(x,y+2):
            return True
        else:
            return False
    else:
        if iswall(x,y) and iswall(x+1,y) and iswall(x+2,y):
            return True
        else:
            return False

def turn(x,y,d):
    if d == 0:
        for i in range(x-1,x+2):
            for j in range(y,y+3):
                if not iswall(i,j):
                    return -1,-1,False,0
        return x-1,y+1,True,1
    else:
        for i in range(x,x+3):
            for j in range(y-1,y+2):
                if not iswall(i,j):
                    return -1,-1,False,0
        return x+1,y-1,True,0

def solve(x,y,d,ex,ey,ed):
    queue = deque()
    queue.append((x,y,d,1))
    visited[x][y][d] = 1
    while queue:
        x,y,d,c = queue.popleft()
        # 그냥 움직이기
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if check(nx,ny,d) and not visited[nx][ny][d]:
                queue.append((nx,ny,d,c+1))
                visited[nx][ny][d] = c+1
        # 돌기
        nx,ny,flag,nd = turn(x,y,d)
        if flag and not visited[nx][ny][nd]:
            queue.append((nx,ny,nd,c+1))
            visited[nx][ny][nd] = c+1
        if visited[ex][ey][ed]:
            return visited[ex][ey][ed]-1
    return 0
global N
N = int(input())
matrix = [list(input()) for _ in range(N)]
visited = [[[0,0] for _ in range(N)] for _ in range(N)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]
tx,ty,td = search('B')
ex,ey,ed = search('E')
print(solve(tx,ty,td,ex,ey,ed))

# 0 : 가로 , 1 : 세로