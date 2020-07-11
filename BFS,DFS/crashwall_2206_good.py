import sys
sys.stdin = open("crashwall.txt")

def prin(a):
    for i in range(len(a)):
        print(*a[i])
    print()

from _collections import deque

def iswall(x,y):
    if x < 0 or y < 0:
        return False
    elif x >= N or y >= M:
        return False
    else:
        return True
def bfs(x_end,y_end):
    queue = deque()
    # x, y, cnt, 방문 여부
    queue.append((0,0,1,0))
    # 벽안뚫최소, 벽뚫최소
    visited = [[[987654321,987654321] for _ in range(M)] for _ in range(N)]
    visited[0][0] = [1,987654321]
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    while queue:
        x,y,cnt,wall_visi = queue.popleft()
        if cnt >= min(visited[x_end][y_end]):
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if iswall(nx,ny):
                # 다음 위치가 벽이든 아니든 방문하지 않았으면 푸쉬
                if cnt+1 < visited[nx][ny][wall_visi]:
                    # 벽을 안뚫은 경로 -> 벽이건 뭐건 다 담는데 벽을 만나면 벽 뚫이 1되야함
                    if wall_visi == 0:
                        queue.append((nx,ny,cnt+1,matrix[nx][ny]))
                        visited[nx][ny][matrix[nx][ny]] = cnt+1
                    # 벽을 뚫은 경로 -> 그냥 길만 담고 무조건 벽뚫여부는 무조건 참
                    else:
                        if matrix[nx][ny] == 0:
                            queue.append((nx, ny, cnt + 1, wall_visi))
                            visited[nx][ny][wall_visi] = cnt + 1

    if min(visited[x_end][y_end])== 987654321:
        return -1
    else:
        return  min(visited[x_end][y_end])
global N,M
N,M = map(int,input().split())
matrix = [list(map(int,input())) for _ in range(N)]
print(bfs(N-1,M-1))

