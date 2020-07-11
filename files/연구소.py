import sys
from _collections import deque
import itertools
sys.stdin = open("input8.txt")
def prin(a):
    for i in range(len(a)):
        print(*a[i])
    print()
def wall(x,y,matcopy):
    N,M = len(matrix),len(matrix[0])
    if x < 0 or y < 0:
        return False
    elif x >= N or y >= M:
        return False
    elif matcopy[x][y]:
        return False
    else:
        return True
def bfs(x,y,cnt,min_value,matcopy):
    matcopy[x][y] = 3
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    queue = deque()
    queue.append((x,y))
    while queue:
        if cnt > min_value:
            return cnt
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if wall(nx,ny,matcopy):
                queue.append((nx,ny))
                cnt += 1
                matcopy[nx][ny] = 3
    return cnt
def search():
    start,point = [],[]
    cnt = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix[x][y] == 2:
                start.append((x,y))
            elif matrix[x][y] == 0:
                point.append((x,y))
            elif matrix[x][y] == 1:
                cnt += 1
    return start,point,cnt
def solve():
    start,point,buck = search()
    combs = list(itertools.combinations(point,3))
    min_value = 99999999999
    for comb in combs:
        matcopy = [[] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matcopy[i].append(matrix[i][j])
        for com in comb:
            a,b = com
            matcopy[a][b] = 1
        # prin(matcopy)
        now = 0
        for sta in start:
            x,y = sta
            if matcopy[x][y] == 2:
                now = bfs(x,y,now+1,min_value,matcopy)
        # prin(matcopy)
        if now  < min_value:
            min_value = now

    return len(matrix)*len(matrix[0]) - min_value - buck - 3
T = 3

for test_case in range(T):
    N,M = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    print(solve())