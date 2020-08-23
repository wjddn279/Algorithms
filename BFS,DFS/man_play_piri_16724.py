import sys
sys.stdin = open("input.txt")

def prin(a):
    for i in a:
        print(*i)
    print()

from _collections import deque

def bfs(x,y,cnt):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = cnt
    while queue:
        x,y = queue.popleft()
        dx,dy = direction[matrix[x][y]]
        nx,ny = x+dx, y+dy
        # 안들린 점이 있으면 내걸로 만들고
        if visited[nx][ny] == 0:
            queue.append((nx,ny))
            visited[nx][ny] = cnt
        # 내 점이랑 이어지네? -> circular 하다는 거니까 내 영토
        elif visited[nx][ny] == visited[x][y]:
            result[0] += 1
            return cnt+1
        # 다른 점이랑 만났네? -> 나는 그 영토에 소속이었네
        elif visited[nx][ny] < visited[x][y]:
            return cnt+1

    return cnt+1

N, M = map(int,input().split())
matrix = [list(input()) for _ in range(N)]
direction = {'D':(1,0),'R':(0,1),'L':(0,-1),'U':(-1,0)}
visited = [[0 for _ in range(M)] for _ in range(N)]
result = [0]
cnt = 1
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            cnt = bfs(i,j,cnt)

print(result[0])