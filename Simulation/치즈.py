import sys
sys.stdin = open("input.txt")

def prin(a):
    for i in a:
        print(i)
    print()
# N : 세로 격자 , M : 가로 격자
# 4변중 2변 이상이 실내온도와 접촉하면 한시간 안에 녹아버림

from _collections import deque

def iswall(x,y):
    if x < 0 or y < 0 : return False
    elif x >= N or y >= M : return False
    else: return True

def air(x,y):
    n_queue = deque()
    temp = []
    n_queue.append((x,y))
    a_visited[x][y] = 1
    while n_queue:
        x,y = n_queue.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if iswall(nx,ny) and not a_visited[nx][ny]:
                if matrix[nx][ny]:
                   visited[nx][ny] += 1
                   if visited[nx][ny] == 2:
                       temp.append((nx,ny))
                else:
                    n_queue.append((nx,ny))
                    a_visited[nx][ny] = 1
    return temp

global N,M
N, M = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
a_visited = [[0 for _ in range(M)] for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
time = 0
queue = air(0,0)
while queue:
    time += 1
    stack = []
    while queue:
        x,y = queue.pop()
        matrix[x][y] = 0
        stack += air(x,y)
    queue = stack[:]
print(time)


