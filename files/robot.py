import sys
sys.stdin = open("robot.txt")

def prin(a):
    for i in range(len(a)):
        print(*a[i])
    print()

# 명령 1 : GO K  현재 향하는 방향으로 k 만큼 움직임
# 명령 2: Turn dir : dir은 left or right 이며 90도 회전
from _collections import deque
# 0 은 갈수 있는 지점 1 은 못가는 지점
# 로봇을 원하는 위치로 이동시키고 우너하는 방향으로 바로보도록 하는 명령어 횟수
def iswall(x,y):
    if x < 0 or y < 0:
        return False
    elif x >= M or y >= N:
        return False
    elif matrix[x][y] == 1:
        return False
    else:
        return True

def decision(i):
    if i == 0:
        return 1
    elif i == 1 or i == 2:
        return 2
    else:
        return 3
def bfs(x,y,dir,x_end,y_end,dir_end):
    if x == x_end and y == y_end:
        for j in range(4):
            if direction[dir][j] == dir_end:
                return decision(j)-1
    queue = deque()
    queue.append((x,y,dir,0))
    visited = [[987654321 for _ in range(N)] for _ in range(M)]
    visited[x][y] = 0
    result = 987654321
    while queue:
        x,y,dir,cnt = queue.popleft()
        for i in range(4):
            moving = direction[dir]
            for k in range(1,4):
                nx = x + k * dx[moving[i]]
                ny = y + k * dy[moving[i]]
                # if iswall(nx,ny) and cnt + decision(i) < visited[nx][ny]: 해주면 안되는 이유?
                # else 할 경우 한칸 두칸 세칸 갈 수 있는데, 벽에 막힐 경우에만 짤라야 하고
                # visited는 한칸은 안되더라도 두칸, 세칸은 될 수 있다.
                # 또 queue 에 담을 때 cnt + decision(i) <= visited[nx][ny]과 cnt + decision(i) < visited[nx][ny] 은 엄청난 메모리 차이가 있다.
                if iswall(nx,ny):
                    if cnt + decision(i) < visited[nx][ny]:
                        if nx == x_end and ny == y_end:
                            dir = moving[i]
                            for j in range(4):
                                if direction[dir][j] == dir_end:
                                    if cnt+decision(j)+decision(i)-1 < result:
                                        result = cnt+decision(j)+decision(i)-1
                            break
                        else:
                            if cnt+decision(i) <= result:
                                queue.append((nx,ny,moving[i],cnt+decision(i)))
                                visited[nx][ny] = cnt+decision(i)
                else:
                    break
    return result
# M: 세로 길이, N: 가로 길이
# 1: 동 2: 서 3: 남 4: 북
# 시작 행렬 + 방향 , 목표 행렬 + 방향

global M,N
M, N = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(M)]
# +1 되어있는 상태 (4,2) -> (3,1)
x_start,y_start,dir_start = map(int,input().split())
x_end,y_end,dir_end = map(int,input().split())
# direction : 각 방향에서 그대로,오른쪽,왼쪽,반대으로 움직이면 무슨 방향을 가르키는가?
direction = [[],[1,3,4,2],[2,4,3,1],[3,2,1,4],[4,1,2,3]]
dx = [0,0,0,1,-1]
dy = [0,1,-1,0,0]
print(bfs(x_start-1,y_start-1,dir_start,x_end-1,y_end-1,dir_end))