import sys
sys.stdin = open("input.txt")

# 10:22


from _collections import deque

def iswall(x,y):
    if x < 0 or y < 0 :
        return False
    elif x >= N or y >= M:
        return False
    elif matrix[x][y] == 1:
        return False
    else:
        return True

def bfs(x,y,cnt):
    queue = deque()
    queue.append((x,y))
    val = 1
    visited[x][y] = cnt
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if iswall(nx,ny) and not visited[nx][ny]:
                visited[nx][ny] = cnt
                queue.append((nx,ny))
                val += 1
    area.append(val)

global N,M
N, M = map(int,input().split())
matrix = [list(map(int,input())) for _ in range(N)]

# 영역에 포함 된 갯수, 영역 구분을 위한 번호
visited = [[0 for _ in range(M)] for _ in range(N)]
area = [0,0]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
cnt = 2
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0 and visited[i][j] == 0:
            bfs(i,j,cnt)
            cnt +=1

result = [[0 for _ in range(M)] for _ in range(N)]
for x in range(N):
    for y in range(M):
        if matrix[x][y] == 1:
            result[x][y] += 1
            stack = []
            for i in range(4):
                nx,ny = x+dx[i],y+dy[i]
                if iswall(nx,ny):
                    if visited[nx][ny] != 0 and visited[nx][ny] not in stack:
                        result[x][y] += area[visited[nx][ny]]
                        stack.append(visited[nx][ny])
        print(result[x][y]%10, end="")
    print()
