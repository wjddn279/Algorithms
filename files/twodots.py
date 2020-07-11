import sys
sys.stdin = open("twodots.txt")

def prin(a):
    for i in range(len(a)):
        print(*a[i])
    print()

from _collections import deque

def search():
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0:
                return (i,j)
    return -1
def iswall(x,y):
    if x < 0 or y < 0:
        return False
    elif x >= N or y >= M:
        return False
    else:
        return True
def bfs(x_start,y_start):
    queue = deque()
    # x위치,y위치,색깔
    queue.append((x_start,y_start,matrix[x_start][y_start],x_start,y_start))
    visited[x_start][y_start] = matrix[x_start][y_start]
    result = False
    while queue:
        prin(visited)
        x,y,color,x_not,y_not = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if iswall(nx,ny) and matrix[nx][ny] == color:
                # 전에 왔던 좌표로 돌아가지 않고 방문한 좌표와 갔을때 사이클
                if visited[nx][ny] == color and (nx,ny) != (x_not,y_not):
                    result = True
                elif visited[nx][ny] == 0:
                    queue.append((nx,ny,matrix[nx][ny],x,y))
                    visited[nx][ny] = matrix[nx][ny]
    return result
# N X M 행렬
global N,M
N, M = map(int,input().split())
matrix = [list(input()) for _ in range(N)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
# 색깔, 시작점 여부
visited = [[0 for _ in range(M)] for _ in range(N)]
while True:
    point = search()
    if point == -1:
        print('No')
        break
    else:
        result = bfs(point[0],point[1])
    if result == True:
        print('Yes')
        break
