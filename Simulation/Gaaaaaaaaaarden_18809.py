import sys
sys.stdin = open("../input.txt")

def prin(a):
    for i in a:
        print(*i)
    print()

from _collections import deque
from itertools import combinations

def iswall(x,y):
    if x < 0 or y < 0: return False
    elif x >= N or y >= M: return False
    elif matrix[x][y] == 0: return False
    else: return True

def bfs(green,red,result):
    queue = deque()
    visited = [[[-1,-1] for _ in range(M)] for _ in range(N)]
    cnt = 0
    for gre in green:
        queue.append((land[gre][0],land[gre][1],0,0))
        visited[land[gre][0]][land[gre][1]] = [0, 0]
    for re in red:
        queue.append((land[re][0],land[re][1],1,0))
        visited[land[re][0]][land[re][1]] = [1, 0]
    while queue:
        x,y,color,rnd = queue.popleft()
        if visited[x][y] == 'f':
            continue
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if iswall(nx,ny):
                if visited[nx][ny] == [-1,-1]:
                    queue.append((nx,ny,color,rnd+1))
                    visited[nx][ny] = [color,rnd+1]
                elif visited[nx][ny] != 'f':
                    if visited[nx][ny][0] != color and visited[nx][ny][1] == rnd+1:
                        visited[nx][ny] = 'f'
                        cnt += 1
    return max(result,cnt)



global N,M,G,R
N, M, G, R = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]
# matrix: 0 -> 호수, 1 -> 뿌릴 수 있는 땅, 2 -> 배양액 못 뿌리는 땅

land = []
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 2:
            land.append((i,j))

result = 0
for per in combinations(list(range(len(land))),G+R):
    for green in combinations(per,G):
        red = []
        for num in per:
            if num not in green:
                red.append(num)
        result = bfs(green,red,result)
print(result)
