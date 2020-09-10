# 10시 30분

import sys
sys.stdin = open("../input.txt")

def prin(a):
    for i in a:
        print(i)
    print()

from _collections import deque
from itertools import permutations

def iswall(x,y):
    if x < 0 or y < 0 : return False
    elif x >=N or y >= M : return False
    else: return True

def search():
    cnt = 1
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and matrix[i][j]:
                start.append((i,j))
                go_island(i,j,cnt)
                cnt += 1
    return cnt

def go_island(i,j,cnt):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = 1
    matrix[i][j] = cnt
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if iswall(nx,ny) and matrix[nx][ny] and not visited[nx][ny]:
                queue.append((nx,ny))
                matrix[nx][ny] = cnt
                visited[nx][ny] = 1

def dis_island(i):
    visited = [[float('inf') for _ in range(M)] for _ in range(N)]
    queue = deque()
    queue.append((start[i-1][0],start[i-1][1],0,-1))
    visited[start[i-1][0]][start[i-1][1]] = 0
    while queue:
        x,y,cnt,dir = queue.popleft()
        if dir == -1:
            for k in range(4):
                nx,ny = x+dx[k],y+dy[k]
                if iswall(nx,ny):
                    if matrix[nx][ny] == i and visited[nx][ny] > cnt + 1:
                        queue.append((nx,ny,0,-1))
                        visited[nx][ny] = 0
                    elif matrix[nx][ny] == 0:
                        queue.append((nx,ny,cnt+1,k))
                    else:
                        if distance[i][matrix[nx][ny]] > cnt:
                            distance[i][matrix[nx][ny]] = cnt
        else:
            nx, ny = x + dx[dir], y + dy[dir]
            if iswall(nx, ny):
                if matrix[nx][ny] == i  and visited[nx][ny] > cnt + 1:
                    queue.append((nx, ny, 0, -1))
                    visited[nx][ny] = 0
                elif matrix[nx][ny] == 0:
                    queue.append((nx, ny, cnt + 1, dir))
                    visited[nx][ny] = cnt + 1
                else:
                    if distance[i][matrix[nx][ny]] > cnt and cnt != 1:
                        distance[i][matrix[nx][ny]] = cnt

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    fx = find(x)
    fy = find(y)
    if fx != fy:
        parent[fy] = fx


global N,M
N, M = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
start = []
search()
num_island = len(start)
distance = [[200 for _ in range(num_island+1)] for _ in range(num_island+1)]
for i in range(1,num_island+1):
    dis_island(i)
result = 0
node = []
for i in range(1,num_island+1):
    for j in range(i,num_island+1):
        if distance[i][j] != 200 and distance[i][j] != 0:
            node.append((i,j,distance[i][j]))

node.sort(key=lambda x:x[2])
parent = [i for i in range(num_island+1)]
cnt = 0
for v1,v2,cost in node:
    if find(v1) != find(v2):
        union(v1,v2)
        cnt += 1
        result += cost
if cnt == num_island-1:
    print(result)
else:
    print(-1)

