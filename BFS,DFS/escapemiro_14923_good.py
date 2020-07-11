import sys
sys.stdin = open("escapemiro.txt")

# N : 세로 M: 가로

from _collections import deque
def iswall(x,y):
    if x < 0 or y < 0:
        return False
    elif x >= N or y >= M:
        return False
    else:
        return True

def bfs(x_start,y_start,x_end,y_end):
    queue = deque()
    # x, y, cnt, 벽뚫여부
    queue.append((x_start,y_start,0,0))
    # 벽 안뚫 cnt, 벽 뚫 cnt
    visited = [[[987654321,987654321] for _ in range(M)] for _ in range(N)]
    visited[x_start][y_start][0] = 0
    while queue:
        x,y,cnt,wall_visi = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if iswall(nx,ny):
                if cnt + 1 < visited[nx][ny][wall_visi]:
                    if wall_visi == 0:
                        queue.append((nx,ny,cnt+1,matrix[nx][ny]))
                        visited[nx][ny][matrix[nx][ny]] = cnt+1
                    else:
                        if matrix[nx][ny] == 0:
                            queue.append((nx, ny, cnt + 1, wall_visi))
                            visited[nx][ny][wall_visi] = cnt + 1

    if min(visited[x_end][y_end]) == 987654321:
        return -1
    else:
        return min(visited[x_end][y_end])

global N,M
N, M = map(int,input().split())
x_start, y_start = map(int,input().split())
x_end, y_end = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
print(bfs(x_start-1,y_start-1,x_end-1,y_end-1))