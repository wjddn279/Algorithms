# 0이 빈칸 1이 집 2가 치킨집
# 치킨 거리 : |r1-r2| + |c1-c2|

import sys
sys.stdin = open('chicken.txt')
from _collections import deque
from itertools import combinations

def search():
    home, chicken = [], []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                home.append((i,j))
            elif matrix[i][j] == 2:
                chicken.append((i,j))
    return home, chicken

def wall(x,y):
    if x < 0 or y < 0:
        return False
    elif x >= len(matrix) or y >= len(matrix):
        return False
    else:
        return True
def bfs(start_x,start_y,target,now,minimum):
    temp = 9999999999
    for tar in target:
        a = abs(start_x-tar[0]) + abs(start_y-tar[1])
        if a < temp:
            temp = a
    if minimum < now +temp:
        return -1
    else:
        return now +temp

def solve(can):
    minimum = 9999999999
    for target in can:
        now = 0
        for home in homes:
            x,y = home
            now = bfs(x,y,target,now,minimum)
            if now == -1:
                break
        else:
            if now < minimum:
                minimum = now
    return minimum
N,M = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
homes, chicken = search()
candidate = list(combinations(chicken,M))
dx = [0,0,-1,1]
dy = [1,-1,0,0]
print(solve(candidate))
