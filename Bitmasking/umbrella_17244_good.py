import sys
sys.stdin = open("umbrella.txt")

def prin(a):
    for i in range(len(a)):
        print(*a[i])
    print()

from _collections import deque

def permutation(n,k,sum,x_start,y_start):
    if sum >= result[0]:
        return
    if n == k:
        temp1 = sum + bfs(x_start,y_start,target[k][0],target[k][1])
        if temp1 >= result[0]:
            return
        temp2 = temp1 + bfs(target[k][0],target[k][1],end[0],end[1])
        if temp2 < result[0]:
            result[0] = temp2
            return
    else:
        for i in range(k,n+1):
            target[i],target[k] = target[k],target[i]
            temp = sum + bfs(x_start,y_start,target[k][0],target[k][1])
            permutation(n,k+1,temp,target[k][0],target[k][1])
            target[i], target[k] = target[k], target[i]
def search():
    target = []
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 'S':
                start = (i,j)
            elif matrix[i][j] == 'E':
                end = (i,j)
            elif matrix[i][j] == 'X':
                target.append((i,j))

    return start,end,target

def iswall(x,y):
    if x < 0 or y < 0:
        return False
    elif x >= M or y >= N:
        return False
    elif matrix[x][y] == '#' or matrix[x][y] == 'E':
        return False
    else:
        return True

def bfs(x,y,x_end,y_end):
    queue = deque()
    queue.append((x,y,0))
    visited = [[0 for _ in range(N)] for _ in range(M)]
    visited[x][y] = 1
    while queue:
        x,y,cnt = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx == x_end and ny == y_end:
                return cnt + 1
            if iswall(nx,ny) and visited[nx][ny] == 0:
                queue.append((nx,ny,cnt+1))
                visited[nx][ny] = 1

global N,M

result =[987654321]
N, M = map(int,input().split())
# N: 가로 길이, M: 세로 길이
# . : 비어 있는 곳, # : 벽, S : 현재 위치, E : 나가는 문의 위치, X: 챙겨야 하는 물건(최대 5개)
matrix = [list(input()) for _ in range(M)]
start,end,target = search()
dx = [0,0,-1,1]
dy = [1,-1,0,0]
if len(target) == 0:
    result[0] = bfs(start[0],start[1],end[0],end[1])
else:
    permutation(len(target)-1,0,0,start[0],start[1])
print(result[0])