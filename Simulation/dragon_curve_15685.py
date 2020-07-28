import sys
sys.stdin = open("")

from _collections import deque

def iswall(x,y):

    if x < 0 or y < 0:
        return False
    elif x >= 100 or y >= 100:
        return False
    else:
        return True
# 끝점에 현재 도형 시계방향으로 돌린것

matrix = [[0 for _ in range(100)] for _ in range(100)]
N = int(input())
info = [list(map(int,input().split())) for _ in range(N)]
# 우 상 좌 하
dx = [1,0,-1,0]
dy = [0,-1,0,1]

for x_start,y_start,d,g in info:
    step = []
    for i in range(g):
        if i == 0:
            matrix[x_start][y_start] = 1
            step.append([x_start,y_start])
            if iswall(x_start+dx[d],y_start+dy[d]):
                nx,ny = x_start+dx[d],y_start+dy[d]
                matrix[nx][ny] = 1
                step.append([nx,ny])
        else:
            x_cri,y_cri = step.pop()
            length = len(step)
            for st in range(length):
                x,y = step[st]
                x_var,y_var = x_cri - x, y_cri - y



