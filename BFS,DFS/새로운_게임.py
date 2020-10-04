# 20:55

import sys
sys.stdin = open("input.txt")

def prin(a):
    for i in a:
        print(*i)
    print()
# 1. N * N 체스판 위 K 개의 말 사용
# 2. 말은 1~K 번호 이동방향 위 아래 왼쪽 오른쪽 (상하좌우)
# 3. 가장 아래에 있는 말만 이동 가능.
# 이동 하려하는 칸이
# 흰색 -> 그칸으로 이동, 가장 위애 a말 올려놈
# 빨간색 -> 순서 바뀌어서 올라감
# 파란색 -> A번 말의 이동방향 반대로 하고 한칸 이동
# 말이 4개 이상 쌓이는 순간 게임 종료

from copy import deepcopy

def change_dir(a):
    if a == 1: return 2
    elif a== 2: return 1
    elif a==3 :return 4
    else: return 3

def iswall(x,y):
    if x < 0 or y <0:
        return False
    elif x >= N or y >= N:
        return False
    else:
        return True

def go_white_or_red(x,y,nx,ny):
    for idx in visited[x][y]:
        location[idx][0], location[idx][1] = nx, ny
    if matrix[nx][ny] == 0:
        visited[nx][ny] += visited[x][y]
    else:
        visited[nx][ny] += visited[x][y][::-1]
    visited[x][y] = []

def solve():
    for cnt in range(1000):
        for i in range(K):
            x, y, dir = location[i]
            if visited[x][y][0] == i:
                nx, ny = x + dx[dir], y + dy[dir]
                if not iswall(nx, ny) or matrix[nx][ny] == 2:
                    dir = change_dir(dir)
                    nx, ny = x + dx[dir], y + dy[dir]
                    if not iswall(nx, ny) or matrix[nx][ny] == 2:
                        nx,ny = x,y
                    else:
                        go_white_or_red(x,y,nx,ny)
                    location[i][2] = dir
                else:
                    go_white_or_red(x,y,nx,ny)

                if len(visited[nx][ny]) >= 4:
                    return cnt+1
    return -1


global N,K
N, K = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
visited = [[[] for _ in range(N)] for _ in range(N)]
# 우 좌 상 하
dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]

location = [0 for _ in range(K)]
for i in range(K):
    # 행 열 이동방향
    x,y,dir = map(int,input().split())
    visited[x-1][y-1].append(i)
    location[i] = [x-1,y-1,dir]

print(solve())