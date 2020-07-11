import sys
sys.stdin = open("backon.txt")

def prin(a):
    for i in range(len(a)):
        print(*a[i])
    print()

from _collections import deque

# N : 유저 수 M : 친구 관계 수

def bfs(start):
    queue = deque()
    queue.append(start)
    visited = [0 for _ in range(N+1)]
    visited[start] = 1
    while queue:
        now = queue.popleft()
        for i in range(1,N+1):
            if matrix[now][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = visited[now]+1
    return sum(visited)-N



global N
N,M = map(int,input().split())
matrix = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(M):
    x,y = map(int,input().split())
    matrix[x][y] = 1
    matrix[y][x] = 1
min_value = 987654321
min_idx = 987654321
for i in range(1,N+1):
    value = bfs(i)
    if value < min_value:
        min_value = value
        min_idx = i
    elif value == min_value and i < min_idx:
        min_value = value
        min_idx = i
print(min_idx)
