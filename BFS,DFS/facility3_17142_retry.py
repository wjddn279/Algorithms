import sys
sys.stdin = open("../input.txt")

def prin(a):
    for i in range(len(a)):
        print(*a[i])
    print()

from _collections import deque
from itertools import combinations

def iswall(x,y):
    if x < 0 or y < 0: return False
    elif x >= N or y >=N: return False
    elif matrix[x][y] == 1: return False
    else: return True

def bfs(locate,result):
    queue = deque()
    ready, num = [], 0
    max_val = 0
    for x,y in locate:
        queue.append((x,y))
        visited[x][y] = 0
    while queue:
        if num == total:
            return max_val
        x,y = queue.popleft()
        cnt = visited[x][y]
        if cnt == result:
            return cnt
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i],
            if iswall(nx,ny) and visited[nx][ny] == -1:
                queue.append((nx,ny))
                visited[nx][ny] = cnt+1
                if matrix[nx][ny] == 0:
                    max_val = max(max_val,visited[nx][ny])
                    num += 1
    if num == total:
        return cnt
    else:
        return -1


global N, total
N, M = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
total,virus = 0, []
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 0:
            total += 1
        elif matrix[i][j] == 2:
            virus.append((i,j))

result = float('inf')
for locate in combinations(virus,M):
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    cnt = bfs(locate,result)
    if cnt != -1:
        result = min(result,cnt)
if result == float('inf'):
    print(-1)
else:
    print(result)




