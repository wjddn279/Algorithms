import sys
sys.stdin = open("robot_cleaner.txt")


from _collections import deque

def iswall(x,y):
    if x < 0 or y < 0:
        return False
    elif x >= M or y >= N:
        return False
    elif matrix[x][y] == 'x':
        return False
    else:
        return True

def bfs(x_start,y_start):
    queue = deque()
    queue.append((x_start,y_start,0,[(x_start,y_start)]))
    while queue:
        x,y,visit,foot_step = queue.popleft()
        print(len(foot_step))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if iswall(nx,ny) and (nx,ny) not in foot_step:
                for k in range(len(target)):
                    if (nx,ny) == target[k]:
                        print(foot_step+[(nx,ny)])
                        visit = visit | (1<<k)
                        if visit == (1<<len(target))-1:
                            return len(foot_step)
                        queue.append((nx, ny, visit, foot_step+[(nx,ny)]))
                        break
                else:
                    queue.append((nx, ny, visit, foot_step+[(nx,ny)]))
    if result[0] == 987654321:
        return -1
    else:
        return result[0]

def search():
    target = []
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 'o':
                start = (i,j)
            elif matrix[i][j] == '*':
                target.append((i,j))
    return start, target
# N : 가로 M : 세로
# . : 깨끗, o : 출발점, * : 더러움, x : 가구
global N,M
dx = [0,0,-1,1]
dy = [1,-1,0,0]
while True:
    result = [987654321]
    N, M = map(int,input().split())
    if N == 0 and M == 0:
        break
    matrix = [list(input()) for _ in range(M)]
    start, target = search()
    if len(target) == 0:
        print(0)
    else:
        print(bfs(start[0],start[1]))