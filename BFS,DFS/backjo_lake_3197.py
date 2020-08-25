import sys
sys.stdin = open("input.txt")

def prin(a):
    for i in a:
        print(*i)
    print()

from _collections import deque

def iswall(x,y):
    if x < 0 or y < 0 :return False
    elif x >= N or y >= M: return False
    else: return True


def ready():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == '.' or matrix[i][j] == 'L':
                cnt += 1
                if matrix[i][j] == 'L':
                    target.append(cnt)
                queue = deque()
                queue.append((i,j))
                visited[i][j] = cnt
                matrix[i][j] = cnt
                while queue:
                    x,y = queue.popleft()
                    for k in range(4):
                        nx,ny = x+dx[k],y+dy[k]
                        if iswall(nx,ny):
                            if visited[nx][ny] == 0:
                                if matrix[nx][ny] == 'L':
                                    target.append(cnt)
                                    queue.append((nx,ny))
                                    visited[nx][ny] = cnt
                                    matrix[nx][ny] = cnt
                                if matrix[nx][ny] == '.':
                                    queue.append((nx,ny))
                                    visited[nx][ny] = cnt
                                    matrix[nx][ny] = cnt
                                if matrix[nx][ny] == 'X':
                                    next_queue.append((nx,ny,cnt,1))
                                    visited[nx][ny] = cnt

def change(b,x,y):
    aqueue = deque()
    aqueue.append((x,y))
    sub_visited[x][y] = 1
    matrix[x][y] = b
    while aqueue:
        x,y = aqueue.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if iswall(nx,ny) and sub_visited[nx][ny] == 0:
                if matrix[nx][ny] != 'X' and not matrix[nx][ny] in target:
                    matrix[nx][ny] = b
                    sub_visited[nx][ny] = 1
                    aqueue.append((nx,ny))

def bfs():
    while next_queue:
        x,y,area,cnt = next_queue.popleft()
        matrix[x][y] = area
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if iswall(nx,ny):
                if visited[nx][ny] == 0:
                    if matrix[nx][ny] == 'X':
                        next_queue.append((nx,ny,matrix[x][y],cnt+1))
                        visited[nx][ny] = cnt+1
                if matrix[nx][ny] in target:
                    if matrix[nx][ny] == target[0]:
                        if matrix[x][y] == target[1]:
                            return cnt
                        else:
                            change(matrix[nx][ny], x, y)

                    if matrix[nx][ny] == target[1]:
                        if matrix[x][y] == target[0]:
                            return cnt
                        else:
                            change(matrix[nx][ny], x, y)


global N,M
N, M = map(int,input().split())
matrix = [list(input()) for _ in range(N)]
visited =[[0 for _ in range(M)] for _ in range(N)]
sub_visited =[[0 for _ in range(M)] for _ in range(N)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
target = []
next_queue = deque()
ready()
print(bfs())
