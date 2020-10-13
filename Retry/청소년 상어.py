import sys
sys.stdin = open("input.txt")

def prin(a):
    for i in a:
        print(i)
    print()

from copy import deepcopy
from _collections import deque

def iswall(x,y,matrix):
    if x < 0 or y < 0 : return False
    elif x >=4 or y >= 4 : return False
    elif matrix[x][y][0] == -1: return False
    else : return True

def move_fish():
    for num in range(1, 17):
        x, y = fish[num]
        d = matrix[x][y][1]
        if x == -1 and y == -1:
            continue
        nx, ny = x + dx[d], y + dy[d]
        while not iswall(nx, ny, matrix):
            d = (d + 1) % 8
            nx, ny = x + dx[d], y + dy[d]
        # 빈칸이면
        if matrix[nx][ny][0] == 0:
            fish[num] = [nx, ny, d]
        else:
            next = matrix[nx][ny][0]
            fish[num], fish[next] = fish[next], fish[num]
        matrix[x][y], matrix[nx][ny] = matrix[nx][ny], matrix[x][y]
        matrix[nx][ny][1] = d

def move_shark(x,y,d,cnt):
    queue = deque()
    queue.append((x,y,d,cnt,deepcopy(matrix)))
    while queue:
        x,y,d,cnt,mat = queue.popleft()
        for k in range(4):
            nx,ny = x+k*dx[d],y+k*dy[d]
            if iswall(nx,ny,mat):
                queue.append((nx,ny,))

matrix = []
for _ in range(4):
    arr = list(map(int,input().split()))
    temp = []
    for i in range(4):
        x,y = arr[2*i:2*(i+1)]
        temp.append([x,y-1])
    matrix.append(temp)

fish = [[-1,-1,-1] for _ in range(17)]
for x in range(4):
    for y in range(4):
        fish[matrix[x][y][0]] = [x,y]

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

fish[matrix[0][0][0]] = [-1,-1]
cnt = matrix[0][0][0]
matrix[0][0][0] = -1
shark = [0,0,matrix[0][0][1]]
move_fish()
prin(matrix)
