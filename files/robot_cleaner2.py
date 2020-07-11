import sys
sys.stdin = open("robot_cleaner.txt")

def prin(a):
    for i in range(len(a)):
        print(*a[i])
    print()
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

def permu(n,k,sum,start):
    if sum > result[0]:
        return
    if n == k:
        temp = count[step[k]][start]
        if sum + temp < result[0]:
            result[0] = sum + temp
    else:
        for i in range(k,n+1):
            step[i],step[k] = step[k],step[i]
            temp = count[step[k]][start]
            permu(n,k+1,sum+temp,step[k])
            step[i],step[k] = step[k],step[i]

def bfs(x_start,y_start,x_end,y_end):
    queue = deque()
    queue.append((x_start,y_start,0))
    visited = [[0 for _ in range(N)] for _ in range(M)]
    visited[x_start][y_start] = 1
    while queue:
        x,y,cnt = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if iswall(nx,ny) and visited[nx][ny] == 0:
                if nx == x_end and ny == y_end:
                    return cnt+1
                else:
                    queue.append((nx,ny,cnt+1))
                    visited[nx][ny] = 1
    return -1

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

def cnt():
    for i in range(len(target)):
        for j in range(i+1,len(target)):
            value = bfs(target[i][0],target[i][1],target[j][0],target[j][1])
            count[i][j] = value
            count[j][i] = value
            if count[i][j] == -1:
                return False
    return True

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
    target.append(start)
    count = [[0 for _ in range(len(target))] for _ in range(len(target))]
    step = list(range(0,len(target)-1))
    flag = cnt()
    if flag:
        permu(len(step)-1,0,0,len(target)-1)
        print(result[0])
    else:
        print(-1)