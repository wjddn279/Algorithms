import sys
sys.stdin = open("raizer.txt")

def prin(a):
    for i in range(len(a)):
        print(*a[i])
    print()
# 15:16

from _collections import deque

def iswall(x,y):
    if x < 0 or y < 0:
        return False
    elif x >= H or y >= W:
        return False
    elif matrix[x][y] == '*':
        return False
    else:
        return True

def decision(dir):
    # 우 좌 상 하
    if dir == 0: return [0,2,3]
    if dir == 1: return [1,2,3]
    if dir == 2: return [0,1,2]
    if dir == 3: return [0,1,3]

def find():
    point = []
    for i in range(H):
        for j in range(W):
            if matrix[i][j] == 'C':
                point.append(i)
                point.append(j)
            if len(point) == 4:
                return point
def bfs(x_strat,y_start,x_end,y_end,result):
    queue = deque()
    # x,y,꺾은횟수,현재방향
    for i in range(4):
        nx,ny = x_strat + dx[i],y_start + dy[i]
        if iswall(nx,ny):
            queue.append((nx,ny,0,i))
            visited[nx][ny][i] = 0
    while queue:
        x,y,cnt,dir = queue.popleft()
        if cnt >= result:
            continue
        for i in decision(dir):
            nx,ny = x+dx[i], y+dy[i]
            if iswall(nx,ny) and visited[nx][ny][i] > cnt:
                if dir == i: temp = cnt
                else: temp = cnt+1
                if nx == x_end and ny == y_end:
                    result = min(result,temp)
                else:
                    queue.append((nx,ny,temp,i))
                    visited[nx][ny][i] = temp
    return result
#
global W,H
W, H = map(int,input().split())
matrix = [list(input()) for _ in range(H)]
x_start,y_start,x_end,y_end = find()
visited = [[[987654321 for _ in range(4)] for _ in range(W)] for _ in range(H)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
print(bfs(x_start,y_start,x_end,y_end,987654321))