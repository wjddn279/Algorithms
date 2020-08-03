import sys
sys.stdin = open("making_bridge_2146.txt")

def prin(a):
    for i in a:
        print(*i)
    print()

from _collections import deque

def iswall(x,y):
    if x < 0 or y < 0:
        return False
    elif x >= N or y >= N:
        return False
    else:
        return True

def bounding():
    cnt = 0
    for i in range(N):
        for j in range(N):
            if boundary[i][j] == 0 and matrix[i][j] == 1:
                cnt += 1
                queue = deque()
                queue.append((i,j))
                boundary[i][j] = cnt
                while queue:
                    x,y = queue.popleft()
                    for k in range(4):
                        nx,ny = x+dx[k],y+dy[k]
                        if iswall(nx,ny) and boundary[nx][ny] == 0 and matrix[nx][ny] == 1:
                            queue.append((nx,ny))
                            boundary[nx][ny] = cnt

def counting(x_start,y_start,result):
    queue = deque()
    queue.append((x_start,y_start,0))
    visited[x_start][y_start] = 1
    while queue:
        x,y,cnt = queue.popleft()
        if cnt == result:
            return cnt
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if iswall(nx,ny):
                if boundary[nx][ny] != 0:
                    if boundary[nx][ny] == boundary[x_start][y_start]:
                        continue
                    else:
                        return cnt
                elif visited[nx][ny] == 0:
                    queue.append((nx,ny,cnt+1))
                    visited[nx][ny] = 1
    return cnt


global N
N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]
boundary = [[0 for _ in range(N)] for _ in range(N)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
bounding()

result = 987654321
for i in range(N):
    for j in range(N):
        if boundary[i][j] != 0:
            visited = [[0 for _ in range(N)] for _ in range(N)]
            temp = counting(i,j,result)
            if temp != 0:
                result = min(result,temp)
print(result)